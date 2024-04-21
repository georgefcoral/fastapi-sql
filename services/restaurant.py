from models.restaurant import Restaurant as RestaurantModel
from schemes.restaurant import Restaurant

class RestaurantService:

    def __init__(self, db) -> None:
        self.db = db

    def get_all(self):
        response = self.db.query(RestaurantModel).all()
        return response

    def get(self, id: str):
        response = self.db.query(RestaurantModel).filter(RestaurantModel.id == id).first()
        return response

    def create(self, restaurant: Restaurant):
        new_restaurant = RestaurantModel(**restaurant.model_dump())
        self.db.add(new_restaurant)
        self.db.commit()
        return restaurant

    def update(self, id: str, restaurant: Restaurant):
        response = self.db.query(RestaurantModel).filter(RestaurantModel.id == id).first()
        if not response:
            return None

        response.rating = restaurant.rating
        response.name = restaurant.name
        response.site = restaurant.site
        response.email = restaurant.email
        response.phone = restaurant.phone
        response.street = restaurant.street
        response.city = restaurant.city
        response.state = restaurant.state
        response.lat = restaurant.lat
        response.lng = restaurant.lng

        self.db.commit()
        return restaurant

    def delete(self, id: str):
        response = self.db.query(RestaurantModel).filter(RestaurantModel.id == id).first()
        if not response:
            return None

        self.db.delete(response)
        self.db.commit()
        return response
