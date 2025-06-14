# Use the official Ollama image
FROM ollama/ollama:latest

# Copy your local models into the container 
# Move or copy your models folder into project directory
# COPY models /root/.ollama/models

# Copy your start_service.sh script into the container
COPY start_service.sh /start_service.sh

# Expose the Ollama API port
EXPOSE 11434

# Set Ollama to listen on all interfaces
ENV OLLAMA_HOST=0.0.0.0

# Install curl for health checks
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*
RUN chmod +x /start_service.sh

ENTRYPOINT ["sh", "/start_service.sh"]
