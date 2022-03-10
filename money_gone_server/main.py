from flask import Flask, render_template

app = Flask(__name__)

@app.route("/index", methods=["GET"])
def boot():
    path = "/app/money_gone/data"
    return render_template("/app/money_gone/data/index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)