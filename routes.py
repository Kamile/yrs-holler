from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/pinpoint')
def maps():
    return render_template('pinpointed.html')

@app.route('/recorded')
def recorded():
    return render_template('recorded.html')

@ap.route('/settings')
def signup():
    return render_template('signup.html')

if __name__ == '__main__':
    app.run(debug=True)