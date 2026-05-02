FROM python:3.9-slim

# Create application workdir and install dependencies
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy service package
COPY service/ ./service/

# Use non-root user
RUN useradd --uid 1000 theia && chown -R theia /app
USER theia

EXPOSE 8080
CMD ["gunicorn", "--bind=0.0.0.0:8080", "--log-level=info", "service:app"]
