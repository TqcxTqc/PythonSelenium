FROM python:alpine3.6

WORKDIR /app

COPY requirements.txt .

RUN pip install -U pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN ["pytest", "-v"]
