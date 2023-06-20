# Design a new container with pyspark ready
FROM jupyter/pyspark-notebook:latest

# upgrade pip
RUN pip install --upgrade pip

# install python specific packages
COPY requirements.txt .
RUN pip install --user -r requirements.txt

# add script execution when launch
# CMD [ "python", "script.py" ]

# add entry point to script such that docker run image can take in extra parameters
ENTRYPOINT [ "python" ]

# Rudimentary CLI Start
# docker container run -it --rm -v $(pwd)/data-streaming-service:/home/jovyan/work -p 8888:8888 --env-file 
# .env data-stream-service jupyter-notebook jupyter/pyspark-notebook

# docker container exec -it <container_name> bash