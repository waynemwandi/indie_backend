# Use the full Python image version 3.11.7
FROM python:3.11.7

# Set the working directory in the container
WORKDIR /app

# Install MySQL development libraries (prerequisite for mysqlclient)
RUN apt-get update && apt-get install -y \
    default-libmysqlclient-dev \
    --no-install-recommends && rm -rf /var/lib/apt/lists/*

# Copy the requirements file into the container at /app
COPY ./requirements.txt /app/requirements.txt

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . /app

# Expose port 8000
EXPOSE 8000


