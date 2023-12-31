from flask import Flask, request, jsonify
import subprocess
from subprocess import CalledProcessError

app = Flask(__name__)

@app.route('/webhook-endpoint', methods=['POST'])
def webhook():
    try:
        data = request.json

        # Extract relevant information from the payload
        ref = data.get('ref', '')
        commits = data.get('commits', [])
        sender = data.get('sender', {})
        
        print(f"Received a push to branch: {ref}")
        
        for commit in commits:
            commit_id = commit.get('id', '')
            message = commit.get('message', '')
            author = commit.get('author', {}).get('name', '')

            print(f"  Commit ID: {commit_id}")
            print(f"  Author: {author}")
            print(f"  Message: {message}")
            print("")

        print(f"Push triggered by: {sender.get('login', '')}")

        # Perform git pull
        subprocess.run(['git', 'pull'])
        print("Git pull successful.")

        # Restart the Flask application after git pull
        restart_flask()
        # 

        return jsonify({'status': 'success'}), 200

    except Exception as e:
        print(f"Error during webhook processing: {e}")
        return jsonify({'status': 'error', 'message': str(e)}), 500

def restart_flask():
    try:
        # Restart the Flask application
        subprocess.run(['python3', 'hook.py'])
        print("Restarted Flask application successfully. ")
    except CalledProcessError as e:
        print(f"Error during Flask application restart: {e}")

def run_app():
    try:
        # Restart the Flask application
        subprocess.run(['python3', 'app.py'])
        print("run app.py successfully. ")
    except CalledProcessError as e:
        print(f"Error during app.py run: {e}")

if __name__ == '__main__':
    run_app()
    app.run(host='0.0.0.0', port=5000)
