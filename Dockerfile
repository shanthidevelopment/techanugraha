FROM python:3.10.2-slim-bullseye



# cd to directory /usr/src/app. this will be our working directory
WORKDIR /app

# copy the content of current directory in to the pwd of docker image.
# pwd in image is /app
COPY requirements.txt ./


# Install system dependencies required for mysqlclient and others
RUN apt-get update && apt-get install -y \
    gcc \
    default-libmysqlclient-dev \
    libssl-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*


# now run the command to install dependencies from requirements file
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
# expose the port 8800
EXPOSE 8000

# everytime container is started, run this command
