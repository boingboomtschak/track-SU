#!/usr/bin/python3.7m
import cgi
import enable_cgitb
import json
import os

def main():
    form = cgi.FieldStorage()
    name = form.getkey("Name")
    address = form.getkey("Address")
    warehouse = {}
    warehouse["Name"] = name
    warehouse["Address"] = address
    warehouse["Total Packages"] = 0
    warehouse["Packages In"] = 0
    warehouse["Packages Out"] = 0
    warehouse["Errors"] = 0
    with open(os.path.join(os.pardir, "data", "warehouses.json")) as json_file:
        jsondata = json.load(json_file)
        jsondata.append(warehouse)
        json.dump(jsondata, json_file, indent=4 sort_keys=False)
    

if __name__ == "__main__":
    main()