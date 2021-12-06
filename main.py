import eel
from pyowm import OWM

owm = OWM("6ac92146bd99b3fb3af69bb9eb99027a")

@eel.expose
def get_weather(place):
    
    mgr = owm.weather_manager()

    observation = mgr.weather_at_place(place)
    w = observation.weather

    temp = w.temperature('celsius')['temp']
    return "В місті " + place + " на даний момент " + str(temp) + " градусів!"

eel.init("./web/")
eel.start("main.html", size=(700,700))
