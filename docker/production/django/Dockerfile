FROM ghcr.io/astral-sh/uv:0.6.0 AS uv
FROM docker.io/python:3.13-slim-bookworm AS python

ARG BUILD_ENVIRONMENT=local

ENV BUILD_ENV=${BUILD_ENVIRONMENT}
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

ENV PATH="/opt/venv/bin:$PATH"

WORKDIR /app

#-----------------------------------------------------------------------------------------------------------------------
# Python build stage
#-----------------------------------------------------------------------------------------------------------------------
FROM python AS python-build

ENV UV_CACHE_DIR=/opt/uv-cache/
ENV UV_COMPILE_BYTECODE=1
ENV UV_LINK_MODE=copy
ENV VIRTUAL_ENV=/opt/venv

RUN --mount=from=uv,source=/uv,target=/bin/uv \
  --mount=type=cache,target=/opt/uv-cache/ \
  --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
  --mount=type=bind,source=uv.lock,target=uv.lock \
  uv sync --active --frozen --no-dev --no-default-groups

#-----------------------------------------------------------------------------------------------------------------------
# Django build stage
#-----------------------------------------------------------------------------------------------------------------------
FROM python AS django-image

# Create app user
RUN groupadd --system app \
  && useradd --gid app --shell /bin/bash --home-dir /app app

COPY --from=python-build --chown=app:app /opt/venv /opt/venv

COPY --chown=app:app ./docker/production/django/entrypoint /entrypoint
RUN sed -i 's/\r$//g' /entrypoint
RUN chmod +x /entrypoint

COPY ./docker/production/django/start /start
RUN sed -i 's/\r$//g' /start && \
  chmod +x /start

COPY --chown=app:app . /app
RUN chown -R app:app /app
RUN rm -rf /app/docker && \
  rm -rf /app/.dockerignore && \
  rm -rf /app/pyproject.toml && \
  rm -rf /app/uv.lock

USER app

ENTRYPOINT ["/entrypoint"]
