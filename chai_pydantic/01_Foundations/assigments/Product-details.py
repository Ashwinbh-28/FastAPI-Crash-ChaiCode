# Create a Product model with id, name, price and in_stock
from pydantic import BaseModel

class ProductDetail(BaseModel):
    id: int
    name: str
    price: float
    in_stock: bool = True

product_data = {
    "id": 1205,
    "name": 'Lux',
    "price": 25.00,
}

product_avail = ProductDetail(**product_data)
print(product_avail)
