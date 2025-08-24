# To create a bookingmodel with user_id, room_id, nights (int must >= 1) rate per_nights
# Also add the computed field : total_amount = nights * rate per_nights
from pydantic import BaseModel, Field, computed_field

class Booking(BaseModel):
    user_id: int
    room_id : int
    nights : int = Field(..., ge=1)
    rate_per_nights = float


    @computed_field
    @property
    def total_amount(self) -> float:
        return self.nights * self.rate_per_nights
