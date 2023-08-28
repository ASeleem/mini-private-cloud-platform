from unittest.mock import MagicMock
import fixtures
from novaclient.v2.servers import Server, ServerManager
from novaclient.base import TupleWithMeta
from requests.models import Response 
from novaclient import exceptions 

class ServerFixtures(fixtures.Fixture, Server):

    server_info = {
        "id": 1234,
        "name": "sample-server",
        "image": {
            "id": 2,
            "name": "sample image",
        },
        "flavor": {
            "id": 1,
            "name": "256 MiB Server",
        },
        "hostId": "e4d909c290d0fb1ca068ffaddf22cbd0",
        "status": "ACTIVE",
        "progress": 60,
        "addresses": {
            "public": [
                {
                    "version": 4,
                    "addr": "1.2.3.4",
                },
                {
                    "version": 4,
                    "addr": "5.6.7.8",
                }],
            "private": [{
                "version": 4,
                "addr": "10.11.12.13",
            }],
        },
        "metadata": {
            "Server Label": "Web Head 1",
            "Image Version": "2.1"
        },
        "OS-EXT-SRV-ATTR:host": "computenode1",
        "security_groups": [{
            'id': 1, 'name': 'securitygroup1',
            'description': 'FAKE_SECURITY_GROUP',
            'tenant_id': '4ffc664c198e435e9853f2538fbcd7a7'
        }],
        "OS-EXT-MOD:some_thing": "mod_some_thing_value",
        "console": {'console': {'url': 'http://0.0.0.0:6080/vnc_auto.html?token=4ac66b95-3dee-935d-8777-3433a3595ad5', 'type': 'novnc'}},
    }

    def __init__(self, manager = None, info = None, loaded=False, resp=None):
        super().__init__(manager = None, info = self.server_info, loaded=False, resp=None)

    def _setUp(self):   
        self.response = Response()
        self.response.status_code = 202
        self.return_value = TupleWithMeta((self.response, None), self.response)
        self.server_manager = ServerManager(MagicMock())  
        self.server = Server(manager=self.server_manager, info=self.server_info) 
        self.server_list = [self.server, self.server] 
    def list(self):
        self.server_manager.list = MagicMock(return_value=self.server_list)
        return self.server_manager.list()
    def start(self):
        self.start = MagicMock(return_value=self.return_value)
        if(self.status == 'SHUTOFF' or self.status == 'STOPPED'):
            self.status = "ACTIVE"
            return self.start()
        else:
            raise exceptions.Conflict(409)
    def stop(self):
        self.stop = MagicMock(return_value=self.return_value)
        if(self.status == 'ACTIVE' or self.status == 'SHUTOFF' or self.status == 'RESCUED'):
            self.status = "STOPPED"
            return self.stop()
        else:
            raise exceptions.Conflict(409)
    def reboot(self):
        self.reboot = MagicMock(return_value=self.return_value)
        if(self.status == 'ACTIVE' or self.status == 'SHUTOFF' or self.status == 'RESCUED'):
            self.status = "ACTIVE"
            return self.reboot()
        else:
            raise exceptions.Conflict(409)
    def delete(self):
        self.delete = MagicMock(return_value=self.return_value)
        if(self.status == 'ACTIVE' or self.status == 'SHUTOFF' or self.status == 'RESCUED' \
            or self.status == 'ERROR' or self.status == 'BUILDING'):
            self.status = "DELETED"
            return self.delete()
        else:
            raise exceptions.Conflict(409)
    def get_status(self):
        return self.status
    def get_vnc_console(self, console_type='novnc'):
        self.get_vnc_console = MagicMock(return_value=self.server._info['console'])
        return self.get_vnc_console()
    def get_console_output(self):
        self.get_console_output = MagicMock(return_value='Console-Output')
        return self.get_console_output()
    
