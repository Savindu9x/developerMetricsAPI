FROM python:3.11.7-alpine3.19

WORKDIR /app/src
COPY . /app/src

RUN pip install flask mysql-connector-python

EXPOSE 5000

CMD ["python3", "developerMetricAPI.py"]
