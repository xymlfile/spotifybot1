# Use the official Python base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the requirements.txt file into the container
COPY requirements.txt .

# Install pip (if it's not already installed) and dependencies from requirements.txt
RUN python -m ensurepip --upgrade && \
    pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application into the container
COPY . .

# Run the Python script
CMD ["python", "./spotify/main.py"]
