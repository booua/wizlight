FROM python:3
ADD . /wizlight
WORKDIR /wizlight
RUN pip3 install --no-cache-dir -r requirements.txt

CMD python3 server.py