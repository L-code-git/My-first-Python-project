
# from re import search
# import tkinter as tk
# from tkinter import messagebox
# from unicodedata import name
# from geopy.geocoders import Nominatim
# from timezonefinder import TimezoneFinder
# from datetime import datetime
# import pytz
# import requests
# from PIL import Image, ImageTk









# def get_weather():
#     city = search_box.get()
#     if not city:
#         messagebox.showerror("Erorr", "Please enter a city name!")
#         return
    
#     try:
#         geolocator =Nominatim(user_agent="my_weasther_app")
#         location = geolocator.geocode(city)
        
#         if location:
#             lat = location.latitude
#             lon = location.longitude
            
        
#         if location:
#             city_name = location.address.split(",")[0]
#             city_label.configure(text=city_name)
            
            
            
        
#             # city_label.config(text="City not found!", font="helvetcia")
            
#             tf = TimezoneFinder()
#             result = tf.timezone_at(lng=lon, lat=lat)
            
#             if result:
#                 local_time = datetime.now(pytz.timezone(result))
#                 current_time = local_time.strftime("%H %M")
                
#                 clock_label.config(text=current_time)
#                 time_label.config(text="LOCAL TIME")
            
            
            
            
#             # weather
#             api_key = "3a1c18f6690eaa70f1d47c93c0151ac7"
#             api = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}"
            
            
#             json_data = requests.get(api).json()
#             condition = json_data["weather"][0]["main"]
#             description = json_data["weather"][0]["description"]
#             temperature = int(json_data["main"]["temperature"]-273.15)
#             pressure = json_data["main"]["pressure"]
#             humidity = json_data["main"]["humidity"]
#             wind = json_data["wind"]["speed"]
            
#             temperature_label.config(text=f"{temperature}")
#             condition_label.config(text=f"{description} | FEELS LIKE {temperature} °")
#             description_label.config(text=description)
#             humidity_label.config(text=humidity)
#             pressure_label.config(text=pressure)
#             wind_label.config(text=wind)
            
            
            
#     except Exception as e:
#         messagebox.showerror("Error", f"An error occurred: {e}")
    
    


# root = tk.Tk()
# root.title("weather App")
# root.geometry("1080x800")
# root.resizable(False, False)



# def search():
#     city = search_box.get()
#     print(city)


# title = tk.Label(
#     root,
#     text = "Weather App",
#     font = ("Helvetica", 30, "bold"),
#     fg = "#1070C4"
#         )
# title.pack(pady=20)


# search_box = tk.Entry(
#     root,
#     justify="center",
#     font=("Arial", 15),
#     #fg = "#1070C4",
# )
# search_box.pack(pady=10)

# search_button = tk.Button(
#     root,
#     text="Search",
#     font=("Arial", 15, "bold"),
#     command=get_weather,
#     fg = "#1070C4",
#     # bg = "#1070C4"
# )
# search_button.pack(pady=10)

# #logo


# image = Image.open("image/PNG.webp")
# image = image.resize((200, 200))

# weather_logo = ImageTk.PhotoImage(image)

# logo_label = tk.Label(
#     root,
#     image=weather_logo,
#     bg="#f2f2f2"
# )
# logo_label.pack(pady=20) 








# weather_frame = tk.Frame(
#     root,
#     bg="#1070C4",
#     width=900,
#     height=80
# )
# weather_frame.pack(pady=10)    
# weather_frame.pack_propagate(False) 











# # wind_frame = tk.Frame(weather_frame, bg="#B48B11")
# # wind_frame.pack(side="left", expand=True, pady=(10, 0))

# wind_label = tk.Label(
#     weather_frame,
#     text="WIND",
#     font=("helvetica", 10, "bold"),
#     bg="#B48B11",
#     fg="white",

# )
# # wind_label.pack(side="left", expand=True, pady=(10, 0))
# wind_label.grid(row=0, column=0, padx=50, pady=(10, 5))


# wind_value_label = tk.Label(
#     weather_frame,
#     text=" ",
#     font=("helvetica", 10, "bold"),
#     bg="#B48B11",
#     fg="white",
# )
# # wind_value_label.pack(side="left", expand=True, pady=(10, 0))
# wind_value_label.grid(row=1, column=0, padx=50, pady=(5, 10))


# # humidity_frame = tk.Frame(weather_frame, bg="#B48B11")
# # humidity_frame.pack(side="left", expand=True, pady=(10, 0))


