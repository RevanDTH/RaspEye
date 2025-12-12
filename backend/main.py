from flask import Flask,request
import json

app = Flask(__name__)

payload_obj = None


@app.route('/update_metrics', methods=["POST"])
def update_metrics():
	payload = request.data
	global payload_obj
	try:
		payload_obj = json.loads(payload.decode('utf-8'))
	except Exception:
		payload_obj = None

	if payload_obj:
		return "success"
	else:
		return "false"
	
@app.route('/debug')
def debug_return():
	if isinstance(payload_obj, dict):
		return payload_obj
	else:
		return "No metrics found"





if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5050)