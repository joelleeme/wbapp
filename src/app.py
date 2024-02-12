#!/usr/bin/env python3

from flask import Flask, request, redirect, url_for, render_template_string

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def main():
    message = ""
    if request.method == "POST":
        input_text = request.form.get("user_input", "")
        message = f"You entered: {input_text}"
    return '''
    <h2>Enter some text and submit to see it echoed back</h2>
    <form action="/" method="POST">
        <input name="user_input" placeholder="Enter something here...">
        <input type="submit" value="Submit!">
    </form>
    ''' + (f"<p><strong>{message}</strong></p>" if message else "")

if __name__ == "__main__":
    app.run(debug=True)
