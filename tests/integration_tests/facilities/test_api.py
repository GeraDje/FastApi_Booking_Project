async def test_get_facilities(ac):
    response = await ac.get("/facilities")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


async def test_create_facili(ac):
    facilities_title = "Test Facilities"
    responce = await ac.post(
        "/facilities",
        json={
            "title": facilities_title,
        }
    )
    assert responce.status_code == 200
    res = responce.json()
    assert isinstance(res, dict)
    assert res["data"]["title"] == facilities_title