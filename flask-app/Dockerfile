FROM python:3.10 AS build

WORKDIR /app

COPY requirements.txt .
COPY app.py .

RUN pip install --user -r requirements.txt

# Stage 2
FROM python:3.10-slim

WORKDIR /app

COPY --from=build /root/.local /root/.local
COPY --from=build /app /app

ENV PATH=/root/.local/bin:$PATH

EXPOSE 9000

CMD [ "gunicorn", "app:app", "--bind", "0.0.0.0:9000" ]