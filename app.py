from statsd import StatsClient
import logging
from flask import Flask

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

#klient statsd
statsd = StatsClient(host='localhost', port=8125, prefix='flask_app')

@app.route('/')
def home():
    logger.info("Wywołano endpoint /")
    return "Flask works :)"

@app.route('/debug')
def debug():
    logger.info("Debug endpoint")
    return "Debug log"

@app.route('/warning')
def warning():
    logger.info("Warning endpoint")
    return "Warning log"

@app.route('/error')
def error():
    logger.info("error endpoint")
    return "Error log"

@app.route('/simulate-error')
def simulate_error():
    logger.info("Endpoint /fail został wywołany")
    raise Exception("Testowy wyjątek")

@app.errorhandler(Exception)
def handle_exception(error):
    logger.exception("Wystąpił wyjątek w aplikacji")

    #wysyłanie metryki do StatsD
    statsd.incr("exception.total")

    return {
        "error": str(error)
    }, 500

if __name__ == "__main__":
    logger.info("Starting Flask app")
    app.run(debug=True)


statsd = StatsClient(host='localhost', port=8125, prefix='flask_app')