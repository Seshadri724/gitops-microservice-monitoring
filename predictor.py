import requests
import time
import statsmodels.api as sm
import pandas as pd
from datetime import datetime

def fetch_metrics():
    # Simulate fetching latency metrics from Prometheus
    response = requests.get('http://localhost:5000/api/health')
    return response.json()['timestamp']

def predict_latency_spike(data, threshold=0.4):
    df = pd.DataFrame(data, columns=['timestamp'])
    model = sm.tsa.ARIMA(df, order=(1,1,0)).fit()
    forecast = model.forecast(steps=1)
    if forecast.iloc[0] > threshold:
        send_slack_alert(f"Predicted latency spike: {forecast.iloc[0]:.2f}s")

def send_slack_alert(message):
    webhook_url = "YOUR_SLACK_WEBHOOK_URL"
    payload = {"text": message}
    requests.post(webhook_url, json=payload)

if __name__ == "__main__":
    metrics = []
    for _ in range(10):
        metrics.append(fetch_metrics())
        time.sleep(1)
    predict_latency_spike(metrics)