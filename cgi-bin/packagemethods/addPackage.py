#!/usr/bin/python
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
    package {}
    package["Name"] = name
    package["Description"] = des
    package["ShelfNum"] = shelfNum
    package["Date In"] = dateIn
    with open(os.path.join(os.pardir, "data", "warehouses.json")) as json_warehouse:
        with open(os.path.join(os.pardir, "data", "packages.json")) as json_package:
        #gets warehouse name and checks if this warehouse exists     
            while not validInput
                warehouse = form.getkey("Warehouse")
                    for i in json_file:
                        if warehouse == json_file[i]["Warehouse"]
                            package["Warehouse"] = warehouse
                            packagedata = json.load(package_data)
                            packagedata.append(package)
                            warehouse["Packages In"] += 1
                            warehouse["Total Packages"] += 1
                            json.dump(packagedata,json_package,indent=4 sortkeys=False)
                            validInput = True

if __name__ == "__main__":
    main()