FROM cibuilds/hugo:latest

# RUN apk --no-cache add \
RUN apk update && apk add \
    rsync \
    vim \
    python3 \
    python3-dev \
    py3-setuptools \
    py3-virtualenv

# set up a working directory in /opt volume
VOLUME /opt
RUN mkdir /opt/hugo
WORKDIR /opt/hugo

COPY . /opt/hugo/
RUN python3 -m pip install --upgrade pip && \
    python3 -m pip install -r requirements.txt

ENTRYPOINT /bin/bash
