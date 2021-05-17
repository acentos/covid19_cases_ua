import os, sys
from flask import Flask


app = Flask(__name__)
app.config['DATA_EXTENSIONS'] = ["csv"]
app.config['UPLOAD_FOLDER'] = os.path.join("uploads")
app.config['DOWNLOAD_FOLDER'] = os.path.join("downloads")

def create_app():
    try:
        import covid19_stat.view
    except Exception as err:
        print(f"[!] Error: {err}")
        sys.exit()