FROM python:3.8-slim-buster
WORKDIR /app

# Update package lists and install git
RUN apt-get update && apt-get -y install git

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD python3 main.py
