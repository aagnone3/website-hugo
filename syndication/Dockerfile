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

COPY . .
RUN python3 -m pip install --upgrade pip && \
    python3 -m pip install -r requirements.txt

WORKDIR /home/user
USER user
