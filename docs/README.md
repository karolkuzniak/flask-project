# Flask Observability Demo

Example monitoring stack built with Flask, Prometheus and Grafana.

This project demonstrates how to expose application metrics and visualize them using a modern observability stack.

## Architecture

Flask application exposes metrics through `/metrics` endpoint.
Prometheus collects these metrics and Grafana visualizes them.

```
Flask → Prometheus → Grafana
```

## Tech Stack

* Python
* Flask
* Docker
* Prometheus
* Grafana
* StatsD
* Logging

## Project Structure

```
flask_project
│
├── app.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
│
├── logs
│
├── prometheus
│   └── prometheus.yml
│
└── docs
    ├── flask.png
    ├── metrics.png
    ├── prometheus.png
    └── grafana.png
```

## Running the project

Start the monitoring stack:

```
docker compose up
```

## Services

| Service    | URL                           |
| ---------- | ----------------------------- |
| Flask      | http://localhost:5000         |
| Metrics    | http://localhost:5000/metrics |
| Prometheus | http://localhost:9090         |
| Grafana    | http://localhost:3000         |

## Flask Endpoints

```
/
 /debug
 /warning
 /error
 /simulate-error
 /health
 /metrics
```

## Metrics

Application exposes metrics compatible with Prometheus:

```
flask_requests_total
flask_errors_total
```

These metrics track:

* total HTTP requests
* application errors

## Screenshots

### Flask Application

<img width="1912" height="1063" alt="Zrzut ekranu 2026-03-11 190025" src="https://github.com/user-attachments/assets/0c776453-cbef-4473-adcb-03833bd693cc" />


### Metrics Endpoint

<img width="956" height="461" alt="metrics" src="https://github.com/user-attachments/assets/7a2f93cc-3c92-433f-8afd-da85ace33873" />


### Prometheus
<img width="1919" height="1070" alt="Zrzut ekranu 2026-03-11 185252" src="https://github.com/user-attachments/assets/5ce30c6d-a9d0-4d07-a90b-b38e2e08084f" />


### Grafana

<img width="959" height="497" alt="grafana" src="https://github.com/user-attachments/assets/8b9d9781-67ee-4d3e-9b43-cb68cb90a825" />


## Features

* structured logging
* Prometheus metrics
* StatsD metrics
* error handling
* health check endpoint
* Dockerized monitoring stack

## Observability Stack

```
Flask → Prometheus → Grafana
```

This setup simulates a simplified production observability pipeline used in modern cloud environments.
