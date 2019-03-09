#!/usr/bin/env python3

import cgi
import enable cgitb
import json
import os

def main():
    validInput = False
    form = cgi.FieldStorage()
    name = form.getkey("Name")
    des = form.getkey("Description")
    shelfNum = form.getkey("ShelfNum")
    dateIn = form.getkey("Date In")
    package = {}
    package["Name"] = name
    package["Description"] = des
    package["Shelf Number"] = shelfNum
    package["Date In"] = dateIn
    with open(os.path.join(os.pardir, "data", "warehouses.json")) as json_warehouse:
        while not validInput: #validate input while the warehouse name does not match an existing name is warehouse list
            warehouse = form.getkey("Warehouse")
            for i in json_file:
                if warehouse == json_file[i]["Warehouse"]:
                    validInput = True
        with open(os.path.join(os.pardir, "data", "packages.json")) as json_package:
            #at this point it is appropriate to create the json file b/c data has been collected
            package["Warehouse"] = warehouse
            packagedata = json.load(package_data)
            packagedata.append(package)
            json.dump(packagedata,json_package,indent=4 sortkeys=False)  
            #package json close, increment warehouse data that pertains to packages before closing existing warehouse json  
        warehouse["Packages In"] += 1
        warehouse["Total Packages"] += 1
                                      
if __name__ == "__main__":
    main()