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

def Authentication(username,password):
    client = APIClient()
    role = Roles.objects.create(id=1,name="Super Admin",)
    role = Roles.objects.create(id=2,name="Admin",)
    user = User.objects.create(email=username,role=role,username=username)
    user.set_password(password)
    user.save()
    headers = {'Content-Type': 'application/json'}
    data = {"password":password,"username":username}
    url = reverse('signin')
    response = client.post(url, data=data,format='json',headers=headers)
    res = response.json()
    return {"token":"Bearer "+res["data"]["access"],"id":user.id}


class Vendor_Orders_Test_cases(APITestCase):
    token = ""

    def setUp(self):
        self.client = APIClient()
        self.username = "superadmin@test.com"
        self.password = "super@123"
        self.id = 0


    def test_CreateVendor(self):
        authentication = Authentication(self.username,self.password)
        headers = {
            'Authorization': authentication["token"],
            'Content-Type': 'application/json',
        }
        data = {"password":"vendortest","email":"vendor4@gmail.com","name":"test_user","address":"dehradun","contact_details":"9898765678,lkkf fkf"}
        url = reverse('create_vendor')
        response = self.client.post(url, data,format='json',headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_GetVendorList(self):
        authentication = Authentication(self.username,self.password)
        url = reverse('vendor_list')
        response = self.client.get(url, {'limit': 1, 'size': 10},HTTP_AUTHORIZATION=authentication["token"])
        self.assertEqual(response.status_code, 200)

    def test_UpdateVendor(self):
        authentication = Authentication(self.username,self.password)
        headers = {'AUTHORIZATION': authentication["token"],'Content-Type': 'application/json'}
        data = {"name":"test_user","address":"dehradun","contact_details":"9898765678,lkkf fkf"}
        url = "/api/vendors/update/"+str(authentication["id"])+"/"
        response = self.client.put(url, data,format='json',headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_DeleteVendors(self):
        authentication = Authentication(self.username,self.password)
        headers = {'AUTHORIZATION': authentication["token"],'Content-Type': 'application/json'}
        url = "/api/vendors/delete/"+str(authentication["id"])+"/"
        response = self.client.delete(url, headers=headers)
        self.assertEqual(response.status_code, 200)


    def test_CreatePurchaseOrders(self):
        authentication = Authentication(self.username,self.password)
        headers = {'Authorization': authentication["token"],'Content-Type': 'application/json'}
        data = {"vendor_code":"vendor3","items":{"product_name":"p1","category":"c1","quantity":6},"quantity":6}
        url = reverse('create_purchase_order')
        response = self.client.post(url, data,format='json',headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_GetPurchaseOrdersList(self):
        authentication = Authentication(self.username,self.password)
        url = reverse('purchase_orders_list')
        response = self.client.get(url, {'limit': 1, 'size': 10},HTTP_AUTHORIZATION=authentication["token"])
        self.assertEqual(response.status_code, 200)

    def test_UpdatePurchaseOrders(self):
        authentication = Authentication(self.username,self.password)
        headers = {'AUTHORIZATION': authentication["token"],'Content-Type': 'application/json'}
        data = {"vendor_code":"vendor3","items":{"product_name":"p1","category":"c1","quantity":6},"quantity":6}
        url = "/api/purchase_orders/update/1/"
        response = self.client.put(url, data,format='json',headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_DeletePurchaseOrders(self):
        authentication = Authentication(self.username,self.password)
        headers = {'AUTHORIZATION': authentication["token"],'Content-Type': 'application/json'}
        url = "/api/purchase_orders/delete/1/"
        response = self.client.delete(url, headers=headers)
        self.assertEqual(response.status_code, 200)


    def test_GetVendorPerformance(self):
        authentication = Authentication(self.username,self.password)
        url = "/api/vendors/2/performance/"
        response = self.client.get(url ,HTTP_AUTHORIZATION=authentication["token"])
        self.assertEqual(response.status_code, 200)