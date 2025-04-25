# Use a slim Python base
FROM python:3.11-slim

# Install prerequisites, add NodeSource repo for Node.js 20.x, then install Git and Node.js
RUN apt-get update \
 && apt-get install -y --no-install-recommends \
      curl \
      ca-certificates \
      gnupg \
 && curl -fsSL https://deb.nodesource.com/setup_20.x | bash - \
 && apt-get install -y --no-install-recommends \
      git \
      nodejs \
 && rm -rf /var/lib/apt/lists/*

# Install the Codex CLI globally
RUN npm install -g @openai/codex
