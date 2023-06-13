# system level import
import json
import logging

# library level import
from tweepy import Stream

class TweetsListener(Stream):
    """
        Class constructor to isntantiate a tweet listener object with a cscocket
    """
    def __init__(self, *args, csocket):
        super().__init__(*args)
        self.client_socket = csocket
        self.__logger = self.__init_logger()


    def __init_logger(self):
        """
            Initialize logging mechanism for debugging
        """    
        return logging.getLogger(self.__class__.__name__)


    def on_data(self, data):
        """
            Load data streamed from source
        """
        try:
            self.__logger.debug('Attempting to load data')
            msg = json.loads( data )
                    
            # if tweet is longer than 140 characters
            if "extended_tweet" in msg:
                # add at the end of each tweet "t_end" 
                self.client_socket\
                    .send(str(msg['extended_tweet']['full_text']+"t_end")\
                    .encode('utf-8'))         
                self.__logger.debug(f"System Loaded with Message: { str(msg['extended_tweet']['full_text']+'t_end').encode('utf-8') }")    
            else:
                # add at the end of each tweet "t_end" 
                self.client_socket \
                    .send(str(msg['text']+"t_end") \
                    .encode('utf-8'))
                self.__logger.debug(f"System Loaded with Message: { str(msg['text']+'t_end').encode('utf-8') }")    
            return True
        except BaseException as e:
            self.__logger.error("Error on_data: %s" % str(e), exc_info=True)
        return True


    def on_error(self, status):
        self.__logger.error(status, exc_info=True)
        return True

