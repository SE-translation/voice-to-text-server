from flask import Flask
from .transcribe_blueprint import transcribe_blueprint


app = application = Flask(__name__)
app.register_blueprint(transcribe_blueprint)
app.debug = True


if __name__ == "__main__":
    app.run(debug=True)
