# This sends a generate request using LAN IP instead of localhost to an dockerized LLM running on port 11434
# The port is the one exposed by the docker container, which is 11434 in this case
# Replace <Your LAN IP> with your actual LAN IP address (e.g., 192.168.1.100)
# To find your LAN IP, use 'ipconfig' on Windows, 'ifconfig' on macOS, or 'ip addr' on Linux

import requests, json

url = "http://<Your LAN IP>:11434/api/generate"
data = {"model": "qwen2.5:0.5b", "prompt": "Why is the sky blue?"}

response = requests.post(url, json=data)
for line in response.iter_lines():
    if line:
        data = json.loads(line.decode())
        if "response" in data:
            print(data["response"], end="")

# Uncomment this version for localhost testing
'''
import requests, json

url = "http://localhost:11434/api/generate"
data = {"model": "qwen2.5:0.5b", "prompt": "Why is the sky blue?"}

response = requests.post(url, json=data)
for line in response.iter_lines():
    if line:
        data = json.loads(line.decode())
        if "response" in data:
            print(data["response"], end="")
'''
