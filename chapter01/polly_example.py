import sys
import boto3
from decouple import config

def main():
  print('Starting ..polly')
  AWS_REGION = config('aws_region_name')
  AWS_ACCESS_KEY_ID = config('aws_access_key_id')
  AWS_SECRET_KEY = config('aws_secret_access_key')

  print(AWS_REGION)
  print(AWS_ACCESS_KEY_ID)
  print(AWS_SECRET_KEY)
  polly = boto3.client('polly', region_name=AWS_REGION, aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_KEY)
  res = polly.synthesize_speech(Text='Hello', OutputFormat='mp3', VoiceId='Aditi')
  print(res)
  audio = res['AudioStream'].read()
  with open('hello.mp3', 'wb') as file:
    file.write(audio) 

if __name__=='__main__':
  main()
