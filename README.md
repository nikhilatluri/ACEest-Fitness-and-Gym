# ACEest-Fitness-and-Gym


# Flask Fitness App

A lightweight Flask web application for fitness tracking, packaged with Docker for consistency across development, testing, and deployment. Automated testing and CI/CD are enabled via GitHub Actions.

---

## Local Setup & Running the Application

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/your-repo.git
   cd your-repo



2. **Install dependencies (optional, for running outside Docker):**
   ```bash 
   python3 -m venv venv 
   source venv/bin/activate
   pip install -r requirements.txt



3. **Run the application:**
    ```bash
    flask run

By default, the app runs on http://localhost:5000.


4. **Run with Docker (recommended):**
   ```bash
   docker build -t flask-fitness-app .
   docker run -p 5000:5000 flask-fitness-app




## Running Tests Locally


### With Pytest (outside Docker):
   ```bash
   pytest pytest/
```
     


### With Docker:
   ```bash
   docker run --rm flask-fitness-app pytest pytest/
```




## GitHub Actions CI/CD Pipeline Overview

Trigger: Automatically runs on every push or pull request.
Build: Builds the Docker image using the provided Dockerfile.
Test: Executes all Pytest unit tests inside the built Docker container to ensure application stability.
Fail Fast: If any test fails, the pipeline fails and blocks merging.

You can find the workflow configuration in .github/workflows/ci-cd.yml.

## Project Structure
   ```bash
ACEest-Fitness-and-Gym/
│
├── app.py
├── controller.py
├── api_v1.py
├── html.py
├── requirements.txt
├── Dockerfile
├── .dockerignore
├── pytest/
│   ├── conftest.py
│   └── test_app.py
└── .github/
    └── workflows/
        └── ci-cd.yml
```


## Key Configuration Files
Below are the main configuration files required for Dockerization and CI/CD.
Copy each code block into its respective file in your repository.

### Dockerfile
```bash
FROM python:3.10-slim

WORKDIR /app

RUN apt-get update && apt-get install -y gcc libpq-dev && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_ENV=production

CMD ["flask", "run"]
```


### requirements.txt
```bash
click==8.1.7
Flask==2.2.5
Flask-Login==0.6.3
Flask-SQLAlchemy==3.0.5
greenlet==3.1.1
itsdangerous==2.1.2
Jinja2==3.1.6
MarkupSafe==2.1.5
SQLAlchemy==2.0.43
typing_extensions==4.7.1
Werkzeug==2.2.3
pytest==8.4.1
pre-commit
```



## .dockerignore
```bash
__pycache__/
*.pyc
*.pyo
*.pyd
pytest/
.env
.git
```


### github/workflows/ci-cd.yml
```bash
name: CI/CD Pipeline

on: [push, pull_request]

jobs:
  build-and-test:
    runs-on: ubuntu-latest

    steps:
      # Step 1: Checkout code
      - name: Checkout repository
        uses: actions/checkout@v4

      # Step 2: Set up Docker Buildx (for cross-platform builds and caching)
      - name: Set up Docker Buildx
        uses: docker/setup-buildx-action@v3

      # Step 3: Build Docker image
      - name: Build Docker image
        uses: docker/build-push-action@v5
        with:
          context: .
          file: ./Dockerfile
          tags: flask-fitness-app:latest
          load: true  # Loads image into Docker for next steps

      # Step 4: Run Pytest tests inside the built Docker image
      - name: Run Pytest in Docker container
        run: |
          docker run --rm flask-fitness-app:latest pytest pytest/
```


## Questions or Contributions
Feel free to open issues or pull requests for improvements, bug fixes, or questions!
```bash

**Copy and paste this entire content into your README.md file.**  
If you need sample code for `app.py` or your tests, or want to extend this with deployment or environment variable management, just let me know!
```

