FROM python:3.12-slim

# Install curl and uv globally
RUN apt-get update && apt-get install -y curl && \
    curl -LsSf https://astral.sh/uv/install.sh | env UV_INSTALL_DIR="/usr/local/bin" sh

# Create non-root user
RUN adduser --disabled-password --gecos "" flaskuser

# Set working directory
WORKDIR /app

# Copy the rest of the code
COPY . .

# Install Python deps (uv will create .venv in /app)
RUN uv sync && uv lock && \
    echo "--- .venv Content ---" && \
    ls -la /app/.venv && \
    echo "--- .venv/bin Content ---" && \
    ls -la /app/.venv/bin

# Add .venv to PATH so we can run `flask` directly
ENV PATH="/app/.venv/bin:$PATH"

# Expose Flask port
EXPOSE 5000

# Run Flask using correct syntax
CMD ["flask", "--app", "main", "run", "--host=0.0.0.0"]
