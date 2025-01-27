# Import packages
import boto3, os
from dotenv import load_dotenv

# Take environment variables from .env file
load_dotenv()

# Get env variables
accessKeyId = os.environ.get('ACCESS_KEY_ID')
secretKey = os.environ.get('ACCESS_SECRET_KEY')
region = os.environ.get('REGION')
bucketName = os.environ.get('BUCKET_NAME')

# Create the service Polly and assign credentials
polly_client = boto3.Session(
    aws_access_key_id=accessKeyId,                  
    aws_secret_access_key=secretKey,
    region_name=region).client('polly')

def speechSynthesis(request):
    # Create parameters and call the service
    try:
        response = polly_client.start_speech_synthesis_task(
            VoiceId=request['voiceId'],
            OutputS3BucketName=bucketName,
            OutputFormat='mp3', 
            Text=request['text'],
            TextType='text',
            SampleRate='22050')

        print("Audio file is saved into {} ".format(response['SynthesisTask']['OutputUri']))
    except:
        raise Exception("Oops! An unexpected error was raised")


