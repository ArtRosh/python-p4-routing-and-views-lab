#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return f"<h1>Python Operations with Flask Routing and Views</h1>"

@app.route("/print/<parameter>")
def print_string(parameter):
    print(parameter)
    return parameter

@app.route("/count/<parameter>")
def count(parameter):
    num = int(parameter)
    output = [] #list of strings
    for param in range(num):
       output.append(str(param)) 
    
    res = "\n".join(output) + "\n"
    return res

@app.route("/math/<num1>/<operation>/<num2>")
def math(num1, operation, num2):
    a = int(num1)
    b = int(num2)
    
    if operation == "+":
        result = a + b
    elif operation == "-":
        result = a - b
    elif operation == "*":
        result = a * b
    elif operation == "div":
        result = a / b
    elif operation == "%":
        result = a % b
    return str(result)


if __name__ == '__main__':
    app.run(port=5555, debug=True)
