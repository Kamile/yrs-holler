from flask import Flask
app = Flask("Cats Against Catcalling")

@app.route("/hello")
def hello_world():
    return "It works!"

if __name__ == "__main__":
    app.run()
