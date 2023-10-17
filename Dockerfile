FROM unit:1.31.0-python3.11

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY /app/ /app/app/

RUN mkdir config && chown unit:unit config

COPY ./unit.json /docker-entrypoint.d/unit.json

