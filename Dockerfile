FROM python:3.9-slim


# === Create working folder and install dependencies ===
WORKDIR /app
COPY requirements.txt .
# --no-cache-dir is used to keep image small
RUN pip install --no-cache-dir -r /app/requirements.txt


# === Copy application contents ===
COPY service/ ./service/


# === Switch to non-root user (defined by IBM): ===
RUN useradd --uid 1000 theia && chown -R theia /app
USER theia


# === Run service ===
EXPOSE 8080
CMD gunicorn --bind=0.0.0.0:8080 --log-level=info service:app
