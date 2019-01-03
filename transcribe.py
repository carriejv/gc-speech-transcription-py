import sys
import io
import os
import time
import datetime

# Imports the Google Cloud client library
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types

# Instantiates a client
client = speech.SpeechClient()

def transcribe_gcs(gcs_uri):
    """Asynchronously transcribes the audio file specified by the gcs_uri."""
    from google.cloud import speech
    from google.cloud.speech import enums
    from google.cloud.speech import types
    client = speech.SpeechClient()

    audio = types.RecognitionAudio(uri=gcs_uri)
    config = types.RecognitionConfig(
        encoding=enums.RecognitionConfig.AudioEncoding.FLAC,
        sample_rate_hertz=44100,
        language_code='en-US',
        enable_word_time_offsets=True)

    operation = client.long_running_recognize(config, audio)

    begin = time.time()
    print('Auto-Transcript: ' + gcs_uri)
    response = operation.result(timeout=60000)

    for result in response.results:
        alt = result.alternatives[0]
        print('[{}] | {}'.format(str(datetime.timedelta(seconds=alt.words[0].start_time.seconds)), alt.confidence))
        print('{}\n'.format(result.alternatives[0].transcript))

    duration = time.time() - begin
    print('Auto-Transcript Completed: Duration {}s'.format(duration))

transcribe_gcs(sys.argv[1])