FROM python:3.12.5
  
ENV \
# python:
PYTHONFAULTHANDLER=1 \
PYTHONUNBUFFERED=1 \
PYTHONHASHSEED=random \
PYTHONDONTWRITEBYTECODE=1 \
# pip:
PIP_NO_CACHE_DIR=1 \
PIP_DISABLE_PIP_VERSION_CHECK=1 \
PIP_DEFAULT_TIMEOUT=100 \
PIP_ROOT_USER_ACTION=ignore \
# poetry:
POETRY_VERSION=1.8.3 \
POETRY_VIRTUALENVS_CREATE=false \
POETRY_CACHE_DIR='/var/cache/pypoetry' \
POETRY_HOME='/usr/local'

RUN apt-get update && apt-get upgrade -y \
  && apt-get install --no-install-recommends -y \
    bash \
    curl \
    build-essential \
    gettext \
    && curl -sSL 'https://install.python-poetry.org' | python - \
    && poetry --version \
    # Cleaning cache:
    && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
    && apt-get clean -y && rm -rf /var/lib/apt/lists/*

WORKDIR /code

COPY . /code

# Project initialization:
# hadolint ignore=SC2046
RUN --mount=type=cache,target="$POETRY_CACHE_DIR" \
  poetry run pip install pip \
  && poetry --version && poetry run pip --version \
  && poetry install \
    --no-interaction --no-ansi --sync --only main

ENTRYPOINT [ "bash", "./docker/django/gunicorn.sh" ]