from flask import Flask
import blueprints


app = Flask(__name__)
app.register_blueprint(blueprints.transcribe)

if __name__ == "__main__":
    app.run(debug=True)
