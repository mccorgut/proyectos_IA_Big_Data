import boto3
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Retrieve AWS credentials and configuration from environment variables
AWS_ACCESS_KEY = os.environ.get('ACCESS_KEY_ID')  # AWS Access Key ID
AWS_SECRET_KEY = os.environ.get('ACCESS_SECRET_KEY')  # AWS Secret Access Key
BUCKET_SOURCE = os.environ.get('BUCKET_SOURCE')  # S3 bucket name
REGION = os.environ.get('REGION')  # AWS region for Rekognition and S3

# Initialize the Rekognition client using AWS credentials and region
rekognition = boto3.client(
    'rekognition',
    aws_access_key_id=AWS_ACCESS_KEY,  # AWS Access Key ID
    aws_secret_access_key=AWS_SECRET_KEY,  # AWS Secret Access Key
    region_name=REGION  # AWS region
)

# Animal detection function (version 2.0)
def detect_animal_s3(file_name):
    try:
        # Use Rekognition's detect_labels function to identify labels in the image stored in S3
        response = rekognition.detect_labels(
            Image={'S3Object': {'Bucket': BUCKET_SOURCE, 'Name': file_name}},  # S3 bucket and file name
            MaxLabels=10,  # Limit the number of labels returned
            MinConfidence=70  # Only return labels with confidence of at least 70%
        )

        # Print the full response from Rekognition for debugging
        print("Rekognition Response:", response)

        # Print each label and its associated categories
        for label in response['Labels']:
            print(f"Label: {label['Name']}, Categories: {label['Categories']}")

        # Filter labels to include only those related to animals
        animals = [label['Name'] for label in response['Labels'] if
                   'Animals and Pets' in [category['Name'] for category in label['Categories']]]

        # Print the detected animals
        print("Detected animals:", animals)

        # Return the list of detected animals, or None if no animals are detected
        if not animals:
            print("No animals detected")
            return None
        return animals

    except Exception as e:
        # Print any error that occurs during the detection process
        print(f"Error detecting animals: {e}")
        return None
