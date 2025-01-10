# Use the official selenium/standalone-chrome image as the base
FROM selenium/standalone-chrome:latest

# Install Python and pip
USER root
RUN apt-get update -y && apt-get install -y \
    python3 \
    python3-pip \
    && apt-get clean

# Set the working directory inside the container
WORKDIR /usr/src/app

# Copy the requirements.txt into the container
COPY . .

# Install Python dependencies from requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt


# Expose the Selenium WebDriver port
EXPOSE 4444

CMD ["python", "./spotify/main.py"]
