# AWS Certified Developer Challenges

1.1. Challenge: Polly API Example: Hello World
<p>Make a call to aws polly using aws boto3 python sdk to convert some text into some sound as an mp3 file</p>
<br>
<details>

Add system environment variables on you machine

<br>
For macos it would be in the file: ~/.bash_profile.

```

export aws_region_name="your aws region"
export aws_access_key_id="your aws access key id"
export aws_secret_access_key="your aws secret key"

```

Add the following python code

```

import sys
import boto3
from decouple import config

def main():
  print('Starting ..polly')
  AWS_REGION = config('aws_region_name')
  AWS_ACCESS_KEY_ID = config('aws_access_key_id')
  AWS_SECRET_KEY = config('aws_secret_access_key')

  polly = boto3.client('polly', region_name=AWS_REGION, aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_KEY)
  res = polly.synthesize_speech(Text='Hello', OutputFormat='mp3', VoiceId='Aditi')
  audio = res['AudioStream'].read()
  with open('hello.mp3', 'wb') as file:
    file.write(audio) 

if __name__=='__main__':
  main()


``` 

Install  python-decouple

```

 pip install python-decouple

```

Run Program

```
python polly_example.py

```

You shoud see file like 'hello.mp3 with some sound as you entered above'

</details>
