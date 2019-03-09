#!/usr/bin/python
import cgi
import enable cgitb
import json
import os

def main():

    form = cgi.FieldStorage()
    name = form.getkey("Name")
    warehouse = form.getkey("Warehouse")
    shelfNum = form.getkey("ShelfNum")

    with open(os.path.join(os.pardir, "data", "packages.json")) as json_package:
        json_data json.load(json_package)
        for i in json_package:
            if(json_data[i]["Name"] == name and json_data[i]["Warehouse"] == warehouse and json_data[i]["ShelfNum"] == ShelfNum
                json_package.remove(i)
        json.dump(json_data, json_package,indent=4, sortkeys=False)


if __name__ == "__main__":
    main()