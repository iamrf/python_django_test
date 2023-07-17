#!/bin/bash

# Start Redis server
redis-server --appendonly yes &

# Wait for Redis server to be ready
while true; do
    redis-cli ping &>/dev/null
    if [ $? -eq 0 ]; then
        break
    fi
    sleep 1
done

# Load data into Redis
cat /redis_data.txt | redis-cli --pipe

# Save the data to disk
redis-cli save

# Gracefully shutdown Redis
redis-cli shutdown

# Start redis-server
redis-server
