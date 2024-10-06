import re

def clean():
    with open("log.txt", 'r') as file:
        msg= file.read()

    msg = msg.replace(' ', '') # removing unncessary spaces
    msg = re.sub(re.compile(r"<key.space:' '>"), ' ', msg) # replacing space by ' '
    regex_key = re.compile(r'(<key\..*?)(?:\'| |\d|\"|key.esc|\s)>(>?)') # gathering  all special keys
    msg = re.sub(regex_key, '',msg) # replacing all special keys with empty string
    msg = msg.replace('\'', '') # replacing the quote with empty string
    msg = msg.replace(',', '') # replacing the comma with empty string
    print(msg)