FROM python:3.4-alpine
ADD . /code
RUN pip install -r /code/requirements.txt
CMD ["python", "/code/APIServer.py"]