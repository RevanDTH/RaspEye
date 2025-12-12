from flask import Flask, render_template
from requests import get
import json

app = Flask(__name__, template_folder='templates', static_folder='static')


@app.route('/')
def index():
	try:
		uri = "http://172.20.0.11:5050/api/metrics/latest"
		response = get(url=uri)
		response_data = response.json()
		if response_data.get("status") == "success" and response_data.get("data"):
			latest_metrics = response_data["data"]
		else:
			latest_metrics = {
				"cpu_percent": 0,
				"memory": 0,
				"disk_percent": 0
			}
	except:
		latest_metrics = {
			"cpu_percent": 0,
			"memory": 0,
			"disk_percent": 0
		}
	return render_template('index.html', metrics=latest_metrics)


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8080)