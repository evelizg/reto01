# set base image (host OS)
FROM python:3.8

# set the working directory in the container
WORKDIR /code

# copy the dependencies file to the working directory

COPY requirements.txt .
COPY requirements2.txt .
COPY requirements3.txt .
  
    

# install dependencies

RUN pip install -r requirements.txt
RUN pip install -r requirements2.txt
RUN pip install -r requirements3.txt



# copy the content of the local src directory to the working directory
COPY src/ .

# command to run on container start
CMD [ "uvicorn", "server3:app", "--host", "0.0.0.0", "--reload", "--port", "5000" ]

HEALTHCHECK --interval=600s --timeout=3s \
CMD curl -f http://localhost:5000/retoibm/sumar/10/20/ || exit 1
