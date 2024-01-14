# Dockerfile
FROM python:3.8-slim-buster
# Set the working directory to /app

ENV PYTHONUNBUFFERED True

# Copy the local code to the container image.
ENV APP_HOME /backend
WORKDIR $APP_HOME
COPY . ./

RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Run the web service on container startup.
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 app:app