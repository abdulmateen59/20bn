FROM python:latest
RUN pip3 install -U pytest
COPY . /home/WORKSPACE
WORKDIR /home/WORKSPACE



# $ docker build -t twentybn . && docker run -it --rm twentybn /bin/bash
# $ python3 main.py
# $ pytest fitness/test_workout_history.py