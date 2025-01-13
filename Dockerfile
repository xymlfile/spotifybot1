# Use the official selenium/standalone-chrome image as the base
FROM selenium/standalone-chrome:latest

# Switch to root to install dependencies
USER root

# Update and install dependencies in separate steps to identify issues more clearly
RUN apt-get update -y && apt-get install -y \
    python3 python3-pip python3-venv && apt-get clean

RUN apt-get update -y && apt-get install -y \
    curl wget unzip ca-certificates fonts-liberation \
    libappindicator3-1 libnss3 libxss1 libgbm-dev \
    libasound2 libatk-bridge2.0-0 libatk1.0-0 \
    libgdk-pixbuf2.0-0 libgtk-3-0 xdg-utils xvfb && apt-get clean

# Install Google Chrome (latest version)
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb \
    && dpkg -i google-chrome-stable_current_amd64.deb \
    && apt-get -f install -y

# Install ChromeDriver (ensure it matches the version of Chrome installed)
RUN LATEST_VERSION=$(curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE) && \
    wget https://chromedriver.storage.googleapis.com/$LATEST_VERSION/chromedriver_linux64.zip && \
    unzip chromedriver_linux64.zip && \
    mv chromedriver /usr/local/bin/ && \
    rm chromedriver_linux64.zip

# Install Selenium via pip
RUN pip install selenium

# Install 'wait-for-it' script to wait for Selenium WebDriver to be ready
RUN curl -o /usr/local/bin/wait-for-it https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh \
    && chmod +x /usr/local/bin/wait-for-it

# Set the working directory inside the container
WORKDIR /usr/src/app

# Copy the application files (requirements.txt, script, etc.) into the container
COPY . .

# Create a virtual environment for Python
RUN python3 -m venv /usr/src/app/venv

# Install Python dependencies from requirements.txt
RUN /usr/src/app/venv/bin/pip install --no-cache-dir -r requirements.txt

# Set the display environment variable for headless Chrome mode
ENV DISPLAY=:99

# Expose the Selenium WebDriver port
EXPOSE 4444

# Command to start the application, ensuring WebDriver is available before running the script
CMD /usr/src/app/venv/bin/python ./spotify/main.py
