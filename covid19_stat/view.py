from werkzeug.utils import redirect
from covid19_stat import app
import os
from flask import render_template, request, url_for, send_file, send_from_directory
from werkzeug.utils import secure_filename
from covid19_stat.handler.data_processor import data_processor


@app.route('/', methods=["GET", "POST"])
def index():
    
    if request.method == 'POST':

        if 'data' not in request.files:
            return redirect(url_for(request.url))
    
        data = request.files['data']
        data_extension = str(data.filename).split('.')[-1].lower()
    
        if data_extension in app.config['DATA_EXTENSIONS']:
        
            secure_data = secure_filename(data.filename)
            data.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_data))

            stat_lines, data_result, data_file = data_processor(data.filename)

            return render_template(
                "index.html",
                stat_lines=stat_lines,
                data_result=data_result,
                data_file=data_file.split('/')[-1])

    return render_template("index.html", data_file=None)

@app.route('/downloads/<path:filename>', methods=['GET'])
def download_file(filename):
    return send_file(
        os.path.join(os.getcwd(), app.config['DOWNLOAD_FOLDER'], filename))

@app.errorhandler(404)
def page_not_found(err):
    return "<center><h2>404</h2></center>"