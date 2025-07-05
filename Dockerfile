FROM python:3.12-slim AS builder

WORKDIR /app

COPY requierments.txt /app/requierments.txt
RUN pip install --no-cache-dir -r requierments.txt

COPY . /app

FROM python:3.12-slim
WORKDIR /app

COPY --from=builder /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages
COPY --from=builder /app /app

RUN addgroup --system appgroup && adduser --system appuser --ingroup appgroup
USER appuser

ENV PYTHONUNBUFFERED=1 PYTHONDONTWRITEBYTECODE=1

EXPOSE 8000

CMD alembic upgrade head && uvicorn app.main:app --host 0.0.0.0 --port 8000