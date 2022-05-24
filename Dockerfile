FROM python:latest

ADD . /home/model-server/

WORKDIR /home/model-server/

RUN apt-get update && apt-get install -y python3-opencv

RUN pip3 install --upgrade pip

RUN pip3 install opencv-python

RUN git clone https://github.com/pytorch/fairseq.git

RUN pip install ./fairseq/

RUN cd /home/model-server/OFA

RUN sed '1d' ./OFA/requirements.txt | xargs -I {} pip install {}

RUN pip3 install -r requirements.txt

CMD exec gunicorn -b :5000 --graceful-timeout 300 -t 600 app:app

EXPOSE 5000
