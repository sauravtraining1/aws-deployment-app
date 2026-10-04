from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, My Application is running!'

@app.route("/health")
def health():
    return {
        "status": "healthy"
    }

@app.route("/version")
def version():
    return {
        "application": "aws-deployment-app",
        "version": "1.0.0"
    }

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5001,
        debug=True
    )

