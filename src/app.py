from flask import Flask
from flask import request
import helper
import logging_definition
import logging
from model import data_store
from support import constants

log = logging.getLogger()
app = Flask(__name__)

seen_strings = {}

@app.route('/')
def root():
    '''
        API:
            /
        Index methid which will display about the various API endpoints the application has
        Returns:
            str
    '''

    log.info(" ")
    log.info("Displaying App information")
    log.info(" ")

    return constants.WELCOME_INFORMATION
    

@app.route('/stringinate', methods=['GET','POST'])
def stringinate():
    '''
        API: 
            /stringinate

        Method to parse and return the string with below details
            1. Length of the input string
            2. Character that is frequently repeated
            3. Max times the value has occured

        Returns:
        Dict
    '''
    global seen_strings

    if not seen_strings:
        seen_strings = data_store.data_retriever()

    #Input parsing
    input = ''
    if request.method == 'POST':
        input = request.json
        input = input.get('input','')
    else:
        input = request.args.get('input', '')
    log.info(f'Received String: {input}')

    #Input validation
    if input == '': return {'response':'Please send non empty data'}


    #String runbook
    if input in seen_strings:
        log.info(f"Updating the counter of: {input}")
        seen_strings[input]['popularity'] += 1
    else:
        log.info(f"Adding an entry in data_store for: {input}")
        seen_strings.update({input:{'popularity':1,'length':len(input)}})

        log.info("Process to get the max occurance started")
        occurance = helper.get_occurance(input)
        word,max_occurance = helper.get_max_occurance(occurance)

        seen_strings[input]['frequent character'] = word
        seen_strings[input]['frequent character occurance'] = max_occurance
        log.info("Process to get the max occurance Completed")

    #update the data_store
    data_store.data_loader(seen_strings)

    return {
        "input": input,
        "length": seen_strings.get(input,{}).get('length',0),
        "frequent character" :seen_strings.get(input,{}).get('frequent character',[]),
        "frequent character occurance": seen_strings.get(input,{}).get('frequent character occurance',0)
    }

@app.route('/stats')
def string_stats():
    '''
        API: 
            /stats
        Method that will return 
            1. Most populat word
            2. Longest input received
        returns:
            dict
    '''

    global seen_strings
    if not seen_strings:
        seen_strings = data_store.data_retriever()

    log.info("Process to find the Popular and longest word started")
    most_popular = helper.get_most_popular(seen_strings)
    longest_input = helper.get_longest_input(seen_strings)
    log.info("Process to find the Popular and longest word completed")
    
    return {
        "most popular": most_popular,
        "longest input received" : longest_input
    }