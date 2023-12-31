from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook-endpoint', methods=['POST'])
def webhook():
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

    return jsonify({'status': 'success'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
