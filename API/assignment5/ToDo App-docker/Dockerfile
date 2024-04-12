
FROM python AS base

RUN  apt-get --assume-yes update
RUN  apt-get install --assume-yes sqlite3 libsqlite3-dev


FROM base 
WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY ./app /code/app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]