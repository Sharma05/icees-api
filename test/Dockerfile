FROM python:3.8

COPY . /icees-api
RUN pip install -r icees-api/requirements.txt
RUN pip install -r icees-api/requirements-test.txt

WORKDIR /icees-api

ENTRYPOINT ["pytest"]

