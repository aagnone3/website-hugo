FROM cibuilds/hugo:latest

# RUN apk --no-cache add \
RUN apk update && apk add \
    rsync \
    vim \
    python3 \
    python3-dev \
    py3-setuptools \
    py3-virtualenv

# setting UID to 1000 avoids permissions issues when mapping volumes and/or mounting
RUN addgroup -g 1000 -S group
RUN adduser -u 1000 -S user -G group

# set up a working directory in /opt volume
VOLUME /opt
RUN mkdir /opt/hugo && \
    chown user:group /opt/hugo

WORKDIR /opt/hugo
COPY . /opt/hugo/
RUN python3 -m pip install --upgrade pip && \
    python3 -m pip install -r requirements.txt

USER user
