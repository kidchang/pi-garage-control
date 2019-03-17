FROM alpine:3.7

EXPOSE 3333
VOLUME /var/run
WORKDIR /usr/src/app

RUN apk add --no-cache \
    python3 \
    bash

COPY requirements.txt /requirements.txt
COPY app.py /usr/src/app/app.py
RUN pip3 install --no-cache-dir -r /requirements.txt

CMD [ "python3", "app.py" ]