# humidity_label = tk.Label(
#     weather_frame,
#     text="HUMIDITY",
#     font=("helvetica", 10, "bold"),
#     bg="#B48B11",
#     fg="white",
# )
# # humidity_label.pack(side="left", expand=True, pady=(10, 0))
# humidity_label.grid(row=0, column=1, padx=50, pady=(10, 5))



# humidity_value_label = tk.Label(
#     weather_frame,
#     text=" ",
#     font=("helvetica", 10, "bold"),
#     bg="#B48B11",
#     fg="white",
# )
# # humidity_value_label.pack(side="left", expand=True, pady=(10, 0))
# humidity_value_label.grid(row=1, column=1, padx=50, pady=(5, 10))

# # description_value_label = tk.Frame(weather_frame, bg="#B48B11")
# # description_value_label.pack(side="left", expand=True, pady=(10, 20))

# description_label = tk.Label(
#     weather_frame,
#     text="DESCRIPTION",
#     font=("helvetica", 10, "bold"),
#     bg="#B48B11",
#     fg="white",             
# )
# # description_label.pack(side="left", expand=True, pady=(10, 0))
# description_label.grid(row=0, column=2, padx=50, pady=(10, 5))





# description_value_label = tk.Label(
#     weather_frame,
#     text=" ",
#     font=("helvetica", 10, "bold"),
#     bg="#B48B11",
#     fg="white",
# )
# # description_value_label.pack(side="left", expand=True, pady=(10, 0))
# description_value_label.grid(row=1, column=2, padx=50, pady=(5, 10))





# # pressure_value_label = tk.Frame(weather_frame, bg="#B48B11")
# # pressure_value_label.pack(side="left", expand=True, pady=(10, 20))

# pressure_label = tk.Label(
#     weather_frame,
#     text="PRESSURE",    
#     font=("helvetica", 10, "bold"),
#     bg="#B48B11",
#     fg="white",
# )
# # pressure_label.pack(side="left", expand=True, pady=(10, 5))
# pressure_label.grid(row=0, column=3, padx=50, pady=(10, 5))



# pressure_value_label = tk.Label(
#     weather_frame,
#     text=" ",
#     font=("helvetica", 10, "bold"),
#     bg="#B48B11",
#     fg="white",
# )
# # pressure_value_label.pack(side="left", expand=True, pady=(10, 0))
# pressure_value_label.grid(row=1, column=3, padx=50, pady=(5, 10))






# city_label = tk.Label(
#     root,
#     font=("helvetica", 25, "bold"),
#     fg="#816A25",
# )
# city_label.place(x=230, y=190)


# time_label = tk.Label(
#     root,
#     font=("helvetica", 20, "bold"),
#     fg="#816A25",
# )
# time_label.place(x=80, y=230)



# clock_label = tk.Label(
#     root,
#     font=("helvetica", 20, "bold"),
#     fg="#816A25",
# )
# clock_label.place(x=80, y=260)



# temperature_label = tk.Label(
#     root,
#     font=("helvetica", 20, "bold"),
#     fg="#816A25",
# )
# temperature_label.place(x=80, y=310)



# condition_label = tk.Label(
#     root,
#     font=("helvetica", 20, "bold"),
#     fg="#816A25",
# )   
# condition_label.place(x=80, y=350)


# root.mainloop()









































import os
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import requests
from datetime import datetime
from threading import Thread



API_KEY = "3a1c18f6690eaa70f1d47c93c0151ac7"  
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
FORECAST_URL = "https://api.openweathermap.org/data/2.5/forecast"


BACKGROUND_IMAGE = "background.jpg.jpeg"



COLORS = {
    "bg_dark": "#1e2430",     #main background color
    "bg_card": "#2a3142",     #background of the labels
    "bg_input": "#353c50",    #background of the fields entry 
    "accent": "#4a9eff",      #color for buttons and weather
    "accent_hover": "#3a8eef",  #
    "text": "#ffffff",
    "text_dim": "#c8d0e0",
    "success": "#4caf50",
    "error": "#f44336",
    "warning": "#ff9800",
}

FONTS = {
    "title": ("Segoe UI", 22, "bold"),
    "subtitle": ("Segoe UI", 12),
    "city": ("Segoe UI", 20, "bold"),
    "temp_big": ("Segoe UI", 48, "bold"),
    "label": ("Segoe UI", 11),
    "value": ("Segoe UI", 11, "bold"),
    "btn": ("Segoe UI", 11, "bold"),
    "small": ("Segoe UI", 9),
}

