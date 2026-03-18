from flask import Flask

app = Flask(__name__)


@app.route("/gugu")
def gugudan():
    dan = 3
    lines = ["<title>gugudan</title><h1>Gugudan</h1>"]
    for i in range(1, 10):
        lines.append(f"{dan} * {i} = {dan * i}<br>")
    return "\n".join(lines)


if __name__ == "__main__":
    app.run(debug=True)
    # 디버그모드 켜기. 코드 수정 시 자동으로 서버 재시작