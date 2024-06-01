from dotenv import load_dotenv
from flask import Flask, render_template, request, jsonify
from ice_breaker import ice_break_with

load_dotenv()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/process", methods=["POST"])
def process():
    name = request.form['name']
    summary, profile_pic_url = ice_break_with(name=name)
    return jsonify(
        dict({"picture_url": profile_pic_url,}, **summary.to_dict())
    )

if __name__ == "__main__":
    app.run(host="127.0.0.1", debug=True)