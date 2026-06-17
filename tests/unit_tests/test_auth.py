from src.services.auth import AuthService



class TestAuthService():

    def test_create_access_token(self):
        data = {"user_id": 1}
        jwt_token = AuthService().create_access_token(data)

        assert jwt_token
        assert isinstance(jwt_token, str)

    def test_hash_password(self):
        password_one = "dadaddadad"
        hashed_password_one = AuthService().hash_password(password_one)
        password_two = "xcvvxcv"
        hashed_password_two = AuthService().hash_password(password_two)
        assert hashed_password_one != hashed_password_two
        assert isinstance(hashed_password_one, str)
        assert isinstance(hashed_password_two, str)
        assert AuthService().verify_password(password_one, hashed_password_one) is True
        assert AuthService().verify_password(password_two, hashed_password_two) is True