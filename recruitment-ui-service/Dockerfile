FROM python:3.6
LABEL maintainer="Aishwary <aishwaryt@vmware.com>"

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app
EXPOSE 5006
ENTRYPOINT [ "python" ]

CMD [ "main.py" ]