from tkinter import *
import requests
import json

root = Tk()
root.title("Air Quality...")
root.geometry('700x90')


def zip_lookup():
    try:
        api_request = requests.get(
            "https://www.airnowapi.org/aq/forecast/zipCode/?format=application/json&zipCode=" + zips.get() +
            "&distance=25&API_KEY=5E5DE48A-BD0D-4783-B03C-5F98D794AF48")
        api = json.loads(api_request.content)

        city = api[0]['ReportingArea']
        quality = api[0]['AQI']
        category = api[0]['Category']['Name']

        if category == "Good":
            weather_color = "#0C0"
        elif category == "Moderate":
            weather_color = "#FFFF00"
        elif category == "Unhealthy for Sensitive Groups":
            weather_color = "#ff9900"
        elif category == "Unhealthy":
            weather_color = "#FF0000"
        elif category == "Very Unhealthy":
            weather_color = "#990066"
        elif category == "Hazardous":
            weather_color = "#660000"

        root.configure(background=weather_color)
        my_label = Label(root, text=city + " Air Quality " + str(quality) + " " + category, font=("Helvetica", 20)
                         , background=weather_color)
        my_label.grid(row=1, column=0, columnspan=2)

    except requests.ConnectionError:
        api = 'Error...'


zips = Entry(root)
zips.grid(row=0, column=0, stick=W + E + N + S)

zip_button = Button(root, text="Lookup Zip", command=zip_lookup)
zip_button.grid(row=0, column=1, stick=W + E + N + S)

root.mainloop()
