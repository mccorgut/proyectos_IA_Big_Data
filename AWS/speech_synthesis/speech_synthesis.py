import boto3 # Import the AWS SDK for Python language
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

# Accessing environment variables
AWS_ACCESS_KEY = os.getenv('ACCESS_KEY_ID')  # AWS Access Key
AWS_SECRET_KEY = os.getenv('ACCESS_SECRET_KEY')  # AWS Secret Key
REGION = os.getenv('REGION')  # AWS region for S3

# Initialize the S3 client
polly_client = boto3.client(
    'polly',
    aws_access_key_id=AWS_ACCESS_KEY,  # AWS Access Key ID
    aws_secret_access_key=AWS_SECRET_KEY,  # AWS Secret Access Key
    region_name=REGION  # AWS region
)

# Create parameters and call the service
try:
    response = polly_client.start_speech_synthesis_task(
        VoiceId='Lucia',
        OutputS3BucketName='my-polly-ai-bucket',
        OutputFormat='mp3', 
        Text='Cualquier tecnología suficientemente avanzada es ' +
        'indistinguible de la magia',
        TextType='text',
        SampleRate='22050')

    print("Audio file is saved into {} ".format(response['SynthesisTask']['OutputUri']))
except:
    print("Oops! An unexpected error was raised")