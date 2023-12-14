from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from rest_framework.test import APITestCase

class Vendor_Orders_Test_cases(APITestCase):

    def setUp(self):
        self.client = APIClient()

    def test_GetVendorList(self):
        url = reverse('vendor_list')
        headers = {"Authorization":"Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzMzNzMwNjUzLCJpYXQiOjE3MDIxOTQ2NTMsImp0aSI6IjdiNDNhMzkyNTFjNDRhZDNhMjFmYjdmM2FlN2JiYWFkIiwidXNlcl9pZCI6MX0.kay6hoRRD0f-ZU5uoMKGdEnQnU1KKNYUVCmVOJYNicg"}
        response = self.client.get(url,headers=headers)
        print(response,"response response response response response")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    """def test_CreateVendor(self):
        client = APIClient()
        url = reverse('vendors/create')
        response = client.post(url, {'data': 'sample'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_UpdateVendor(self):
        client = APIClient()
        url = reverse('vendors/update/2/')
        response = client.put(url, {'data': 'updated'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)"""
