FROM python:3.7.3-alpine

# RUN apk add --update mariadb-dev gcc libc-dev libffi-dev

COPY requirements.txt /usr/src/admin/
RUN pip install --no-cache-dir -r /usr/src/admin/requirements.txt

COPY insert_test_counties.py /usr/src/admin/
COPY insert_test_data.py /usr/src/admin/

COPY app /usr/src/admin/app
COPY start.py /usr/src/admin/

EXPOSE 9900
CMD ["python", "/usr/src/admin/start.py"]
