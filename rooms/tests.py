from rest_framework.test import APITestCase
from . import models
from users.models import User

class TestAmenities(APITestCase):
   

    NAME = "Amenity Test"
    DESC = "Amenity Des"
    URL = "/api/v1/rooms/amenities/"



    def setUp(self): # setUp() 메서드는 다른 테스트 메서드가 실행되기 전에 가장 먼저 실행되어, 데이터 베이스를 설정함.
        models.Amenity.objects.create(
            name = self.NAME,
            description = self.DESC
        )





    def test_all_amenities(self):
        response = self.client.get(self.URL)
        # print(response)  # <Response  status_code=200 , "application/json">
        # print(response.json())  # []
        data = response.json()

        self.assertEqual(response.status_code, 200, "Status code is not 200")

        self.assertIsInstance(data, list)  # assertIsInstance(데이터, 자료형): 데이터가 해당 자료형인지 테스트함.

        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['name'], self.NAME)
        self.assertEqual(data[0]['description'], self.DESC)

    



    def test_create_amenity(self):

        new_amenity_name = "New Amenity"
        new_amenity_description= "New Amenity desc"

        response = self.client.post(self.URL, data={"name": new_amenity_name, "description": new_amenity_description})
        data = response.json()
        self.assertEqual(response.status_code, 200, "Not 200 status code")
        self.assertEqual(data['name'], new_amenity_name)
        self.assertEqual(data['description'], new_amenity_description)

        response = self.client.post(self.URL)
        data = response.json()
        
        self.assertEqual(response.status_code, 400)
        self.assertIn("name", data)  # assertIn("키", 데이터): 키가 데이터에 포함되어 있는지 테스트함.




###############################################



class TestAmenity(APITestCase):
    NAME = "Test Amenity"
    DESC = "Test Dsc"

    def setUp(self):
        models.Amenity.objects.create(
            name=self.NAME,
            description=self.DESC
        )

    def test_amenity_not_found(self):
        response = self.client.get("/api/v1/rooms/amenities/2")
        self.assertEqual(response.status_code, 404)


    def test_get_amenity(self):
        response = self.client.get("/api/v1/rooms/amenities/1")
        self.assertEqual(response.status_code, 200)

        data = response.json()
        self.assertEqual(data["name"], self.NAME)

        self.assertEqual(data['description'], self.DESC)

    
    def test_delete_amenity(self):
        response = self.client.delete("api/v1/rooms/amenities/1")
        self.assertEqual(response.status_code, 404)



###############################################



class TestRooms(APITestCase):

    def setUp(self):
        user = User.objects.create(username="test")
        user.set_password("123")
        user.save()
        self.user = user


    def test_create_room(self):
        response = self.client.post("/api/v1/rooms/")
        self.assertEqual(response.status_code, 403)

        self.client.force_login(self.user)

        response = self.client.post("/api/v1/rooms/")
        print(response)