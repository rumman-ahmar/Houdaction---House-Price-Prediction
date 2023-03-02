import pickle
import pandas as pd
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles


app = FastAPI()

# configure template
templates = Jinja2Templates(directory="templates")
# configure static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# get cities
cities = list(pd.read_csv("cities.csv")['city'])

# load model
with open("knr_model", "rb") as f:
    knr_model = pickle.load(f)


# helper function
def city_mapping(city):
    city_position = [0, 0, 0, 0, 0, 0, 0]
    idx = cities.index(city)
    if idx == 0:
        return city_position

    city_position[idx-1] = 1
    return city_position


@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


######################
# APIs
######################
@app.get("/cities")
def get_cities():
    return cities


@app.get("/predict_price")
def get_predict_price(city, under_construction: int, bhk: int,
                      sqr_ft: float, rtm: int):

    city_position = city_mapping(city)
    test = [under_construction, bhk, sqr_ft, rtm]
    test = test + city_position
    print(test)
    predicted_price = knr_model.predict([test])
    return f"Predicted price is {round(predicted_price[0], 2)} Lacs"
