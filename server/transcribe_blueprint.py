from flask import Blueprint, request
import voice_to_text

transcribe_blueprint = Blueprint('root', __name__)


@transcribe_blueprint.route("/transcribe", methods=["GET"])
def root_get():
    return """Please send a post request instead. We need an audio file. You can send the request like this:
            import requests
            file = FileStorage(
            stream=open("audio_file.wav", "rb", buffering=0),
            filename="audio_file.wav",
            content_type="audio/wav",
        )
        data = {"audio_file": file}
        result = requests.post(url, data=data)"""


@transcribe_blueprint.route("/transcribe", methods=["POST"])
def root_post():
    print(request.files)
    print(request)
    if "audio_file" in request.files.keys():
        print("got here")
        file = request.files['audio_file']
        text = voice_to_text.transcribe_audio(file, "sphinx")
        print(text)
        return '{{"text":"{text}","Code":0}}'.format(text=text)
    else:
        return '{"text":"No audio file received :(","Code":-1}'
