# 1. Base Image: Use a lightweight version of Python
FROM python:3.10-slim

# 2. Set the working directory inside the container
WORKDIR /app

# 3. Copy just the requirements first (uses Docker cache efficiently)
COPY requirements.txt .

# 4. Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy your application code into the container
COPY app/ ./app/

# 6. Expose the port the app runs on
EXPOSE 8000

# 7. Start the application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
