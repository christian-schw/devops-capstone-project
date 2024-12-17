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
# According to Docker Terminal: 
# "JSON arguments recommended for CMD to prevent unintended behavior
# related to OS signals" (JSON arguments is the exec form, see Docker doc).
CMD ["gunicorn", "--bind=0.0.0.0:8080", "--log-level=info" , "service:app"]

# OpenShift service / route URL to access microservice:
# https://accounts-sn-labs-christians21.labs-prod-openshift-san-a45631dc5778dc6371c67d206ba9ae5c-0000.us-east.containers.appdomain.cloud/
