from pydantic import BaseModel, Field


class Restaurant(BaseModel):
    id: str = None
    rating: int = Field(le=4 , ge=0)
    name: str
    site: str
    email: str
    phone: str
    street: str
    city: str
    state: str
    lat: float = Field(le=90 , ge=-90)
    lng: float = Field(le=180 , ge=-180)

    model_config = {
        "json_scheme_extra": {
            "example": {
                "id": '851f799f-0852-439e-b9b2-df92c43e7672',
                "rating": 0,
                "name": "My Name Second Name",
                "site": "www.mysite.com",
                "email": "username@correo.com",
                "phone": "999 999 999",
                "street": "999 Street Test",
                "city": "My City",
                "state": "My State",
                "lat": 19.4400570537131,
                "lng": -99.1270470974249
            }
        }
    }
