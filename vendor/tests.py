from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from rest_framework.test import APITestCase
from vendor.models.users import User,Roles

class FirstTestCases(TestCase):

    def setUp(self):
        pass
    def test_equalValue(self):
        self.assertEqual(1,1)

class Vendor_Orders_Test_cases(APITestCase):
    token = ""

    def setUp(self):
        self.client = APIClient()
        self.username = "superadmin@test.com"
        self.password = "super@123"
        self.id = 0
    
    def test_CreateauthUser(self):
        role = Roles.objects.create(id=1,name="Super Admin",)
        role = Roles.objects.create(id=2,name="Admin",)
        user = User.objects.create(email=self.username,role=role,username=self.username)
        user.set_password(self.password)
        user.save()
        headers = {'Content-Type': 'application/json'}
        data = {"password":self.password,"username":user.username}
        url = reverse('signin')
        response = self.client.post(url, data=data,format='json',headers=headers)
        res = response.json()
        Vendor_Orders_Test_cases.token = "Bearer "+res["data"]["access"]
        self.assertEqual(2,2)


    def test_CreateVendor(self):
        role = Roles.objects.create(id=2,name="Admin",)
        user = User.objects.create(email=self.username,role=role,username=self.username)
        user.set_password(self.password)
        user.save()
        url = reverse('signin')
        data = {"username":"superadmin@test.com", "password":"super@123"}
        response = self.client.post(url, data=data,format='json',headers={'Content-Type': 'application/json'})
        res = response.json()
        token = "Bearer "+res["data"]["access"]
        headers = {
            'Authorization': token,
            'Content-Type': 'application/json',
        }
        data = {"password":"vendortest","email":"vendor4@gmail.com","name":"test_user","address":"dehradun","contact_details":"9898765678,lkkf fkf"}
        url = reverse('create_vendor')
        response = self.client.post(url, data,format='json',headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_GetVendorList(self):
        role = Roles.objects.create(id=2,name="Admin",)
        user = User.objects.create(email=self.username,role=role,username=self.username)
        user.set_password(self.password)
        user.save()
        url = reverse('signin')
        data = {"username":"superadmin@test.com", "password":"super@123"}
        response = self.client.post(url, data=data,format='json',headers={'Content-Type': 'application/json'})
        res = response.json()
        token = "Bearer "+res["data"]["access"]
        url = reverse('vendor_list')
        response = self.client.get(url, {'limit': 1, 'size': 10},HTTP_AUTHORIZATION=token)
        self.assertEqual(response.status_code, 200)

    def test_UpdateVendor(self):
        role = Roles.objects.create(id=2,name="Admin",)
        user = User.objects.create(email=self.username,role=role,username=self.username)
        user.set_password(self.password)
        user.save()
        url = reverse('signin')
        data = {"username":"superadmin@test.com", "password":"super@123"}
        response = self.client.post(url, data=data,format='json',headers={'Content-Type': 'application/json'})
        res = response.json()
        token = "Bearer "+res["data"]["access"]
        headers = {'AUTHORIZATION': token,'Content-Type': 'application/json'}
        data = {"name":"test_user","address":"dehradun","contact_details":"9898765678,lkkf fkf"}
        url = "/api/vendors/update/"+str(user.id)+"/"
        self.id = user.id
        response = self.client.put(url, data,format='json',headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_DeleteVendors(self):
        role = Roles.objects.create(id=2,name="Admin",)
        user = User.objects.create(email=self.username,role=role,username=self.username)
        user.set_password(self.password)
        user.save()
        url = reverse('signin')
        data = {"username":"superadmin@test.com", "password":"super@123"}
        response = self.client.post(url, data=data,format='json',headers={'Content-Type': 'application/json'})
        res = response.json()
        token = "Bearer "+res["data"]["access"]
        headers = {'AUTHORIZATION': token,'Content-Type': 'application/json'}
        url = "/api/vendors/delete/"+str(user.id)+"/"
        response = self.client.delete(url, headers=headers)
        self.assertEqual(response.status_code, 200)