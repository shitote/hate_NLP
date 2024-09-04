FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /swahili_hate
COPY requirements.txt /swahili_hate/
RUN pip install -r requirements.txt
COPY . /swahili_hate/