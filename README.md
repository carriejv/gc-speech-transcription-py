# gc-speech-transcription-py

A very simple command line tool for transcribing FLAC audio files using [Google Cloud Speech Recognition](https://cloud.google.com/speech-to-text/). Also prints confidence ratings and timestamps for each section of speech within the file.

## Usage

```shell
# Console Output
pipenv run transcribe.py google-cloud-storage-uri

# File Output
pipenv run transcribe.py google-cloud-storage-uri > out.txt
```

This script is built to work with 44100 Hz FLAC files containing English speech, however it can be easily modified to fit other compatable formats and languages.

As with all Google Cloud API services, you will need to generate an API credentials file and set `GOOGLE_APPLICATION_CREDENTIALS` environement variable to the appropriate file path.

Audio files of any substantial size or length must be hosted on Google Cloud Storage for use with this API. This script is only designed for use with hosted files.

## License

[MIT](https://github.com/carriejv/gc-speech-transcription-py/blob/master/LICENSE)