FROM python:3.7
LABEL maintainer="Suriyaprakash suriya4code@gmail.com"
WORKDIR /github-stats
# RUN apt-get install -y python3-pip python-dev build-essential
ENV FLASK_APP=main.py
ENV FLASK_ENV = production
ENV FLASK_RUN_HOST=0.0.0.0
# RUN apk add --no-cache gcc musl-dev linux-headers
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5000
COPY . .
CMD ["python", "main.py"]
