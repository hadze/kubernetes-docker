# base image
FROM alpine:3.5

# Install python and pip and upgrade pip
RUN apk add --update py3-pip
RUN pip install --upgrade pip

# install Python modules needed for the example
COPY requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r /usr/src/app/requirements.txt

# copy files required for the app to run
COPY app.py /usr/src/app/
COPY templates/index.html /usr/src/app/templates/

# expose the port number within the container
EXPOSE 5000

# run the application
CMD ["python", "/usr/src/app/app.py"]