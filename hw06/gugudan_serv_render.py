from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("gugudan.html") ##이런 느낌으로 렌더 시작하기

@app.route("/gugudan")
def gugudan():
    dan = request.args.get("dan")  # 기본값은 5
    dan= int(dan)
    resp = "<html>"
    resp += "<head><title>Gugudan</title><head>"
    resp +="<body>"
    for x in range(1,10):
        resp += f"{dan} x {x} = <font color = 'blue'>{dan*x}"
        resp += "<br>"

    resp += "</body>"
    resp += "</html>"
    print(resp)

    return resp

app.run(debug=True)