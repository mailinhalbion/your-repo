#!/bin/bash

while true; do
    python3 hook.py
    echo "Restarting hook.py..."
    sleep 1
done

