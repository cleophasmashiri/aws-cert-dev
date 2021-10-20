import sys
import boto3

def main():
  print('Starting ..polly')

  polly = boto3.client('polly')
  res = polly.synthesize_speech(Text='Hello', OutputFormat='mp3', VoiceId='Aditi')
  print(res)
  audio = res['AudioStream'].read()
  with open('hello.mp3', 'wb') as file:
    file.write(audio) 

if __name__=='__main__':
  main()
