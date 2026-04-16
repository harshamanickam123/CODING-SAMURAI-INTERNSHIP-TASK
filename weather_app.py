import tkinter as tk
import requests

API_KEY = "a7daf04612525243678d6c5c0f7c98d7"

def get_weather():
    city = entry.get()

    result_label.config(text="Loading...")
    root.update()

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()

    if data.get("cod") == 200:
        temp = data["main"]["temp"]
        desc = data["weather"][0]["description"]
        result_label.config(text=f"{temp}°C\n{desc.title()}")
    else:
        result_label.config(text="City not found ❌")


# WINDOW
root = tk.Tk()
root.title("Weather App")
root.geometry("400x350")
root.configure(bg="#1e272e")

# CARD FRAME (center container)
card = tk.Frame(root, bg="#2f3640", bd=0)
card.place(relx=0.5, rely=0.5, anchor="center", width=320, height=280)

# TITLE
title = tk.Label(
    card,
    text="Weather App",
    font=("Segoe UI", 18, "bold"),
    bg="#2f3640",
    fg="white"
)
title.pack(pady=(20, 10))

# ENTRY
entry = tk.Entry(
    card,
    font=("Segoe UI", 12),
    bd=0,
    justify="center"
)
entry.pack(pady=10, ipadx=10, ipady=5)

# BUTTON
button = tk.Button(
    card,
    text="Get Weather",
    font=("Segoe UI", 10, "bold"),
    bg="#00a8ff",
    fg="white",
    activebackground="#0097e6",
    relief="flat",
    command=get_weather
)
button.pack(pady=10, ipadx=10, ipady=5)

# RESULT
result_label = tk.Label(
    card,
    text="",
    font=("Segoe UI", 14),
    bg="#2f3640",
    fg="white",
    justify="center"
)
result_label.pack(pady=20)

root.mainloop()