import sys

sys.path.append('/anaconda/lib/python2.7/site-packages')

from load import app, application

application
app

if __name__ == "__main__":
    app.run("0.0.0.0")
