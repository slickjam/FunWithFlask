FROM python:3

COPY *.py .

RUN pip install flask 

CMD [ "python", "simple_server.py" ]