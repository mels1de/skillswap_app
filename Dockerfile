FROM python:3.12-slim AS builder

WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

FROM python:3.12-slim
WORKDIR /app

COPY --from=builder /usr/local /usr/local
COPY --from=builder /app /app

RUN addgroup --system appgroup && adduser --system appuser --ingroup appgroup
USER appuser

ENV PYTHONUNBUFFERED=1 PYTHONDONTWRITEBYTECODE=1

EXPOSE 8000

CMD alembic upgrade head && uvicorn app.main:app --host 0.0.0.0 --port 8000