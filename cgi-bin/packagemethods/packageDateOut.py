import cgi
import enable cgitb
import json
import os

def main():

    form = cgi.FieldStorage()
    dateOut = form.getkey("Date Out")
    Name = form.getkey("Name")
    shelfNum = form.get("ShelfNum")

    with open(os.path.join(os.pardir, "data", "warehouses.json")) as json_file:
        json_data = json.load(json_file)
        for i in json_file:
            if json_data[i]["Name"] == name and json_data[i]["ShelfNum"] == shelfNum
                package[i]["Date Out"] = dateOut


if __name__ == "__main__":
    main()