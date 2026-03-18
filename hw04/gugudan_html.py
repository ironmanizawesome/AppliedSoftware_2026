dan = 5

filename = "gugudandan.html"
with open(filename, "w") as f:
    f.write("<html>\n")
    f.write("<head><title>gugudan</title></head>\n")
    f.write("<body>\n")
    f.write(f"<h1>{dan}dan</h1>\n")
    for x in range(1, 10):
        print(f"{dan} x {x} = {dan * x}")
        f.write(f"{dan} x {x} = <font color='red'>{dan * x}</font><br>\n")
        f.write("<br>\n")

    f.write("</body>\n")
    f.write("</html>\n")
