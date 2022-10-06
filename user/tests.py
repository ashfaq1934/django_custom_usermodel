from django.test import TestCase
from django.contrib.auth import get_user_model

class UserAccountTests(TestCase):
    def test_new_superuser(self):
        db = get_user_model()
        super_user = db.objects.create_superuser(
            'test@testsuper.com', 'username', 'firstname', 'password')
        self.assertEqual(super_user.email, 'test@testsuper.com')
        self.assertEqual(super_user.user_name, 'username')
        self.assertEqual(super_user.first_name, 'firstname')
        self.assertTrue(super_user.is_superuser)
