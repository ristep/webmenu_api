import unittest
from django.contrib.auth.models import User
from .serializers import (
    MyTokenObtainPairSerializer,
)  # Replace 'myapp' with the actual name of your Django app


class MyTokenObtainPairSerializerTest(unittest.TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(
            username="testuser",
            email="testuser@example.com",
            password="testpassword",
            is_superuser=True,
            is_staff=True,
            is_active=True,
            first_name="Test",
            last_name="User",
        )

    def test_get_token(self):
        # Create an instance of the MyTokenObtainPairSerializer
        serializer = MyTokenObtainPairSerializer()

        # Call the get_token method with the test user
        token = serializer.get_token(self.user)

        # Assert that the token contains the expected user attributes
        self.assertEqual(token["username"], self.user.username)
        self.assertEqual(token["email"], self.user.email)
        self.assertEqual(token["is_superuser"], self.user.is_superuser)
        self.assertEqual(token["is_staff"], self.user.is_staff)
        # You can uncomment and add more assertions for other attributes if needed
        # self.assertEqual(token["is_active"], self.user.is_active)
        # self.assertEqual(token["first_name"], self.user.first_name)
        # self.assertEqual(token["last_name"], self.user.last_name)


if __name__ == "__main__":
    unittest.main()
