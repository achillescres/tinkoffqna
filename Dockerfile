FROM mirror.gcr.io/library/python:3.10.12-slim-bookworm as build

RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc
# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt .

RUN pip install "cython<3.0.0" wheel
RUN pip install "pyyaml==5.4.1" --no-build-isolation
RUN pip install -r requirements.txt

EXPOSE 8080

#ENTRYPOINT ["uvicorn", "app.main:app", "--port", "8080"]
ENTRYPOINT ["python3", "main.py"]
