from flask import Flask
import server



app = application = Flask(__name__)
app.register_blueprint(server.transcribe_blueprint)
app.debug = True


if __name__ == "__main__":
    app.run(debug=True)
