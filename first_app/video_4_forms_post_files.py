from flask import Flask, render_template, request
import pandas as pd

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

        

if __name__ == "__main__":
    app.run(host = "0.0.0.0", debug= True)