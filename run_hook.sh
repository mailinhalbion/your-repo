#!/bin/bash



while true; do
    pip3 install -r requirements.txt
    python3 hook.py
    echo "Restarting hook.py..."
    sleep 2
done


