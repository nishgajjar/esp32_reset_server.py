from flask import Flask

app = Flask(__name__)

@app.route('/reset', methods=['GET'])
def reset_esp32():
    return "RESET", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
