from flask import Flask, request, jsonify
import subprocess
from subprocess import CalledProcessError
import os
import signal
import sys

app = Flask(__name__)
app_process = None
app_name = "app.py"

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
            message = commit.get('message', '')
            author = commit.get('author', {}).get('name', '')

            print(f"  tac gia: {author}")
            print(f"  Message: {message}")
            print("")

        print(f"Push triggered by: {sender.get('login', '')}")

        # Perform git pull
        subprocess.run(['git', 'pull'])

        # Restart the Flask application after git pull
        if app_process:
            terminate_process(app_process)
        restart_flask()
        

        return jsonify({'status': 'success'}), 200

    except Exception as e:
        print(f"Error during webhook processing: {e}")
        return jsonify({'status': 'error', 'message': str(e)}), 500

def restart_flask():
    try:
        # Get the process ID of the current running script
        current_pid = os.getpid()
        print(f"chay trong nen {current_pid}")

        # Restart the script by sending a signal
        os.kill(current_pid, signal.SIGTERM)

    except CalledProcessError as e:
        print(f"Error during Flask application restart: {e}")
        sys.exit(1)

def terminate_process(process):
    process.terminate()
    process.wait()

if __name__ == '__main__':
    
    app_process = subprocess.Popen(['python3', app_name])
    app.run(host='0.0.0.0', port=5000)
