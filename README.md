# Flask Colorful Docker App

A recruiter-friendly Python Flask web application packaged with Docker. The app serves a colorful hello-world page and exposes a `/health` endpoint, making it a clear portfolio example for backend development, containerization, and clean GitHub documentation.

## Recruiter Quick Review

This project demonstrates that I can build, package, run, and document a Python web application using modern developer workflow practices.

Key highlights:

- Built a Flask web app with server-rendered HTML templates.
- Designed a colorful responsive frontend with CSS.
- Added a JSON health-check endpoint for service monitoring.
- Containerized the app with Docker.
- Added Docker Compose for one-command local execution.
- Served the app with Gunicorn for a production-style runtime.
- Documented setup and usage clearly for GitHub reviewers.

## Two-Minute Evaluation

If you are reviewing this project quickly:

1. Open `app.py` to see the Flask routes.
2. Open `Dockerfile` to see how the app is containerized.
3. Open `docker-compose.yml` to see how the service runs.
4. Open `templates/index.html` and `static/css/styles.css` to see the UI.
5. Run `docker compose up --build` and visit `http://localhost:5000`.

## What This Project Shows

- Python Flask web development
- HTML and CSS template rendering
- Docker image creation
- Docker Compose usage
- Production-style app serving with Gunicorn
- Clean project documentation for GitHub

## Tech Stack

| Area | Technology |
| --- | --- |
| Backend | Python, Flask |
| Frontend | HTML, CSS, Jinja templates |
| Server | Gunicorn |
| Containerization | Docker |
| Local orchestration | Docker Compose |
| Version control | Git, GitHub |

## Project Structure

```text
.
|-- app.py
|-- Dockerfile
|-- docker-compose.yml
|-- requirements.txt
|-- .dockerignore
|-- .gitignore
|-- GITHUB_PORTFOLIO_GUIDE.md
|-- static/
|   `-- css/
|       `-- styles.css
`-- templates/
    `-- index.html
```

## Why Docker Is Useful

Docker packages an application, dependencies, and runtime into a container image. This allows the app to run the same way on a laptop, another developer's machine, a cloud server, or a CI/CD pipeline.

Without Docker, someone may need to manually install Python, create a virtual environment, install dependencies, and solve version issues. With Docker, they can build and run the app using a few commands.

For recruiters and engineering teams, Docker shows that the project is not only source code. It is prepared to run in a consistent environment.

## How The Project Was Created

1. Created a Flask application in `app.py`.
2. Added a colorful HTML page in `templates/index.html`.
3. Added styling in `static/css/styles.css`.
4. Listed Python dependencies in `requirements.txt`.
5. Created a `Dockerfile` that builds the Python environment and starts the app.
6. Added `docker-compose.yml` to run the container with one simple command.
7. Added `.dockerignore` and `.gitignore` to keep the repository clean.
8. Wrote this README so recruiters and developers can understand the project quickly.

## Run Locally Without Docker

Use these commands if you want to run the app directly with Python:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

On Windows PowerShell, activate the virtual environment with:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python app.py
```

Open the app:

```text
http://localhost:5000
```

## Run With Docker

Build the Docker image:

```bash
docker build -t flask-colorful-docker .
```

Run the container:

```bash
docker run -p 5000:5000 flask-colorful-docker
```

Open the app:

```text
http://localhost:5000
```

## Run With Docker Compose

Docker Compose is the easiest way to run this project:

```bash
docker compose up --build
```

Stop the app:

```bash
docker compose down
```

## Test The Health Endpoint

Open this URL in your browser:

```text
http://localhost:5000/health
```

Expected response:

```json
{
  "service": "flask-colorful-docker",
  "status": "healthy"
}
```

## GitHub Repository Description

Use this description for the repository:

```text
A colorful Python Flask app containerized with Docker and documented for beginner-friendly deployment.
```

## Suggested GitHub Topics

Add these topics on GitHub so recruiters can find the project:

```text
python
flask
docker
docker-compose
gunicorn
web-development
containerization
portfolio-project
```

## Resume Project Description

```text
Flask Colorful Docker App
- Built a Python Flask web application with Jinja templates, responsive CSS, and a health-check endpoint.
- Containerized the application using Docker and served it with Gunicorn for a production-style runtime.
- Added Docker Compose and clear documentation so the project can be reviewed and run easily from GitHub.
```

## Interview Explanation

```text
I built this project to show that I understand the full path from writing a Python Flask app to packaging it with Docker. The Flask app renders a colorful page and exposes a health endpoint. The Dockerfile builds a lightweight Python image, installs dependencies, copies the app, exposes port 5000, and starts the service with Gunicorn. Docker Compose makes the project easy to run with one command.
```

## Next Improvements

- Add automated tests with `pytest`.
- Add GitHub Actions to build the Docker image.
- Deploy the app to Render, Railway, Fly.io, or AWS.
- Add a form or API endpoint to make the app more interactive.
