# syntax=docker/dockerfile:1

FROM python:3.11
WORKDIR /usr/local/app

# Requirements commented out until they are made
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copy in the source code
COPY . .
EXPOSE 5000

# Setup an app user so the container doesn't run as the root user
RUN useradd app
USER app

CMD ["flask", "run", "--host=0.0.0.0", "--port=8080"]
