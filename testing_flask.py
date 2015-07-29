from flask import Flask
app = Flask("Cats Against Catcalling")

@app.route("/sayname/<name>")
def hello_world(name):
    return name

if __name__ == "__main__":
    app.run()
