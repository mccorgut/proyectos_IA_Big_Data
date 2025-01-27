# Import packages
import boto3, os, base64
from flask import Flask, request, Response, abort
from dotenv import load_dotenv
from detect_faces import detect_faces
from blur_faces import anonymize_face

# Load env variables from .env file
load_dotenv()

# Get env variables
accessKeyId = os.environ.get('ACCESS_KEY_ID')
secretKey = os.environ.get('ACCESS_SECRET_KEY')
bucket_source = os.environ.get('BUCKET_SOURCE')
bucket_dest = os.environ.get('BUCKET_DEST')

# Create Flask application
application = Flask(__name__)

# Create the s3 service and assign credentials
s3 = boto3.Session(
    aws_access_key_id=accessKeyId,
    aws_secret_access_key=secretKey).resource('s3')


# api/analyze endpoint
@application.route('/api/analyze', methods=['POST'])
def analyzeImage():
    key = request.get_json()['key']
    if key is None:
        abort(400)

    try:
        response = detect_faces(key)

        fileObject = s3.Object(bucket_source, key).get()
        fileContent = fileObject['Body'].read()
        buffer_anon_img = anonymize_face(fileContent, response)

        img_enc = base64.b64encode(buffer_anon_img)
        img_dec = base64.b64decode(img_enc)
        s3.Object(bucket_dest, f"result_{key}").put(Body=img_dec)
    except Exception as error:
        print(error)
        abort(500)
    return Response(status=200)


# Run the app
if __name__ == "__main__":
    application.debug = True
    application.run()  # Running on http://127.0.0.1:5000/
