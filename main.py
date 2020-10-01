import tkinter as tk
import requests
from PIL import ImageTk, Image

HEIGHT = 1000
WIDTH = 1000



def get_weather(city):
    weather_key = ''
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {'APPID': weather_key, 'q': city, 'units': 'imperial'}
    response = requests.get(url, params=params)
    print(response.json())
    weather = response.json()

    label4['text'] = format_response(weather)
    label['text'] = format_response1(weather)

def format_response(weather):
    try:
        temp = weather['main']['temp']

        final_str = ' %s °F' % temp

    except:
        final_str = ''

    return final_str


def format_response1(weather):
    try:
        name = weather['name']
        desc = weather['weather'][0]['description']
        feels_like = weather['main']['feels_like']
        humidity = weather['main']['humidity']

        final_str1 = '%s TODAY: \n\n Conditions: %s\n Feels Like: %s\n Humidity: %s' % (name, desc, feels_like, humidity)

    except:
        final_str1 = 'Invalid Entry. Please Try Again.'

    return final_str


root = tk.Tk()
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

background_image = ImageTk.PhotoImage(Image.open('background.jpg'))
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root)
frame.place(relx=0.5, rely=0.3, relwidth=0.75, relheight=0.1, anchor='n')

upper_frame = tk.Frame(root, bg='#96CDCD', bd=3)
upper_frame.place(relx=0.5, rely=0.05, relwidth=0.45, relheight=0.15, anchor='n')

label1 = tk.Label(upper_frame, bg='#E0EEEE', font=('Arial', 45))
label1.place(relwidth=1, relheight=1)

label1['text'] = "Better Weather"

labelframe = tk.LabelFrame(root, text="This is a LabelFrame")
labelframe.pack(fill="both", expand="yes")

entry = tk.Entry(frame, font=('Arial', 30))
entry.place(relwidth=0.7, relheight=1)
placeholder_text = 'Houston'
entry.insert(0, placeholder_text)

button = tk.Button(frame, text="SEARCH", bg='#80c1ff', font=50, command=lambda: get_weather(entry.get()))
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)

lower_frame = tk.Frame(root)
lower_frame.place(relx=0.3, rely=0.5, relwidth=0.4, relheight=0.3, anchor='n')

label = tk.Label(lower_frame, font=('Arial', 20))
label.place(relwidth=1, relheight=1)

lowest_frame = tk.Frame(root, bg='navy', bd=5)
lowest_frame.place(relx=0.7, rely=0.5, relwidth=0.4, relheight=0.3, anchor='n')

label4 = tk.Label(lowest_frame, font=('Arial', 60))
label4.place(relwidth=1, relheight=1)

root.mainloop()
