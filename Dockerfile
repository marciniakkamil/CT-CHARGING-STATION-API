FROM python:3.12.2-slim

WORKDIR /app

# env variables
# python -B
ENV PYTHONDONTWRITEBYTECODE 1
# python -u
ENV PYTHONUNBUFFERED 1

COPY requirements.txt ./

# install requirements without cache dir for Docker
RUN pip install --no-cache-dir -r requirements.txt

COPY . .