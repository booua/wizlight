FROM python:3
ADD . /wizlight
WORKDIR /wizlight
RUN pip3 install --no-cache-dir -r requirements.txt
EXPOSE 5002 38899/udp

CMD python3 server.py