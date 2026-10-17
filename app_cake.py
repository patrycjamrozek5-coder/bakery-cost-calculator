from flask import Flask, render_template, request, send_from_directory

app = Flask(__name__, template_folder=".")

@app.route("/")
def bakery():
    number = request.args.get("number", "")
    cake = request.args.get("cake", "")
    error=""
    total = None
    cake_price =None

    if cake !="":
        try:
            cake_number = int(number) 

            if cake_number >= 1:
                if cake == "cheesecake":
                    cake_price = 25
                elif cake == "sponge cake":
                    cake_price = 15
                else:
                    error = "Invalid cake"
                if error=="":
                    total = cake_number * cake_price
            else:
                error = "Please, choose your cake from list"
        except ValueError:
            error = "Enter a whole number"
    return render_template(
        "cake.html",
        cake_price = cake_price,
        number=number, 
        total=total,
        error=error
    )
@app.route("/cupcake.png")
def cupcake_image():
    return send_from_directory(app.root_path, "cupcake.png")

if __name__=="__main__":
    app.run()
