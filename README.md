# DevOps Project 1 — Dockerized Python Application

## Project Overview

This project demonstrates how to containerize a Python application and deploy it using Docker and Docker Compose.

The application is served through an Nginx reverse proxy running in a separate container.

The project was built and tested on an AWS EC2 instance.

---

## Architecture

```text
                    Internet
                       |
                       v
                AWS EC2 :8081
                       |
                       v
                  Nginx :80
                       |
                Docker Network
                       |
                       v
                  App :5000
                       |
                       v
                Python Application
---

## Technologies Used

- Python
- Git & GitHub
- Docker
- Docker Compose
- Nginx
- AWS EC2
- Linux

---

## Project Structure

devops-project-1/
├── app.py
├── Dockerfile
├── compose.yaml
├── nginx.conf
├── .dockerignore
└── README.md


### Next section: Dockerfile

Add this below it:

```markdown
---

## Dockerfile

The Dockerfile defines how the Python application image is built.

```dockerfile
FROM python:3.12-slim

WORKDIR /app

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]

---

## Docker Compose

Docker Compose is used to define and run the multiple containers required for the project.

This project has two services:

1. `app` — Python application
2. `nginx` — Nginx reverse proxy

```yaml
services:
  app:
    build: .
    environment:
      APP_ENV: production
      APP_VERSION: "2.0"

  nginx:
    image: nginx:latest
    ports:
      - "8081:80"
    volumes:
      - ./nginx.conf:/etc/nginx/conf.d/default.conf:ro
---

## Nginx Reverse Proxy

Nginx is used as a reverse proxy in front of the Python application.

The Nginx configuration is stored in `nginx.conf`:

```nginx
server {
    listen 80;

    location / {
        proxy_pass http://app:5000;
    }
}
---

## How to Run

### 1. Clone the repository

```bash
git clone <your-github-repository-url>
cd devops-project-1
docker compose up -d
docker compose ps
# List running containers
docker ps

# List all containers
docker ps -a

# View application logs
docker compose logs app

# View Nginx logs
docker compose logs nginx

# Stop the Compose services
docker compose stop

# Start the Compose services
docker compose start

# Stop and remove the Compose containers
docker compose down

# Rebuild and start the services
docker compose up -d --build
