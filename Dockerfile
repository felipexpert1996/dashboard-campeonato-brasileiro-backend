FROM python:3.12.1-alpine
WORKDIR /app
COPY . /app
RUN mkdir -p ./app/static
RUN apk add build-base && pip install --upgrade pip
RUN pip install -r requirements.dev.txt