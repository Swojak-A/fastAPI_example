FROM python:3.8-slim

# set MODE for pip requirements ('prod'|'stage'|'') defult: '' (installs dev requirements)
ARG MODE
ARG DOCKER_USER

# tell python not to buffer stdout
ENV PYTHONUNBUFFERED=1

# os dependencies
RUN apt-get update -y && \
    apt-get -y install --no-install-recommends build-essential \
        postgresql-client \
        netcat \
        binutils \
        libjpeg-dev \
        libpq-dev \
        zlib1g-dev \
        curl

# user
RUN groupadd -r user --gid=$DOCKER_USER && \
    useradd -r -g user -d /user/ --uid=$DOCKER_USER -s /sbin/nologin -c "Docker image user" user

# copy scripts
COPY --chown=user:user scripts /user/scripts
RUN chmod ug+x /user/scripts/*

# install requirements
COPY --chown=user:user requirements /user/requirements
RUN /user/scripts/install-requirements.sh $MODE user

# copy code
COPY --chown=user:user app /user/app

USER user

WORKDIR /user/app
