from flask import Flask
from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def index():
    return """
<!DOCTYPE html>
<html lang="kr">
<head>
<meta charset="UTF-8">
<title>Flask Home Page</title>
</head>
<body>
<form method="GET" action="/gugu">
<h2>구구단 출력하기</h2>
<label>단 :
<input type="text" name="dan">
</label>
<button type="submit">출력</button>
</form>
</body>
</html>
"""

@app.route("/gugu")
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