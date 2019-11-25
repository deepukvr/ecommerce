from django.test import TestCase
from authapp.models import Signin, Signup


class SigninTestCase(TestCase):
    def setUp(self):
        Signin.objects.create(username="chakra",password="deeu")
    def test_signin_info(self):
        c1=Signin.objects.get(username="chakra",password="deeu")
        self.assertEqual(c1.get_user(),"chakra")
        self.assertEqual(c1.get_pswd(),"deeu")

class SignupTestCase(TestCase):
    def setUp(self):
        Signup.objects.create(firstname="pratap",lastname="reddy",username="chakra",
                              phone_no="7286851908",email="deepthikotella@gmail.com",password="deeu",rpsw="deepu")
    def test_signin_info(self):
        c2=Signup.objects.get(firstname="pratap")
        self.assertEqual(c2.get_firstname(),"pratap")
