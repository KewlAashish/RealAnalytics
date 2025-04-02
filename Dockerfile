FROM python:3.11-slim

# Install netcat (for wait script)
RUN apt-get update && apt-get install -y netcat-openbsd

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY . .

# Install dependencies
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Copy wait script
COPY wait-for-postgres.sh /wait-for-postgres.sh
RUN chmod +x /wait-for-postgres.sh

EXPOSE 5000

# Wait for Postgres, then run app
CMD ["/wait-for-postgres.sh", "python", "run.py"]
