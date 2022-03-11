FROM python:3.9.10

RUN mkdir -p /app/money_gone

WORKDIR /app/money_gone

RUN mkdir -p /app/money_gone_data

COPY . /app/money_gone/

RUN pip install -r /app/money_gone/requirements.txt

RUN python3 main.py