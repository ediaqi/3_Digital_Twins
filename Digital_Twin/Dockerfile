###################################################################################
#                                   Base stage                                    #
###################################################################################
# syntax = docker/dockerfile:1.3
FROM python:3.10-slim-bookworm  as base

###################################################################################
#                            Production Build stage                               #
###################################################################################
FROM base as builder

ENV DEBIAN_FRONTEND=noninteractive

COPY requirements.txt ./

RUN --mount=type=cache,mode=0777,target=/root/.cache/pip \
    pip3 install --upgrade pip && \
    pip3 install --no-warn-script-location \
    --prefix=/install \
    -r requirements.txt

###################################################################################
#                              Runtime Template Stage                             #
###################################################################################
FROM base as runtime-template

ENV DEBIAN_FRONTEND=noninteractive \
    PYTHONUNBUFFERED=1 \
    PYTHONFAULTHANDLER=1 \
    PYTHONPATH=/app

WORKDIR /app

COPY --from=builder /install /usr/local

EXPOSE 8000

###################################################################################
#                             Local Development Stage                             #
###################################################################################
FROM runtime-template as local

ARG AWS_ACCESS_KEY_ID_ENC \
    AWS_SECRET_ACCESS_KEY_ENC

RUN --mount=type=cache,target=/var/cache/apt,id=apt \
    echo "Installing AWS command line interface..." \
    && apt-get update \
    && apt-get install -y curl unzip \
    && curl -s "https://awscli.amazonaws.com/awscli-exe-linux-$(uname -m).zip" -o "awscliv2.zip" \
    && unzip -qq awscliv2.zip \
    && ./aws/install \
    && rm -rf aws awscliv2.zip \
    && mkdir /root/.aws && echo """credentials""" > /tmp/creds \
    && base64 -d /tmp/creds > /root/.aws/credentials

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]

###################################################################################
#                          Frontend Development Stage                             #
###################################################################################
FROM local as local-with-frontend

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

###################################################################################
#                           Production Runtime stage                              #
###################################################################################
FROM runtime-template as prod

RUN --mount=type=cache,target=/var/cache/apt,id=apt \
    apt-get update && apt-get install -y --no-install-recommends \
    dumb-init \
    vim \
    && apt-get clean \
    && (rm -f /var/cache/apt/archives/*.deb \
    /var/cache/apt/archives/partial/*.deb /var/cache/apt/*.bin /var/lib/apt/lists/* || true)

COPY . .

ENTRYPOINT [ "/usr/bin/dumb-init", "--" ]
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
