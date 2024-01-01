#!/bin/bash



while true; do
    pip install -r requirements.txt
    python3 hook.py
    echo "Restarting hook.py..."
    sleep 1
done


