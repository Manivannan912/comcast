"""
Module to store  the string data and retrive the data
"""

import os
import json
import logging
from support import constants

log = logging.getLogger()

def data_loader(data: dict):
    '''
        Updates the old data
    '''
    try:
        path = constants.FILE_PATH
        log.info("Trying to preserve data")
        with open(path,'w') as f:
            json.dump(data,f)
        log.info("Data preserved successfully")

    except Exception as e:
        log.error(f"Preserving the data failed, due to {str(e)}")
    


def data_retriever():
    '''
        Retrives the old data on restart
    '''
    try:

        data = {}
        path = constants.FILE_PATH
        if os.path.exists(path):

            log.info("Trying to restore data")
            with open(path,'r') as f:
                data = json.load(f)  
            log.info("Data restored successfully")
        
        return data

    except Exception as e:

        log.error(f"Preserving the data failed, due to {str(e)}")
        return {}




