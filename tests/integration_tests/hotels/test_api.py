import pytest


@pytest.mark.parametrize(
    "date_from,date_to,status_code",
    [
        ("2021-01-01", "2021-01-02", 200),
        ("2025-10-02", "2025-10-02", 422),
        ("dsfsdfsdf","sdfsdfsdf",422)
    ]
)
async def test_get_hotels(ac,db,date_from, date_to, status_code):
    responce = await ac.get(
        "/hotels",
        params={
            "date_from": date_from,
            "date_to": date_to,
        },
    )
    assert responce.status_code == status_code


