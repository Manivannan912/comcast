1. Have moved constants and variable that might be changed frequently to a constants file. 
This will provide better control in modifying the variables in a single place.
2. Have created a test folder for unit testing module. This will ensure if the functionality is 
still working after every change.
3. Have used doc string header across all the module and methods for better readability and understandability
4. Created a data store(Have used a temporary file, instead of DB) to persist the data. 
Even if the app is restarted the old or historical data is preserved. The string data will be loaded from data 
store if the app is restarted or seen_string is empty.
5. Have introduced input validation to take away the pain of deducting for empty input
6. Also, segregated the string manipulation function like finding the longest string, character which occured max in 
the string to a helper module for better readability and maintainability
7. Have implemented logging for tracing in case of error or required in case of root cause analysis.
