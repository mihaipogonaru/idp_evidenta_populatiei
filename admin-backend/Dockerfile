FROM python:3.7.3-alpine

RUN apk add --update mariadb-dev gcc libc-dev libffi-dev

COPY requirements.txt /usr/src/admin-backend/
RUN pip install --no-cache-dir -r /usr/src/admin-backend/requirements.txt

COPY app /usr/src/admin-backend/app

EXPOSE 8888
CMD python /usr/src/admin-backend/app/insert_test_counties.py\
  && python /usr/src/admin-backend/app/insert_test_data.py
