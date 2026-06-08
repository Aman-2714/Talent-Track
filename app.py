from flask import Flask
from config import Config
from routes.main_routes import main_bp
import os

app = Flask(__name__)
app.config.from_object(Config)

os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)

app.register_blueprint(main_bp)

if __name__ == "__main__":
    app.run(debug=True, port=2714)
