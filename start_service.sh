#!/bin/sh

# Start Ollama server in the background
ollama serve &

# Wait for Ollama to start
sleep 5

# Pull the model (do not run it, just pull)
ollama pull qwen2.5:0.5b

# Wait for the Ollama server to keep the container alive
wait