FROM python:alpine3.7
RUN mkdir /app
WORKDIR /app/
COPY . /app
RUN pip install -r requirements.txt
EXPOSE 5000
ENV FLASK_APP=hello
ENTRYPOINT [ "python" ]
CMD [ "hello.py" ]