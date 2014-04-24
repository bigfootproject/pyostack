from unittest import TestCase
import openstack_api


class IdentityTests(TestCase):
    def setUp(self):
        conf = openstack_api.init("config.ini")
        self.identity = openstack_api.Identity(conf)

    def test_list_tenants(self):
        tenants = self.identity.list_tenants()
        self.assertNotEqual(len(tenants), 0)
