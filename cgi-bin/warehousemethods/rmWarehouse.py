#!/usr/bin/python
import cgi
import enable cgitb
import json
import os

def main():
    form = cgi.FieldStorage()
    name = form.getkey("Name")
    with open(os.path.join(os.pardir, "data", "warehouses.json")) as json_file:
        json_data = json.load(json_file)
        for i in json_data:
            if json_data[i]["Name"] == name
                json_data.remove(i)
        json.dump(json_data,json_file,indent=4 sortkeys=False)

if __name__ == "__main__":
    main()