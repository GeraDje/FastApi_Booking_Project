from datetime import date
from src.schemas.bookings import BookingAdd


async def test_add_crud(db):
    user_id = (await db.users.get_all())[0].id
    room_id = (await db.rooms.get_all())[0].id
    booking_data = BookingAdd(
        user_id=user_id,
        room_id=room_id,
        date_from=date(2021, 1, 3),
        date_to=date(2021, 1, 1),
        price=100,
    )
    new_booking = await db.bookings.add(booking_data)

    # получить эту бронь и убедиться что она есть
    booking = await db.bookings.get_one_or_none(id=new_booking.id)
    assert booking
    assert booking.id == new_booking.id
    assert booking.room_id == new_booking.room_id
    assert booking.user_id == new_booking.user_id
    assert booking.model_dump(exclude={"id"}) == booking_data.model_dump()

    # обновить бронь
    update_data = date(2021, 12, 3)
    updated_booking_data = BookingAdd(
        user_id=user_id,
        room_id=room_id,
        date_from=date(2021, 12, 1),
        date_to=update_data,
        price=100,
    )
    await db.bookings.edit(updated_booking_data, id=new_booking.id)
    updated_booking = await db.bookings.get_one_or_none(id=new_booking.id)
    assert updated_booking
    assert updated_booking.id == new_booking.id
    assert updated_booking.date_to == update_data

    # удалить бронь
    await db.bookings.delete(id=new_booking.id)
    booking = await db.bookings.get_one_or_none(id=new_booking.id)
    assert not booking
