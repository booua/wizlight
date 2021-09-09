FROM continuumio/miniconda3:latest


RUN conda config --add channels conda-forge && \
    conda create -y -n flask python=3 flask=0.12 uwsgi
COPY requirements.txt /tmp/requirements.txt
RUN conda install -n flask --file /tmp/requirements.txt

# Create a flask user to avoid running uwsgi as root
RUN useradd -r flask

COPY server.py /app/server.py
RUN chown -R flask /app

USER flask

# activate the flask environment
ENV PATH /opt/conda/envs/flask/bin:$PATH
WORKDIR /app

EXPOSE 5005

CMD ["uwsgi", "--http-socket", "0.0.0.0:5005", "--wsgi-file", "server.py", "--callable", "app"]



# FROM python:3
# ADD . /wizlight
# WORKDIR /wizlight
# RUN pip3 install --no-cache-dir -r requirements.txt
# RUN pip3 install uwsgi

# CMD python3 server.py