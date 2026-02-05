from flask import Flask, request, make_response

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World!"

#--------------------
# Path URL parameters
#--------------------

# Getting a string and displaying a string
@app.route("/hello/<name>")
def hello(name):
    return f"Hello {name}!"

# Getting a string but wanting it to behave like numbers
@app.route("/add_wrong/<num1>/<num2>")
def add_wrong(num1, num2):
    return f"{num1} + {num2} = {num1 + num2}" # For num1 = 20 and num2 = 30, this returns 2030.

# Getting path params as int and not as string
@app.route("/add/<int:num1>/<int:num2>")
def add(num1, num2):
    return f"{num1} + {num2} = {num1 + num2}" # Correct sum of 20 + 30 = 50 is shown.

#--------------------
# Query URL parameters
#--------------------
@app.route("/login")
def handle_params():
   username = request.args.get("username") 
   password = request.args.get("password")

   return f"Username: {username} <br>Password: {password}"


#------------------------------------------------------------
# GET vs POST request and handling them separately in flask
#------------------------------------------------------------

# Configure method to allow both flask GET and POST methods
@app.route("/getandpost", methods = ["GET", "POST"])
def getandpost():
    if request.method == "GET":
        return "GET method used."
    elif request.method == "POST":
        return "POST method used."
    else:
        return "This message will never be returned."


#--------------------
# Returning status codes
#--------------------

# Directly in return statement
@app.route("/get202status")
def get202status():
    return "get200status() method successfully called.", 202

# Using make_response()
@app.route("/get202statuswithmakeresponse")
def get202statuswithmakeresponse():
    response = make_response()

    response.status_code = 202
    response.data = "get202statuswithmakresponse() successfully called"
    response.content_type = "text/customkumartext" #!!!!

    return response




if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)