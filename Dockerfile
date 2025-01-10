# Use the official Python base image
FROM python:3.9-slim

# Install dependencies for Selenium and Chrome
RUN apt-get update -y && apt-get install -y \
    wget \
    curl \
    unzip \
    gnupg2 \
    lsb-release \
    libappindicator3-1 \
    libasound2 \
    libatk1.0-0 \
    libatk-bridge2.0-0 \
    libcups2 \
    libx11-xcb1 \
    libdbus-1-3 \
    libgdk-pixbuf2.0-0 \
    libnspr4 \
    libnss3 \
    libx11-6 \
    xdg-utils \
    && apt-get clean

# Install Chrome (latest stable version)
RUN GOOGLE_CHROME_RPM=https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb \
    && wget $GOOGLE_CHROME_RPM -O /tmp/google-chrome.deb \
    && dpkg -i /tmp/google-chrome.deb \
    && apt-get install -f -y

# Install Python dependencies for Selenium
RUN pip install --no-cache-dir selenium

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the Python script into the container
COPY . .

# Command to run when the container starts
CMD ["python", "./spotify/main.py"]
