FROM cibuilds/hugo:latest

RUN apk update && apk add \
    rsync \
    vim \
    python3

# set up a working directory in /opt volume
VOLUME /opt
RUN mkdir /opt/hugo
WORKDIR /opt/hugo

ENTRYPOINT /bin/bash
