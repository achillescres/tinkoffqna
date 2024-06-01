FROM dockerhub.timeweb.cloud/python-3.10-slim as build
WORKDIR /app

RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc

COPY requirements.txt .
RUN pip install -r requirements.txt

EXPOSE 8080

ENTRYPOINT ["uvicorn", "app.main:app", "--port", "8080"]