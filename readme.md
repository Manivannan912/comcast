# Stringinate

# Table of  Contents

- [Overview](#Overview)
    - [root](#root)
    - [stringinate](#stringinate)
    - [stats](#stats)
- [Unit Testing](#Unittesting)

<a name="Overview"></a>

# Overview

The application supports a set of API endpoints that can be used to get information about and manipulate string values. 
The application also tracks statistics about all the strings that have been sent to the server

<a name="root"></a>

## API: /

* The root of the server displays info about the other endpoints. 

<a name="stringinate"></a>

## API: /stringinate

* Get all the info you've ever wanted about a string. Accepts GET and POST requests.
For input "this is the input". The ouput will be
```
{
  "frequent character": [
    "t",
    "i"
  ],
  "frequent character occurance": 3,
  "input": "this is the input",
  "length": 17
}
```

<a name="stats"></a>

## API: /stats

* Get statistics about all strings the server has seen, including the number of times each input has 
been received along with the longest and most popular strings, longest palindrome strings.
The response of the endpoint will be
```
{
  "longest input received": [
    "this is the input"
  ],
  "longest palindrome": [
    "madam"
  ],
  "most popular": [
    "this is the input"
  ]
}
```

<a name="unittesting"></a>

## Unit Testing

This software includes the unit testing package which can be run using `python run_test.py`

```
$ python run_test.py 
.....
----------------------------------------------------------------------
Ran 6 tests in 0.001s

OK
```
