import json

data = json.load(open('newborns.json'))

def get_table_newborns(year):
    table_names = ["Name", "Year", "NumberOfPersons", "Month"]
    
    if year:
        newborns_to_show = [n for n in data if n["Cells"]["Year"]==year]
    else:
        newborns_to_show = data

    row_html = "<table border='1'><tr>"
    for i in table_names:
        row_html += "<th>%s</th>" % i
    row_html += "</tr>"
    for i in newborns_to_show:
        row_html += "<tr>"
        for t in table_names:
            row_html += "<td>%s</td>" % i["Cells"][t]
        row_html += "</tr>"
    row_html += "</table>"
    return row_html