# Sentimental Data Streaming Service
Leveraging Apache Spark to set up a context manager to initialize an automatic data read from a given socket. The twitter APi issue a job to Twitter's frontend to stream real-time tweets to the specified socket for Spark to ingest. The resulting data is then used in a sentimental analysis engine and display on a dashboard.

## Requirements
- Docker
- WSL/Unix system

## File Anatomy
- dashboard: under construction!
- data-streaming-service:\
    1. data: some stream data are stored in in parquet format to be use in model tranining\
    2. plugins: contains the event listener for twitte APi\
- SparkStreamingService: 
    1. Initialize Event Listener, open the socket, and have twitter APi sent the data to the socket


## Installation
1. cd data-streaming-service
2. docker build -t <image_name> .

## Rudimentary CLI Start
1. docker container run -it --rm -v $(pwd)/data-streaming-service:/home/jovyan/work -p 8888:8888 --env-file .env data-stream-service jupyter-notebook
2. docker container exec -it <container_name> bash

## Docker container start
1. cd /docker/clusters/<cluster_name>
2. docker-compose up -d
3. docker-compose exec anaconda jupyter notebook --notebook-dir=/workspace --ip='*' --port=8888 --no-browser --allow-root

## Docker container termination (remember to execute this command after finish)
1. cd /docker/clusters/<cluster_name>
2. docker-compose down


## Roadmap
Leverage Apache Kafka along with Apache Spark to build out a different streaming service for text


## Contributing
To contribute, create your own branch, develop, test and make a pull request to develop branch. 


## Authors and acknowledgment
Ken Trinh

## License
MIT License


