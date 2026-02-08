from flask import Flask, render_template, url_for, redirect

app = Flask(__name__, template_folder="templates/video3") #!

# --------------------------------------------------
# Manipulating HTML templates using Jinja
# --------------------------------------------------

# Pass strings to HTML
@app.route("/")
def index():
    return render_template("home.html", hello_str = "Hello", world_str = "World")

# Pass list to HTML
@app.route("/displaylist")
def displayList_fun():
    mylist = [10, 20, 30, 40, 50]
    return render_template("displaylist_template.html", mylist = mylist)

# --------------------------------------------------
# Custom filters
# --------------------------------------------------

@app.template_filter()
def title_case(s: str):
    newstring = ""
    for index, c in enumerate(s):
        if index % 2 == 0:
            newstring += c.upper()
        else:
            newstring += c.lower()

    return newstring

# --------------------------------------------------
# Redirect
# --------------------------------------------------

@app.route("/redirect_endpoint")
def redirect_endpoint():
    return redirect(url_for("displayList_fun"))

if __name__ == "__main__":
    app.run("0.0.0.0", debug= True)