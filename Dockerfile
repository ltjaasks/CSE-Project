# syntax=docker/dockerfile:1
# Stage 1
FROM python:3.11 as builder
WORKDIR /app

# Requirements commented out until they are made
COPY requirements.txt .
RUN pip install --upgrade pip
# Install dependencies
RUN pip install -r requirements.txt
# Copy the source code
COPY . .
RUN rm requirements.txt

# Stage 2
FROM builder
WORKDIR /app
# Copy installed dependencies from stage 1
COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
# Copy app source code
COPY --from=builder /app/* .

ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=8080

EXPOSE 8080

# Setup an app user so the container doesn't run as the root user
RUN useradd app
USER app

CMD ["flask", "run"]
