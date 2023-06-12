FROM python:3.10.6

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /src

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . /src/

RUN chmod +x ./entrypoint.sh
ENTRYPOINT ["sh", "entrypoint.sh"]