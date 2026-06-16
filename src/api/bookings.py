from fastapi import APIRouter, HTTPException

from src.api.dependencies import DBDep, UserIdDep
from src.exceptions import ObjectNotFoundException, AllRoomsAreBookedException, RoomNotFoundHTTPException
from src.schemas.bookings import BookingAddRequest, BookingAdd
from src.schemas.hotels import Hotel
from src.schemas.rooms import Room
from src.services.bookings import BookingsService

router = APIRouter(prefix="/bookings", tags=["Бронирования"])


@router.get("")
async def get_bookings(db: DBDep):
    return await BookingsService(db).get_bookings()


@router.get("/me")
async def get_my_bookings(user_id: UserIdDep, db: DBDep):

    return await BookingsService(db).get_my_bookings(user_id)


@router.post("")
async def add_booking(
    user_id: UserIdDep,
    db: DBDep,
    booking_data: BookingAddRequest,
):
    try:
        booking = await BookingsService(db).add_booking(user_id, booking_data)
    except AllRoomsAreBookedException:
        raise AllRoomsAreBookedException()

    return {"status": "OK", "data": booking}