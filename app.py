from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def home():
    skills = [
        "Python",
        "Flask",
        "Docker",
        "Containerization",
        "GitHub project documentation",
    ]
    return render_template("index.html", skills=skills)


@app.route("/health")
def health():
    return {"status": "healthy", "service": "flask-colorful-docker"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
