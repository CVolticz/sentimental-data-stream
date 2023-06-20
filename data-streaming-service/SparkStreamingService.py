"""
    Start streaming service using Twitter API
    Open a listenting port on host machine to take in data
"""
# system level import
import os, sys
import socket   # network inteface

# library level import
from dotenv import load_dotenv

# class level import
from plugins.TweetsListener import TweetsListener

# load and set credentials using enviornmental files
load_dotenv()
consumer_key=os.getenv("CONSUMER_KEY")
consumer_secret=os.getenv("CONSUMER_SECRET")
access_token=os.getenv("ACCESS_TOKEN")
access_secret=os.getenv("ACCESS_SECRET")


def sendData(c_socket, filters=['soccer']):
    """
        Function to handle the instantiation of the EventListener
        Also set up a streming service through twitter using our given authorization
    """
    twitter_stream = TweetsListener(
        consumer_key, consumer_secret,
        access_token, access_secret, 
        csocket=c_socket
    )
    twitter_stream.filter(track=filters, languages=["en"])


if __name__ == "__main__":

    # Open a Socket Listener Object on Server (Current Machine)
    # Reserve a port 5555 for listenting service; bind to host
    s = socket.socket() 
    host = "127.0.0.1"          
    port = 5555                 
    s.bind((host, port))
    print(f"Server Listening on Port: {port}")

    # Now wait for client connection.
    # Establish connection with client.
    # allows 5 unacepted connections before refusing
    s.listen(5)                 
    c, addr = s.accept() 
    print( "Received request from: " + str( addr ) )

    # parameterized single-world filter on tweet
    filters = ['ladies coats', 'men coats', 'sneakers', 'beddings', 'lifestyle']
    sendData( c, filters )