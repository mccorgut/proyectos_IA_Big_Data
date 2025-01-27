from flask import Flask, render_template, request, jsonify
import base64
import uuid
from dotenv import load_dotenv
import os
from functions.rekognition import detect_animal_s3  # Import function for detecting animals using Rekognition
from functions.mistral import generate_fun_facts  # Import function to generate fun facts about animals
from functions.analyze_labels import analyze_labels  # Import the label analysis function
import boto3

# Load environment variables from the .env file
load_dotenv()

# Accessing environment variables
AWS_ACCESS_KEY = os.getenv('ACCESS_KEY_ID')  # AWS Access Key
AWS_SECRET_KEY = os.getenv('ACCESS_SECRET_KEY')  # AWS Secret Key
BUCKET_SOURCE = os.getenv('BUCKET_SOURCE')  # Name of the S3 bucket
REGION = os.getenv('REGION')  # AWS region for S3
MISTRAL_API_KEY = os.getenv('MISTRAL_API_KEY')  # Mistral API Key for fetching fun facts

# Initialize the S3 client
s3 = boto3.client(
    's3',
    aws_access_key_id=AWS_ACCESS_KEY,  # AWS Access Key ID
    aws_secret_access_key=AWS_SECRET_KEY,  # AWS Secret Access Key
    region_name=REGION  # AWS region
)

# Initialize Flask application
app = Flask(__name__)


# Route for the home interface
@app.route('/')
def index():
    return render_template('index.html')  # Render the index HTML template


# Function to upload image to S3 (updated to support PNG and JPEG)
def upload_image_to_s3(image_data, file_extension):
    # Generate a unique filename using uuid and include the file extension
    file_name = f"uploads/{str(uuid.uuid4())}{file_extension}"

    # Set the correct content type based on the file extension
    content_type = "image/jpeg" if file_extension in ['.jpg', '.jpeg'] else "image/png"

    try:
        # Upload the image to S3 bucket
        s3.put_object(
            Bucket=BUCKET_SOURCE,  # Specify the bucket name
            Key=file_name,  # Specify the file name in the bucket
            Body=base64.b64decode(image_data),  # Decode the base64 image data
            ContentType=content_type  # Set the appropriate content type (JPEG or PNG)
        )
        print(f"Image uploaded to S3 with file name: {file_name}")  # Log successful upload
        return file_name, f"https://{BUCKET_SOURCE}.s3.amazonaws.com/{file_name}"  # Return file name and URL
    except Exception as e:
        print(f"Error uploading image to S3: {e}")  # Log any error during upload
        return None, None


# Endpoint to analyze the uploaded image
@app.route('/analyze', methods=['POST'])
def analyze():
    try:
        uploaded_file = request.files['image']  # Get the uploaded image file
        if not uploaded_file:
            return jsonify({"error": "No file uploaded"}), 400  # Return error if no file is uploaded

        # Get the file extension and check if it's .png or .jpg
        file_extension = os.path.splitext(uploaded_file.filename)[1].lower()
        if file_extension not in ['.jpg', '.jpeg', '.png']:
            return jsonify({"error": "Unsupported file type"}), 400  # Return error if the file type is not supported

        # Convert the image to base64 and upload it to S3
        image_data = base64.b64encode(uploaded_file.read()).decode('utf-8')
        file_name, file_url = upload_image_to_s3(image_data, file_extension)

        # Detect animals in the image using Rekognition
        animals = detect_animal_s3(file_name)

        if not animals:
            return jsonify(
                {"message": "No animals detected in the image"}), 200  # Return message if no animals are detected

        # Get fun facts about the detected animal
        animal_name = animals[0]  # Assume the first detected animal is the main one
        fun_facts = generate_fun_facts(animal_name)  # Fetch fun facts about the animal

        # Analyze labels detected by Rekognition
        labels = [{"Name": animal, "Confidence": 95} for animal in animals]  # Mock labels from Rekognition
        analysis = analyze_labels(labels)  # Perform analysis on labels

        # Return the image URL, detected animal, fun facts, and analysis as a JSON response
        return jsonify({
            "uploaded_image_url": file_url,
            "animal": animal_name,
            "fun_facts": fun_facts,
            "analysis": analysis
        })

    except Exception as e:
        print(f"Error: {e}")  # Log any error that occurs during processing
        return jsonify({"error": "An error occurred"}), 500  # Return a generic error message


# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)  # Enable debugging mode
