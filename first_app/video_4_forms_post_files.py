from flask import Flask, render_template, request, Response, send_from_directory, abort, jsonify
import pandas as pd
from pathlib import Path
import uuid

app = Flask(__name__, template_folder="templates/video4")

@app.route("/", methods=["GET", "POST"])
def index():

    if request.method == "GET":
        return render_template("index.html")
    elif request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username == "kumar" and password == "kumar":
            return "Success"
        else:
            return "Failure"
        
@app.route("/file_upload", methods = ["POST"])
def file_upload():
    file = request.files.get("file")

    print(f"file = {file}")

    if file:
        if file.content_type == "text/plain":
            return file.read().decode()
        
        if file.content_type == "application/vnd.ms-excel" or file.content_type == "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" or file.content_type == ".xlsx":
            df = pd.read_excel(file)
            return df.to_html()
        
    return "Invalid file provided"

        
@app.route("/convert_to_csv", methods = ["POST"])
def convert_to_csv():

    file = request.files["file"]

    if file:

        df = pd.read_excel(file)

        response = Response(
            df.to_csv(),
            mimetype='text/csv',
            headers={
                "Content-Disposition": "attachment; filename = result.csv"
            }
        )

        return response

@app.route('/convert_to_csv_with_download_page', methods=["POST"])
def convert_to_csv_with_download_page():
    file = request.files.get("file")

    if file:
        script_dir = Path(__file__).parent
        output_dir = script_dir.joinpath("downloads")

        if not output_dir.exists():
            output_dir.mkdir(parents=True)

        # Clear the files already present in the directory
        for fileToDelete in output_dir.iterdir():
            if fileToDelete.is_file():
                fileToDelete.unlink()

        # Read excel file
        df = pd.read_excel(file)

        filename = f'{uuid.uuid4()}.csv'

        filepath = output_dir.joinpath(filename)

        df.to_csv(filepath)

        return render_template('download.html', filename_to_download=filename)

    else:
        return "Invalid file uploaded."
            
@app.route("/download/<filename_to_download>")
def download(filename_to_download):
    script_dir = Path(__file__).parent
    output_dir = script_dir.joinpath("downloads")
    filepath = output_dir.joinpath(filename_to_download)

    if filepath.exists():
        return send_from_directory(output_dir, filename_to_download, download_name='result.csv')
    else:
        return abort(404)
    
@app.route("/handle_js_post", methods = ["POST"])
def handle_js_post():
    greeting = request.json.get('greeting')
    name = request.json.get('name')

    with open('downloads/js_post_data.txt', 'w') as f:
        f.write(f'{greeting} {name}')

    return jsonify({'message': 'Successfully stored the message! - Kumaravel'})



if __name__ == "__main__":
    app.run(host = "0.0.0.0", debug= True)