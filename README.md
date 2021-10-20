# AWS Certified Developer Challenges

1.1. Challenge: Polly API Example: Hello World
<p>Make a call to aws polly using aws boto3 python sdk to convert some text into some sound as an mp3 file</p>
<br>
<details>

[Code](https://github.com/cleophasmashiri/aws-cert-dev/blob/master/chapter01/polly_example.py)
<br>
Run aws configure to add follow the prompt

<br>

```

aws configure 

```


Add the following python code

```

import sys
import boto3
from decouple import config

def main():
  print('Starting ..polly')
 
  polly = boto3.client('polly')
  res = polly.synthesize_speech(Text='Hello', OutputFormat='mp3', VoiceId='Aditi')
  audio = res['AudioStream'].read()
  with open('hello.mp3', 'wb') as file:
    file.write(audio) 

  if __name__=='__main__':
    main()


``` 

Run Program


```
python polly_example.py

```

You shoud see file like 'hello.mp3.

</details>
