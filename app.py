from flask import Flask, jsonify
from prometheus_flask_exporter import PrometheusMetrics
import random
import time

app = Flask(__name__)
metrics = PrometheusMetrics(app)

@app.route('/api/health')
def health():
    time.sleep(random.uniform(0.1, 0.5))  # Simulate latency
    return jsonify({'status': 'healthy', 'timestamp': time.time()})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)