from unittest import TestCase
import openstack_api


class ComputeTests(TestCase):
    def setUp(self):
        conf = openstack_api.init("config.ini")
        self.compute = openstack_api.Compute(conf)

    def test_server_list(self):
        servers = self.compute.server_list()
        self.assertNotEqual(len(servers), 0)
