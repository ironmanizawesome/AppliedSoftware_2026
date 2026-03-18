from flask import Flask

app = Flask(__name__)


@app.route("/gugu")
def gugudan():
    resp = "<html>"
    resp += "<head><title>gugudan</title></head>"
    resp += "<body>"
    dan = 5
    for x in range(1, 10):
        print(f"{dan} * {x} = {dan * x}")
        resp += f"{dan} * {x} = {dan * x}<br>"
    resp += "</body>"
    resp += "</html>"
    print(resp)

    return resp


if __name__ == "__main__":
    app.run(debug=True)
