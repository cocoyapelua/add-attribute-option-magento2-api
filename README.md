To use the script you will need the Magento url and the api authentication code.

  1. Rename the .env.example to .env and fill the variables with the url and the auth.
  2. In ATTRIBUTE_CODE put the attribute code from Magento
  3. Inside the files folder you leave the csv with the value and label column, and put the path in PATH_FILE on env file
  4. Execute from the console
  
If everything is ok, the response should be true, otherwise, there may be an authentication error or with the attribute code.

[]: # Language: python
[]: # Path: main.py
