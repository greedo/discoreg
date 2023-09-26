FROM python:3.8

ENV PYTHONUNBUFFERED 1

WORKDIR /discoreg
EXPOSE 80

COPY requirements.txt /discoreg
RUN pip3 install -r requirements.txt --no-cache-dir
COPY . /discoreg

ENTRYPOINT ["/discoreg/docker-entrypoint.sh"]
CMD ["sh"]
