from flask import Flask
from user_server import user_server
from medical_server import medical_server
import os

app = Flask(__name__)
app.register_blueprint(user_server, url_prefix = "/user")
app.register_blueprint(medical_server, url_prefix = "/medical")
app.secret_key = os.urandom(16)


if __name__ == "__main__":
    app.run()