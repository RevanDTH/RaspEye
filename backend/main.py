from flask import Flask, request, jsonify
import json

app = Flask(__name__)

# Centralized metrics store
payload_obj = None


@app.route('/api/metrics/update', methods=["POST"])
def update_metrics():
	"""Receive metrics update from agent"""
	global payload_obj
	try:
		payload = request.data
		payload_obj = json.loads(payload.decode('utf-8'))
		return jsonify({
			"status": "success",
			"message": "Metrics updated successfully",
			"data": payload_obj
		}), 200
	except Exception as e:
		return jsonify({
			"status": "error",
			"message": f"Failed to update metrics: {str(e)}",
			"data": None
		}), 400


@app.route('/api/metrics/latest')
def latest_metrics():
	if isinstance(payload_obj, dict):
		return jsonify({
			"status": "success",
			"message": "Latest metrics retrieved",
			"data": payload_obj
		}), 200
	else:
		return jsonify({
			"status": "error",
			"message": "No metrics found",
			"data": None
		}), 404





if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5050)