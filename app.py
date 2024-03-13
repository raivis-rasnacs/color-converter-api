from flask import (
    Flask,
    redirect,
    render_template,
    request,
    jsonify
)
from time import sleep

app = Flask(__name__)

app.config["SECRET_KEY"] = "secret!"

@app.route("/convert_to_hex", methods=["GET", "POST"])
def color_converter():
    dec = request.json["dec"]

    # convertion logic
    hex_number = []

    while dec:
        hex_number += [
            str(dec % 16).replace("10", "A")\
                        .replace("11", "B")\
                        .replace("12", "C")\
                        .replace("13", "D")\
                        .replace("14", "E")\
                        .replace("15", "F")
            ]
        dec //= 16

    hex_number.reverse()
    hex_number = "".join(hex_number)

    return jsonify({
        "hex":hex_number
    })

if __name__ == "__main__":
    app.run(debug=True)