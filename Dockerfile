FROM python:3.10-slim

COPY requirements/common.txt requirements/common.txt
RUN pip install -U pip && pip install -r requirements/common.txt

COPY ./api /app/api
COPY ./bin /app/bin
COPY wsgi.py /app/wsgi.py
WORKDIR /app

RUN useradd user && usermod -aG sudo user
USER user

EXPOSE 8080

ENTRYPOINT ["bash", "/app/bin/run.sh"]
