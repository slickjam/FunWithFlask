FROM python:3

COPY *.py .

COPY templates/ templates/

RUN pip install flask 

CMD [ "python", "simple_server.py" ]