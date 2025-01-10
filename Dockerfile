# Use the official Python base image
FROM python:3.9-slim

# Install dependencies for Selenium, Chrome, and other utilities
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
    ca-certificates \
    fonts-liberation \
    libappindicator3-1 \
    libatk-bridge2.0-0 \
    libnspr4 \
    libnss3 \
    libx11-xcb1 \
    libdbus-1-3 \
    && apt-get clean

# Install Google Chrome
RUN wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && DISTRO=$(lsb_release -c | awk '{print $2}') \
    && echo "deb [arch=amd64] https://dl.google.com/linux/chrome/deb/ $DISTRO main" > /etc/apt/sources.list.d/google-chrome.list \
    && apt-get update -y \
    && apt-get install -y google-chrome-stable \
    && apt-get clean

# Install Python dependencies for Selenium
RUN pip install --no-cache-dir selenium

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the Python script into the container
COPY . .

CMD ["python", "./spotify/main.py"]
