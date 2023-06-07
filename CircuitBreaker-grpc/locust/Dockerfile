FROM python

RUN pip install locust

WORKDIR /locust
COPY ./src/locustfile.py .

CMD ["locust"]
