from flask import Flask, request, jsonify
import subprocess
import logging

app = Flask(__name__)

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Secret token for authentication (replace 'your_secret_token' with an actual secret)
SECRET_TOKEN = 'your_secret_token'

@app.route('/webhook-endpoint', methods=['POST'])
def webhook():
    data = request.json

    # Verify the secret token for authentication
    if 'secret' in data and data['secret'] == SECRET_TOKEN:
        # Check if the push is to the master branch
        if 'ref' in data and data['ref'] == 'refs/heads/master':
            try:
                # Git pull from the repository
                subprocess.run(['git', 'pull'])
                # Run deployment script or commands
                subprocess.run(['./deploy.sh'])
                logger.info('Deployment successful.')
                return jsonify({'status': 'success'}), 200
            except Exception as e:
                logger.error(f'Deployment failed. Error: {str(e)}')
                return jsonify({'status': 'error', 'message': str(e)}), 500
        else:
            return jsonify({'status': 'ignored', 'message': 'Not the master branch'}), 200
    else:
        return jsonify({'status': 'unauthorized', 'message': 'Invalid secret token'}), 401

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
