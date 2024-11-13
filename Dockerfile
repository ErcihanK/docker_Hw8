FROM python:3.9-slim

WORKDIR /app

COPY app.py .
COPY test.py .

# Run tests during build
RUN python -m unittest test.py

# Default command when container runs
CMD ["python", "app.py"]