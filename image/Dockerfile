# https://github.com/repejota/docker-alpine-python3/blob/master/Dockerfile

FROM alpine:3.7

RUN mkdir -p /home/omdb

COPY code/omdb /home/omdb

RUN apk add --no-cache python3 python3-dev gcc linux-headers make musl-dev g++ libffi-dev libressl-dev && \
    python3 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip3 install --upgrade pip setuptools && \    
    if [ ! -e /usr/bin/pip ]; then ln -s /usr/bin/pip3 /usr/bin/pip ; fi && \
    if [[ ! -e /usr/bin/python ]]; then ln -sf /usr/bin/python3 /usr/bin/python; fi && \
    rm -r /root/.cache

WORKDIR /home/omdb
RUN cd /home/omdb 

RUN pip3 install -r /home/omdb/requirements.txt

#CMD ["tail", "-f", "/dev/null"]

CMD ["python3", "main.py"]
