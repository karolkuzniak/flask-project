from statsd import StatsClient
import logging
from flask import Flask
from prometheus_client import Counter, generate_latest
from flask import Response

#logging configuration
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("logs/app.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)
app = Flask(__name__)

#client statsd
statsd = StatsClient(host='localhost', port=8125, prefix='flask_app')

#Prometheus metrics
REQUEST_COUNT = Counter(
    "flask_requests_total",
    "Total number of HTTP requests"
)

ERROR_COUNT = Counter(
    "flask_errors_total",
    "Total number of application errors"
)

#counting all requests
@app.before_request
def before_request():
    REQUEST_COUNT.inc()

#endpoint for Prometheus
@app.route("/metrics")
def metrics():
    return Response(generate_latest(), mimetype="text/plain")

@app.route('/')
def home():
    logger.info("output endpoint /")
    return "Flask works :)"

@app.route('/debug')
def debug():
    logger.debug("Debug endpoint")
    return "Debug log"

@app.route('/warning')
def warning():
    logger.warning("Warning endpoint")
    return "Warning log"

@app.route('/error')
def error():
    logger.error("error endpoint")
    return "Error log"

@app.route('/simulate-error')
def simulate_error():
    logger.info("Endpoint /fail został wywołany")
    raise Exception("Testowy wyjątek")

#handling exceptions
@app.errorhandler(Exception)
def handle_exception(error):
    logger.exception("Wystąpił wyjątek w aplikacji")

    #wysyłanie metryki do StatsD
    statsd.incr("exception.total")

    #Prometheus metrics
    ERROR_COUNT.inc()

    return {"error": str(error)}, 500

@app.route("/health")
def health():
    return {"status": "ok"}

if __name__ == "__main__":
    logger.info("Starting Flask app")
    app.run(host="0.0.0.0", port=5000)