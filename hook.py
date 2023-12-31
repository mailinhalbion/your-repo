from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/webhook-endpoint', methods=['POST'])
def webhook():
    data = request.json
    if 'ref' in data and data['ref'] == 'refs/heads/master':
        # Git pull from repository
        subprocess.run(['git', 'pull'])
        # Run deployment script or commands
        subprocess.run(['./deploy.sh'])
        return jsonify({'status': 'success'}), 200
    else:
        return jsonify({'status': 'ignored'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
