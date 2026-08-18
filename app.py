#dbs prediction - v2

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/main",methods=["GET","POST"])
def main():
    return(render_template("main.html"))

@app.route("/dbs",methods=["GET","POST"])
def dbs():
    return(render_template("dbs.html"))

if __name__ == "__main__":
    app.run(port=134)

# add comments from last week again
