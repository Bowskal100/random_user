FROM ubuntu:18.04

LABEL Owner="Sam Shobowale" email="samboske93@gmail.com"

RUN apt-get update -y && \
    apt-get install -y python3-pip python-dev

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip3 install -r requirements.txt password='ilmwies'

COPY . /app

ENTRYPOINT [ "python3" ]

CMD [ "random_user.py" ]

EXPOSE 5000/tcp