from typing import List
import uuid
import math
from geopy.distance import geodesic
from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from starlette.responses import JSONResponse

from config.database import Session
from schemes.restaurant import Restaurant
from services.restaurant import RestaurantService

restaurant_router = APIRouter()


def computeStd(data, mean):
    sum = 0
    for item in data:
        sum = sum + (item - mean) ** 2
    return math.sqrt(sum/len(data))


@restaurant_router.get('/restaurants/statistics', status_code=200)
def get_restaurants_statistics(latitude: float, longitude: float, radius: float) -> JSONResponse:

    if latitude > 90 or latitude < -90:
        return JSONResponse(status_code=400, content=jsonable_encoder({"message": "latitude should be in the range of -90 to 90"}))
    
    if longitude > 180 or longitude < -180:
        return JSONResponse(status_code=400, content=jsonable_encoder({"message": "longitude should be in the range of -180 to 180"}))
    
    if radius < 0:
        return JSONResponse(status_code=400, content=jsonable_encoder({"message": "Invalid radius"}))
    

    db = Session()
    restaurants = RestaurantService(db).get_all()

    count = 0
    avg_rating = 0
    ratings = []
    std = 0

    for restaurant in restaurants:
        distance = geodesic((latitude,longitude),(restaurant.lat, restaurant.lng)).m
        if distance <= radius:
            count = count + 1
            avg_rating = avg_rating + restaurant.rating
            ratings.append(restaurant.rating)

    if count > 0:
        avg_rating = avg_rating/count
        std = computeStd(ratings, avg_rating)

    print(std)

    return JSONResponse(status_code=200, content=jsonable_encoder({"count":count, "avg":avg_rating, "std":std}))

@restaurant_router.get('/restaurants', tags=['restaurants'], response_model=List[Restaurant], status_code=200)
def getRestaurants() -> JSONResponse:
    db = Session()
    response = RestaurantService(db).get_all()
    return JSONResponse(status_code=200, content=jsonable_encoder(response))


@restaurant_router.get('/restaurants/{id}', tags=['restaurants'], response_model=Restaurant)
def getRestaurant(id: str) -> JSONResponse:
    db = Session()
    response = RestaurantService(db).get(id)

    if not response:
        return JSONResponse(status_code=404, content={"message": "Restaurant not found"})

    return JSONResponse(status_code=200, content=jsonable_encoder(response))


@restaurant_router.post('/restaurants', tags=['restaurants'], response_model=dict, status_code=201)
def createRestaurant(restaurant: Restaurant) -> JSONResponse:

    if restaurant.lat > 90 or restaurant.lat < -90:
        return JSONResponse(status_code=400, content=jsonable_encoder({"message": "latitude should be in the range of -90 to 90"}))
    
    if restaurant.lng > 180 or restaurant.lng < -180:
        return JSONResponse(status_code=400, content=jsonable_encoder({"message": "longitude should be in the range of -180 to 180"}))
    
    db = Session()
    restaurant.id = str(uuid.uuid4());
    RestaurantService(db).create(restaurant);
    return JSONResponse(status_code=201, content=jsonable_encoder(restaurant));


@restaurant_router.put('/restaurants/{id}', tags=['restaurants'], response_model=dict, status_code=200)
def updateRestaurant(id: str, restaurant: Restaurant) -> JSONResponse:
    db = Session()
    response = RestaurantService(db).update(id, restaurant)

    if not response:
        return JSONResponse(status_code=404, content={"message": "Restaurant not found"})

    return JSONResponse(status_code=200, content={"message": "Restaurant updated"})


@restaurant_router.delete('/restaurants/{id}', tags=['restaurants'], response_model=dict, status_code=200)
def deleteRestaurant(id: str) -> JSONResponse:
    db = Session()
    response = RestaurantService(db).delete(id)

    if not response:
        return JSONResponse(status_code=404, content={"message": "Restaurant not found"})

    return JSONResponse(status_code=200, content={"message": "Restaurant deleted"})
