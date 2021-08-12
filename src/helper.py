"""
Author: Mani
Module containing methods to 
    1.get occurance 
    2.max occurance of characters
    3.get_most_popular
    4.get_longest_input

"""

def get_occurance(input: str):
    '''
        Checks for the Max occurance of a word in the given String.
        Also, avoids the space, punctuation from the input

        Args:
            input: str
        returns:
            occurance: dict
    '''
    occurance = {}
    if input:
        input = ''.join(e for e in input if e.isalnum())
        for i in input:
            occurance[i] = occurance.setdefault(i,0) + 1
        
    return occurance
    
def get_max_occurance(occurance: dict):
    '''
        Get the word with max occurance

        Args: 
            occurance: dict
        Returns:
            max_occurance: tuple
    '''
    max_word = []
    max_value = 0
    if occurance:

        max_value = max(occurance.values())
        for i in occurance:
            if occurance[i] == max_value:
                max_word.append(i)
    return max_word, max_value

def get_most_popular(data: dict):
    '''
        Gets the most popular world

        Args: 
            data: dict
        Returns:
            popular_word: list
    '''
    popular_word = []
    new_data = {i: data[i]['popularity'] for i in data }
    if new_data:
        popular_count = max(new_data.values())
        popular_word = [ i for i in new_data if new_data[i] == popular_count ]
    return popular_word

def get_longest_input(data: dict):
    '''
        Gets the longest input

        Args: 
            data: dict
        Returns:
            longest_input: list
    '''
    longest_input = []
    new_data = {i: data[i]['length'] for i in data }
    if new_data:
        longest_input_length = max(new_data.values())
        longest_input = [ i for i in new_data if new_data[i] == longest_input_length ]
    return longest_input

def get_longest_palindrome(data: dict):
    '''
        Gets the longest palindrome

        Args: 
            data: dict
        Returns:
            longest_palindrome: list
    '''
    longest_palindrome = []
    new_data = {i: len(i) for i in data if i == i[::-1] }
    if new_data:
        longest_palindrome_length = max(new_data.values())
        longest_palindrome = [ i for i in new_data if new_data[i] == longest_palindrome_length ]
    return longest_palindrome

    

        

