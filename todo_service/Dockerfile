FROM python:3.10.6

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /src

COPY Pipfile Pipfile.lock ./

RUN pip install -U pipenv

RUN pipenv install --system

COPY . /src/

RUN chmod +x ./entrypoint.sh
ENTRYPOINT ["sh", "entrypoint.sh"]