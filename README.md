# Ollama LLM Docker Service

This project provides a containerized Ollama service with the `qwen2.5:0.5b` model, making it accessible over your local network.

## Features

- Dockerized Ollama service
- Pre-configured to pull and serve the `qwen2.5:0.5b` model
- Accessible via LAN IP (not just localhost)
- Simple Python client example included

## Prerequisites

- Docker installed on your system
- Python 3.x with `requests` library (for the client example)

## Getting Started

### Building and Running the Docker Container

1. Build the Docker image:

```bash
docker build -t ollama-llm .
```

2. Run the container:

```bash
docker run -d --name ollama -p 11434:11434 ollama-llm
```

3. Check if the container is running:

```bash
docker ps
```

### Finding Your LAN IP Address

#### On Windows:

1. Open Command Prompt and type:

```bash
ipconfig
```

2. Look for the "IPv4 Address" under your active network adapter (usually Ethernet or Wi-Fi).

#### On macOS:

1. Open Terminal and type:

```bash
ifconfig | grep "inet "
```

2. Look for the IP address that is not 127.0.0.1 (usually starts with 192.168.x.x or 10.x.x.x).

#### On Linux:

1. Open Terminal and type:

```bash
ip addr show | grep "inet "
```

2. Look for the IP address that is not 127.0.0.1 (usually starts with 192.168.x.x or 10.x.x.x).

### Using the API

Once you have your Host LAN IP, you can use the API from any device on your network by replacing `<Your LAN IP>` in the example code:

```python
import requests, json

url = "http://<Your LAN IP>:11434/api/generate"
data = {"model": "qwen2.5:0.5b", "prompt": "Why is the sky blue?"}

response = requests.post(url, json=data)
for line in response.iter_lines():
    if line:
        data = json.loads(line.decode())
        if "response" in data:
            print(data["response"], end="")
```

## API Documentation

For more details on the Ollama API, visit the [official Ollama documentation](https://github.com/ollama/ollama/blob/main/docs/api.md).

## Troubleshooting

### Container Issues

If the container doesn't start or you encounter issues:

```bash
# Check container logs
docker logs ollama

# Restart the container
docker restart ollama

# Remove and recreate the container
docker rm -f ollama
docker run -d --name ollama -p 11434:11434 ollama-llm
```

### Network Issues

If you can't connect to the API:

1. Ensure your firewall allows connections on port 11434
2. Verify you're using the correct LAN IP address
3. Try accessing the API from the same machine using localhost first
