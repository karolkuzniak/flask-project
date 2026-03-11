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

![Flask](docs/flask.png)

### Metrics Endpoint

![Metrics](docs/metrics.png)

### Prometheus

![Prometheus](docs/prometheus.png)

### Grafana

![Grafana](docs/grafana.png)

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
