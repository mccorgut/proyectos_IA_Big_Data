import os
import boto3

from dotenv import load_dotenv

# Load env variables from .env file
load_dotenv()

# Get env variables
accessKeyId = os.environ.get('ACCESS_KEY_ID')
secretKey = os.environ.get('ACCESS_SECRET_KEY')
bucket = os.environ.get('BUCKET_SOURCE')
region = os.environ.get('REGION')

# Create the service Rekognition and assign credentials
rekognition_client = boto3.Session(
    aws_access_key_id=accessKeyId,
    aws_secret_access_key=secretKey,
    region_name=region).client('rekognition')


def detect_faces(img):
    # Assign parameters and call the service
    try:
        response = rekognition_client.detect_faces(
            Image={'S3Object': {'Bucket': bucket, 'Name': img}}, Attributes=['DEFAULT'])
        print("Image task recognition has been successfully run")
    except:
        raise Exception("An unexpected error was raised recognizing an image")
    return response
