from flask import Flask, request

app = Flask(__name__)

def boilmsg(minute):
    if minute <0:
        return "알이 닭 안으로 다시 갈 순 없잖아.."
    elif minute <= 5:
        return "날계란을 먹고 싶은 거구나~?"
    elif minute <= 7:
        return "일본 라멘가게의 감동을 담은 반숙란!"
    elif minute <= 8:
        return  "촉촉한 노른자를 가진 반숙!"
    elif minute <= 9:
        return "반숙인가? 완숙인가?"
    elif minute <= 10:
        return "완숙!"
    elif minute <= 12:
        return  "좀 퍽퍽하네.."
    elif minute <= 17:
        return "아이고 흰자가 타버렸네..!"
    else :
        return "넌 요리하지마라.. 이게 숯덩어리여 뭐여"


def frymsg(minute):
    if minute <0:
        return "당신이 스티븐 호킹이야?"
    elif minute <= 1:
        return "후라이팬은 접시가 아니야.."
    elif minute <= 2:
        return "거 참 참을성이 없는 사람이네.."
    elif minute <= 3:
        return  "이규현이 좋아하는 반숙 후라이! 합격!"
    elif minute <= 4:
        return "적당히 익었네~"
    elif minute <= 5:
        return  "완숙!"
    elif minute <= 7:
        return "바닥면이 흰색이어야 하는데 왜 검정이지..?"
    else:
        return "이야 이건 나중에 석유로 변하겠다야"




@app.route("/")
def index():
    return """
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>계란 삶기 프로그램</title>
</head>
<body>
    <h1>당신만의 삶은 계란을 만들어보세요!</h1>
    <br><hr>
    <h2>얼마동안 계란을 삶을까요?</h2>
    <form method="GET" action="/egg">
    <label>시간(분):
        <input type="text" name="time">
        </label>
        <button type="submit">삶기!</button>
        <button type="submit" name="mode" value="fry">싫어!</button>
    </form>
   
</body>
</html>
"""

@app.route("/egg")
def egg():
    mode = request.args.get("mode", "")
    user_input = request.args.get("time", "").strip()

    if mode == "fry":
        return """
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <title>계란 프라이 프로그램</title>
</head>
<body>
    <h1>오늘은 내가 계란후라이 요리사!</h1>
    <br><hr>
    <h2>계란을 프라이팬에 얼마동안 튀길까요?</h2>

    <form method="GET" action="/fry">
        <label>시간(분):
            <input type="text" name="time">
        </label>
        <button type="submit">제출</button>
    </form>
</body>
</html>
"""

    if user_input.isdigit():
        minute = int(user_input)
        msg = boilmsg(minute)
    else:
        msg = "정수만 입력하세요."

    return f"""
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <title>계란 삶기 결과</title>
</head>
<body>
    <h2>계란 삶기 결과</h2>
    <p>입력 시간: {user_input}분</p>
    <p><font color="blue">{msg}</font></p>
    <a href="/">처음으로 돌아가기</a>
</body>
</html>
"""

@app.route("/fry")
def fry():
    user_input = request.args.get("time", "").strip()

    if user_input.isdigit():
        minute = int(user_input)
        msg = frymsg(minute)
    else:
        msg = "정수만 입력하세요."

    return f"""
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <title>계란 프라이 결과</title>
</head>
<body>
    <h2>계란 프라이 결과</h2>
    <p>입력 시간: {user_input}분</p>
    <p><font color="red">{msg}</font></p>
    <a href="/">처음으로 돌아가기</a>
</body>
</html>
"""

if __name__ == "__main__":
    app.run(debug=True)