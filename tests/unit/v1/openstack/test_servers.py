import unittest
from core.v1.openstack.servers import OpenstackServer
from tests.unit.fixture_data.openstack import server as OpenstackServerFixture



class TestServers(unittest.TestCase):
    def setUp(self):
        self.openstack_server_fixture = OpenstackServerFixture.ServerFixtures()
        self.openstack_server_fixture._setUp()
        self.openstack_servers_list = self.openstack_server_fixture.list()
        self.server_manager = OpenstackServer(server=self.openstack_server_fixture)

    def test_openstack_server_stop(self):
        self.openstack_server_fixture.status = "ACTIVE"
        self.assertEqual(self.server_manager.stop()[0].status_code, 202)
        self.assertEqual(self.server_manager.get_status(), 'STOPPED')


    def test_openstack_server_start(self):
        self.openstack_server_fixture.status = "STOPPED"
        self.assertEqual(self.server_manager.start()[0].status_code, 202)
        self.assertEqual(self.server_manager.get_status(), 'ACTIVE')

    def test_openstack_server_reboot(self):
        self.openstack_server_fixture.status = "ACTIVE"
        self.assertEqual(self.server_manager.reboot()[0].status_code, 202)
        self.assertEqual(self.server_manager.get_status(), 'ACTIVE')

    def test_openstack_server_get_status(self):
        self.assertEqual(self.server_manager.get_status(), self.openstack_server_fixture.status)

    def test_openstack_server_get_vnc_console(self):
        self.assertEqual(self.server_manager.get_vnc_console(), self.openstack_server_fixture.server_info["console"])

    def test_openstack_server_delete(self):
        self.assertEqual(self.server_manager.delete()[0].status_code, 202)
        self.assertEqual(self.server_manager.get_status(), 'DELETED')

    def test_openstack_server_get_console_output(self):
        self.assertEqual(self.server_manager.get_console_output(), 'Console-Output')



if __name__ == '__main__':
    unittest.main()