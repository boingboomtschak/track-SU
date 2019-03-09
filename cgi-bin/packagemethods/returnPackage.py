#!/usr/bin/python
import cgi
import enable cgitb
import json
import os

def main():
    
    form = cgi.FieldStorage()

    with open(os.path.join(os.pardir, "data", "packages.json")) as json_file:
            data = json.load(json_file)
    
    print(data)
    
if __name__ == "__main__":
    main()