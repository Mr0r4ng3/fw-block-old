#!/usr/bin/env bash

set -o errexit
set -o nounset
set -o pipefail

# We are using `gunicorn` for production, see:
# http://docs.gunicorn.org/en/stable/configure.html

# Run python specific scripts:
# Running migrations in startup script might not be the best option, see:
# docs/pages/template/production-checklist.rst
python /code/manage.py migrate --noinput

# Start gunicorn:
# Docs: http://docs.gunicorn.org/en/stable/settings.html
# Make sure it is in sync with `django/ci.sh` check:
/usr/local/bin/gunicorn \
  --config python:docker.django.gunicorn_config \
  fw_block.wsgi