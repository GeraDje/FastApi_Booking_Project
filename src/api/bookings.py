from fastapi import APIRouter
from src.api.dependencies import UserIdDep, DBDep
from src.schemas.bookings import BookingAddRequest, BookingAdd

router = APIRouter(prefix="/bookings", tags=["Бронирования"])


@router.post("/")
async def add_booking(
        user_id: UserIdDep,
        db: DBDep,
        booking_data: BookingAddRequest,

):
    room = await db.rooms.get_one_or_none(id=booking_data.room_id)
    print(f"--------{room}---------")
    room_price: int = room.price
    print(f"--------{room_price}---------")
    _booking_data = BookingAdd(
        user_id=user_id,
        price=room_price,
        **booking_data.model_dump(),
    )
    print(f"--------{_booking_data}---------")
    booking = await db.bookings.add(_booking_data)
    await db.commit()
    return {"status": "OK", "data": booking}

@router.post("/")
async def get_bookings():