WINDOW_W, WINDOW_H = 750, 850       #عرض و طول پنجره



def kelvin_to_celsius(kelvin):    #تایع کمکی
    return kelvin - 273.15


def get_weather_emoji(weather_main):     #select the emoji according the statues of weather
    emojis = {                                                                         #we use a dictionary that conect every statues with a emoji
        "Clear": "☀️", "Clouds": "☁️", "Rain": "🌧️", "Drizzle": "🌦️",                  #dictionary is = get(key, defult).
        "Thunderstorm": "⛈️", "Snow": "❄️", "Mist": "🌫️", "Fog": "🌫️",
        "Haze": "🌫️", "Smoke": "💨", "Dust": "🌪️", "Sand": "🌪️",
        "Ash": "🌋", "Squall": "💨", "Tornado": "🌪️",
    }
    return emojis.get(weather_main, "🌍")




def get_wind_direction(degree):
    directions = ["N", "NE", "E", "SE", "S", "SW", "W", "NW"]                  #degree of the wind in API is 0, 360 
    return directions[round(degree / 45) % 8]



class WeatherApp:                                                      
    def __init__(self, root):                           #save the main window so we could use in other method
        self.root = root
        self.root.title("🌤️ Weather App")               #window title
        self.root.geometry(f"{WINDOW_W}x{WINDOW_H}")
        self.root.configure(bg=COLORS["bg_dark"])
        self.root.resizable(False, False)

        self.current_city = ""
        self.bg_image = None  

        
        self._set_background()         # 

        
        self._build_ui()

    
    def _set_background(self):
        """Load background image and stretch it to fill the window."""
        self.bg_canvas = tk.Canvas(
            self.root, width=WINDOW_W, height=WINDOW_H,
            highlightthickness=0, bd=0
        )
        self.bg_canvas.place(x=0, y=0, relwidth=1, relheight=1)

        if not os.path.exists(BACKGROUND_IMAGE):
            # Fallback: plain dark background
            self.bg_canvas.configure(bg=COLORS["bg_dark"])
            print(f"⚠️  Background image '{BACKGROUND_IMAGE}' not found. "
                  f"Using default color instead.")
            return

        try:
            img = Image.open(BACKGROUND_IMAGE).convert("RGB")
            img = img.resize((WINDOW_W, WINDOW_H), Image.LANCZOS)

            
            overlay = Image.new("RGB", img.size, (10, 15, 25))
            blended = Image.blend(img, overlay, alpha=0.45)

            self.bg_image = ImageTk.PhotoImage(blended)
            self.bg_canvas.create_image(0, 0, image=self.bg_image, anchor="nw")
        except Exception as e:
            self.bg_canvas.configure(bg=COLORS["bg_dark"])
            print(f"⚠️  Could not load background image: {e}")

                                                            #Build UI on top of canvas
    def _build_ui(self):
        # We create a transparent Frame on the Canvas, so widgets appear on top            یک فریم میسازیم کع تمام ویجت ها داخلش باشند
        # of the background image.
        self.main_frame = tk.Frame(self.bg_canvas, bg=COLORS["bg_dark"])
        self.main_frame.place(relx=0.5, rely=0.5, anchor="center",
                              relwidth=0.95, relheight=0.97)

        # Make the frame semi-transparent look by matching the dark color.
        # Tkinter itself doesn't support real transparency, so we simulate it
        # with a dark color that blends with the image overlay.

        #Header
        header = tk.Frame(self.main_frame, bg=COLORS["bg_dark"], pady=10)          #دو لیبل داخلش است  یکی عنوان و یکی زیر عنوان
        header.pack(fill="x")

        tk.Label(
            header, text="🌤️ Weather App",
            font=FONTS["title"], bg=COLORS["bg_dark"], fg=COLORS["text"]
        ).pack()

        tk.Label(
            header, text="Get real-time weather for any city",
            font=FONTS["small"], bg=COLORS["bg_dark"], fg=COLORS["text_dim"]
        ).pack()

        #Search Bar
        search_frame = tk.Frame(self.main_frame, bg=COLORS["bg_dark"], pady=8)
        search_frame.pack(fill="x", padx=20)

        self.entry_city = tk.Entry(                                       #فیلد وردی متن 
            search_frame, font=FONTS["subtitle"],                         #داخل فیلد رنگ نشانگر
            bg=COLORS["bg_input"], fg=COLORS["text"],
            insertbackground=COLORS["text"],
            relief="flat", bd=0
        )
        self.entry_city.pack(side="left", fill="x", expand=True,
                             ipady=10, padx=(0, 8))
        self.entry_city.insert(0, "Kabul")
        self.entry_city.bind("<Return>", lambda e: self.search_weather())

        self.btn_search = tk.Button(                                       #by clicking on button the color changes
            search_frame, text="🔍 Search", font=FONTS["btn"],
            bg=COLORS["accent"], fg="white",
            activebackground=COLORS["accent_hover"],
            activeforeground="white",
            relief="flat", bd=0, cursor="hand2",                          #when mouse is on the button it takes shape hand
            padx=20, pady=10,
            command=self.search_weather                                    #function does run by clicking
        )
        self.btn_search.pack(side="left")

        #Forecast Button
        forecast_frame = tk.Frame(self.main_frame, bg=COLORS["bg_dark"])          #پیش بینی کردن چند روز اینده 
        forecast_frame.pack(fill="x", padx=20, pady=(0, 8))

        self.btn_forecast = tk.Button(
            forecast_frame, text="📅 5-Day Forecast", font=FONTS["btn"],
            bg=COLORS["bg_card"], fg=COLORS["text"],
            activebackground=COLORS["bg_input"],
            activeforeground=COLORS["text"],
            relief="flat", bd=0, cursor="hand2",
            padx=15, pady=8,
            command=self.show_forecast
        )
        self.btn_forecast.pack(side="left")

        #Main Weather Card                               
        self.card_main = tk.Frame(
            self.main_frame, bg=COLORS["bg_card"], padx=20, pady=10
        )
        self.card_main.pack(fill="x", padx=20, pady=8)

        self.lbl_city = tk.Label(                    
            self.card_main, text="—",
            font=FONTS["city"], bg=COLORS["bg_card"], fg=COLORS["text"]
        )
        self.lbl_city.pack()

        self.lbl_emoji = tk.Label(                                   #
            self.card_main, text="🌍",                                   #لیبل برزگ برای ایموجی وضعیت عو
            font=("Segoe UI", 56),                
            bg=COLORS["bg_card"], fg=COLORS["text"]
        )
        self.lbl_emoji.pack(pady=2)

        self.lbl_temp = tk.Label(                                            # دما با رنگ آبی برجستع و بزرگ 
            self.card_main, text="--°C",
            font=FONTS["temp_big"], bg=COLORS["bg_card"], fg=COLORS["accent"]
        )
        self.lbl_temp.pack()

        self.lbl_desc = tk.Label(                                                   #توضیح وضعیت هوا
            self.card_main, text="Waiting for search...",
            font=FONTS["subtitle"], bg=COLORS["bg_card"], fg=COLORS["text_dim"]
        )
        self.lbl_desc.pack()

        #Info Grid                                                                 #we make a empty dictionary for labels list of info_items
        self.info_frame = tk.Frame(self.main_frame, bg=COLORS["bg_dark"])          #incloud enternal buttons and posters
        self.info_frame.pack(fill="x", padx=20, pady=4)

        self.info_labels = {}
        info_items = [
            ("feels_like", "🤔 Feels Like"),             #احساس واقعی دما
            ("humidity", "💧 Humidity"),                 #رطویت
            ("pressure", "🎈 Pressure"),                 #فشار هوا
            ("wind", "💨 Wind"),                         #باد
            ("visibility", "👁️ Visibility"),             #دید افقی
            ("sunrise", "🌅 Sunrise"),                   
            ("sunset", "🌇 Sunset"),
            ("minmax", "⬇️⬆️ Min/Max"),
        ]

        for i, (key, label) in enumerate(info_items):
            row, col = i // 2, i % 2

            cell = tk.Frame(self.info_frame, bg=COLORS["bg_card"],
                            padx=12, pady=5)
            cell.grid(row=row, column=col, padx=5, pady=2, sticky="nsew")         #grid که برخلاف pack است منظم می چیند

            tk.Label(
                cell, text=label, font=FONTS["label"],
                bg=COLORS["bg_card"], fg=COLORS["text_dim"], anchor="w"
            ).pack(fill="x")

            value_lbl = tk.Label(
                cell, text="—", font=FONTS["value"],
                bg=COLORS["bg_card"], fg=COLORS["text"], anchor="w"
            )
            value_lbl.pack(fill="x")
            self.info_labels[key] = value_lbl

        self.info_frame.columnconfigure(0, weight=1)                      
        self.info_frame.columnconfigure(1, weight=1)

        #Status Bar
        self.status = tk.Label(                   #در پایین پنجره برای نمایش پیام های در حال بازگذاری یا اخرین به روزرسانی
            self.main_frame, text="Ready",
            font=FONTS["small"], bg=COLORS["bg_dark"], fg=COLORS["text_dim"]
        )
        self.status.pack(side="bottom", pady=4)

    #Status Helpers
    def set_status(self, text, color=None):                                         #توایع کمکی مثلا اگر رنگ داده تشد رنک پیش فرض استفادع شود
        self.status.config(text=text, fg=color or COLORS["text_dim"])

    #Fetch Current Weather                                                
    def search_weather(self):                                    #گرفتن اب و هوای فعلی 
        city = self.entry_city.get().strip()                         
        if not city:
            messagebox.showwarning("Warning", "Please enter a city name!")
            return

        self.set_status("⏳ Fetching weather data...", COLORS["warning"])        #گرفتن اب و هوا
        self.btn_search.config(state="disabled")
        Thread(target=self._fetch_weather, args=(city,), daemon=True).start()             #اگر درخواست شبکه در thread اصلی باشد رابط گراقیکی تا پایان 
                                                                                          #درخواست فریز می شود با thread ui روان می ماند
    def _fetch_weather(self, city):                              #دریافت داده از api 
        params = {"q": city, "appid": API_KEY, "lang": "en"}       #q = city name , appid=APIkey , lang= language
        try:
            r = requests.get(BASE_URL, params=params, timeout=10)      #با پارامتر get درخواست می دهیم اگر 10 ثانیع طول کشید لغو شود
            if r.status_code == 404:                                    #یعنی شهر پیدا شد
                self.root.after(0, lambda: self._error("❌ City not found!"))    
                return
            if r.status_code == 401:                                    #یعنی API KEY اشتیاه است
                self.root.after(0, lambda: self._error("❌ Invalid API key!"))
                return
            r.raise_for_status()
            data = r.json()
            self.current_city = city
            self.root.after(0, lambda: self._display_weather(data))
        except requests.exceptions.ConnectionError:
            self.root.after(0, lambda: self._error("❌ No internet connection!"))
        except requests.exceptions.Timeout:
            self.root.after(0, lambda: self._error("❌ Request timed out!"))
        except Exception as e:
            self.root.after(0, lambda: self._error(f"❌ Error: {e}"))

    def _error(self, msg):                                        #پیام خطا را در نوار وضعیت تمایش می دهیم
        self.set_status(msg, COLORS["error"])                     #دکمه را دوباره فعال می کنیم
        self.btn_search.config(state="normal")                     #یک پنجره خطا باز می کنیم
        messagebox.showerror("Error", msg)

    #  Display Weather                                            
    def _display_weather(self, data):                           #نمایش داده اب و هوا
        city = data["name"]                                     
        country = data["sys"]["country"]
        weather_main = data["weather"][0]["main"]
        desc = data["weather"][0]["description"]
        temp = kelvin_to_celsius(data["main"]["temp"])
        feels_like = kelvin_to_celsius(data["main"]["feels_like"])
        temp_min = kelvin_to_celsius(data["main"]["temp_min"])
        temp_max = kelvin_to_celsius(data["main"]["temp_max"])
        pressure = data["main"]["pressure"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]
        wind_deg = data["wind"].get("deg", 0)
        visibility = data.get("visibility", 0) / 1000       
        sunrise = datetime.fromtimestamp(data["sys"]["sunrise"]).strftime("%H:%M")
        sunset = datetime.fromtimestamp(data["sys"]["sunset"]).strftime("%H:%M")

        emoji = get_weather_emoji(weather_main)
        wind_dir = get_wind_direction(wind_deg)

        self.lbl_city.config(text=f"{city}, {country}")                #به روز رسانی ویجت ها
        self.lbl_emoji.config(text=emoji)
        self.lbl_temp.config(text=f"{temp:.1f}°C")
        self.lbl_desc.config(text=desc.capitalize())

        self.info_labels["feels_like"].config(text=f"{feels_like:.1f}°C")
        self.info_labels["humidity"].config(text=f"{humidity}%")
        self.info_labels["pressure"].config(text=f"{pressure} hPa")
        self.info_labels["wind"].config(text=f"{wind_speed} m/s ({wind_dir})")
        self.info_labels["visibility"].config(text=f"{visibility:.1f} km")
        self.info_labels["sunrise"].config(text=sunrise)
        self.info_labels["sunset"].config(text=sunset)
        self.info_labels["minmax"].config(text=f"{temp_min:.1f}° / {temp_max:.1f}°")

        self.set_status(
            f"✅ Last updated: {datetime.now().strftime('%H:%M:%S')}",
            COLORS["success"]
        )
        self.btn_search.config(state="normal")

    #5-Day Forecast
    def show_forecast(self):                      #پیش بینی 5 روزه
        city = self.entry_city.get().strip()
        if not city:
            messagebox.showwarning("Warning", "Please enter a city name first!")
            return

        self.set_status("⏳ Fetching forecast...", COLORS["warning"])
        self.btn_forecast.config(state="disabled")
        Thread(target=self._fetch_forecast, args=(city,), daemon=True).start()

    def _fetch_forecast(self, city):
        params = {"q": city, "appid": API_KEY, "lang": "en", "units": "metric"}
        try:
            r = requests.get(FORECAST_URL, params=params, timeout=10)
            r.raise_for_status()
            data = r.json()
            self.root.after(0, lambda: self._show_forecast_window(data))
        except Exception as e:
            self.root.after(0, lambda: self._error(f"❌ Forecast error: {e}"))
            self.root.after(0, lambda: self.btn_forecast.config(state="normal"))

    def _show_forecast_window(self, data):
        self.btn_forecast.config(state="normal")
        self.set_status("✅ Forecast loaded", COLORS["success"])

        win = tk.Toplevel(self.root)
        win.title(f"📅 5-Day Forecast - {data['city']['name']}")
        win.geometry("500x550")
        win.configure(bg=COLORS["bg_dark"])
        win.resizable(False, False)

        tk.Label(
            win, text="📅 5-Day Forecast",
            font=FONTS["title"], bg=COLORS["bg_dark"], fg=COLORS["text"]
        ).pack(pady=15)

        tk.Label(
            win, text=f"🏙️ {data['city']['name']}, {data['city']['country']}",
            font=FONTS["subtitle"], bg=COLORS["bg_dark"], fg=COLORS["text_dim"]
        ).pack(pady=(0, 10))

        daily = {}
        for item in data["list"]:
            date = item["dt_txt"].split(" ")[0]
            daily.setdefault(date, []).append(item)

        container = tk.Frame(win, bg=COLORS["bg_dark"])
        container.pack(fill="both", expand=True, padx=15, pady=10)

        for date, items in list(daily.items())[:5]:
            temps = [i["main"]["temp"] for i in items]
            tmin, tmax = min(temps), max(temps)
            weather = items[0]["weather"][0]["main"]
            desc = items[0]["weather"][0]["description"]
            emoji = get_weather_emoji(weather)

            date_obj = datetime.strptime(date, "%Y-%m-%d")
            date_str = date_obj.strftime("%A %d %B")

            card = tk.Frame(container, bg=COLORS["bg_card"], padx=15, pady=10)
            card.pack(fill="x", pady=4)

            left = tk.Frame(card, bg=COLORS["bg_card"])
            left.pack(side="left", fill="x", expand=True)

            tk.Label(
                left, text=f"{emoji}  {date_str}",
                font=FONTS["value"], bg=COLORS["bg_card"],
                fg=COLORS["text"], anchor="w"
            ).pack(fill="x")

            tk.Label(
                left, text=desc.capitalize(),
                font=FONTS["small"], bg=COLORS["bg_card"],
                fg=COLORS["text_dim"], anchor="w"
            ).pack(fill="x")

            right = tk.Frame(card, bg=COLORS["bg_card"])
            right.pack(side="right")

            tk.Label(
                right, text=f"⬆️ {tmax:.1f}°",
                font=FONTS["value"], bg=COLORS["bg_card"],
                fg=COLORS["error"]
            ).pack(anchor="e")

            tk.Label(
                right, text=f"⬇️ {tmin:.1f}°",
                font=FONTS["value"], bg=COLORS["bg_card"],
                fg=COLORS["accent"]
            ).pack(anchor="e")


#Run the Application 
if __name__ == "__main__":
    if API_KEY == "YOUR_API_KEY_HERE":
        print("⚠️ Please set your API key in the API_KEY variable ")
        print("   Get one at https://openweathermap.org/api")
    else:
        root = tk.Tk()
        app = WeatherApp(root)
        root.mainloop()