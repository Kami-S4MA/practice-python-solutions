import json
from bokeh.plotting import figure, show

f = open("Bdays.json", "r")

Bdays = json.load(f)

monthNames = ["January", "Febuary", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
months = {}

for i in Bdays:

    if monthNames[int(Bdays[i][0:2])-1] not in months:
        months[monthNames[int(Bdays[i][0:2])-1]] = 1

    else:
        months[monthNames[int(Bdays[i][0:2])-1]] += 1

p = figure(
    x_range = list(months.keys()),
    title = "Scientists' Birthdays by Month",
    x_axis_label = "Month",
    y_axis_label = "Number of Birthdays",
    height = 400,
    width = 800
)

p.vbar(
    x = list(months.keys()),
    top = list(months.values()),
    width = 0.8
)

show(p)

