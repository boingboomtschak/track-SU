#!/usr/bin/env python3
import cgi, enable_cgitb, json, os, sys
from tracklib import getArgs

def main():
    args = getArgs(sys.argv)
    if "-name" in args.keys():
        name = args["-name"]
    else:
        name = input("Warehouse name: ")
    if "-address" in args.keys():
        address = args["-address"]
    else:
        address = input("Warehouse address: ")
    warehouse = {}
    warehouse["Name"] = name
    warehouse["Address"] = address
    warehouse["Total Packages"] = 0
    warehouse["Packages In"] = 0
    warehouse["Packages Out"] = 0
    warehouse["Errors"] = 0
    with open(os.path.join(os.pardir, 'data', 'warehouses.json'), 'w+') as json_file:
        try:
            json_data = json.load(json_file)
        except json.decoder.JSONDecodeError:
            json_data = []
        json_data.append(warehouse)
        json.dump(json_data, json_file, indent=4)
    print("Warehouse added to 'warehouses.json' successfully!")


if __name__ == "__main__":
    main()