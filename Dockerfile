# Use the official selenium/standalone-chrome image as the base
FROM selenium/standalone-chrome:latest

# Install Python and pip
USER root
RUN apt-get update -y && apt-get install -y \
    python3 \
    python3-pip \
    python3-venv \
    curl \
    && apt-get clean

RUN curl -o /usr/local/bin/wait-for-it https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh \
    && chmod +x /usr/local/bin/wait-for-it

# Set the working directory inside the container
WORKDIR /usr/src/app

# Copy the requirements.txt into the container
COPY . .

# Create a virtual environment for Python
RUN python3 -m venv /usr/src/app/venv

# Activate the virtual environment and install dependencies from requirements.txt
RUN /usr/src/app/venv/bin/pip install --no-cache-dir -r requirements.txt


# Expose the Selenium WebDriver port
EXPOSE 4444

# Command to run the Python script when the container starts
CMD ["/usr/src/app/venv/bin/python", "./spotify/main.py"]
