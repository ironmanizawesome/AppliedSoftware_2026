from flask import Flask
from flask import Flask, request, render_template

app = Flask(__name__)
@app.route("/")
def index():
    return """
<!DOCTYPE html>
<html lang="kr">
<head>
    <meta charset="UTF-8">
    <script
src="https://ajax.googleapis.com/ajax/libs/jquery/3.7.1/jquery.min.js"></script>
<title>Flask Home Page</title>
</head>
<body>
    <form id="form_id" method= "GET" action="javascript:post_query()">
        <h2>구구단 출력하기</h2>
        <label>단 :
        <input type="text" name="dan">
        </label>
        <button type="submit">출력</button>
    </form>
<div id="results"></div>

<script>
function post_query() {
    $.ajax({
        type: "GET",
        url: "http://127.0.0.1:5000/gugudan",
        data: $("#form_id").serialize(),
        success: update_result,
        dataType: "html"
    });
}
    function update_result(data) {
        $("#results").html(data);
}
</script>
    
</body>
</html>

"""

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