import cgi
import enable cgitb
import json
import os

def main():
    verified = False
    form = cgi.FieldStorage()
    errDes = form.getkey("Error Description")
    reportedBy = form.getkey("Employee Name")
    empID = form.getkey("Employee ID"]
    err {}
    err["Error Description"] = errDes
    err["Employee Name"] = reportedBy
    err["Employee ID"] = empID
    err["Confirmation"] = True
    with open(os.path.join(os.pardir, "data", "errors.json")) as json_errors:
        jsondata = json.load(json_errors)
        jsondata.append(err)
        json.dump(jsondata,json_errors, indent=4, sort_keys=False)




if __name__ == "__main__":
    main()