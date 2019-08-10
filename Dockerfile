FROM cibuilds/hugo:latest

RUN apk --no-cache add \
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

ENTRYPOINT /bin/bash
