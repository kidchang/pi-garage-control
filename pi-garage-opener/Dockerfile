FROM alpine:3.7

WORKDIR /usr/src/app

RUN apk add --no-cache \
    build-base \
    python3 \
    python3-dev \
    bash

COPY requirements.txt /requirements.txt
COPY opener.py /usr/src/app/opener.py
RUN pip3 install --no-cache-dir -r /requirements.txt

CMD [ "python3", "opener.py" ]
