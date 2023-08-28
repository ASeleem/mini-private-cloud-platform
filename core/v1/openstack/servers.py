'''
OpenStack implementation for Servers
'''

import zope.interface
from novaclient import client as noclient
from novaclient.v2.servers import Server
import core.v1.abstract.cloud.servers as AbstractCloud
from novaclient import exceptions as novaExceptions
from core.v1 import exceptions as exceptions

@zope.interface.implementer(AbstractCloud.Servers)
class OpenstackServer:
    ''' OpenStack implementation for Servers '''

    server = None
    client = None

    def __init__(self, server: Server, client: noclient.Client = None):
        if client:
            self.client = client
        self.server = server

    def list(self, client: noclient.Client = None):
        ''' OpenStack implementation for listing Servers '''
        if client:
            self.client = client
        try:
            server_list = self.client.servers.list()
            openstack_server_list = [ OpenstackServer(server) for server in server_list ]
            return openstack_server_list
        except Exception:
            return exceptions.GeneralException
    def stop(self):
        ''' OpenStack implementation for stopping a server '''
        try:
            return self.server.stop()
        except novaExceptions.Conflict:
            return exceptions.Conflict(409)
        except Exception:
            return exceptions.GeneralException
            
    def start(self):
        ''' OpenStack implementation for starting a server '''
        try:
            return self.server.start()
        except novaExceptions.Conflict:
            return exceptions.Conflict(409)
        except Exception:
            return exceptions.GeneralException
    def reboot(self):
        ''' OpenStack implementation for rebooting a server '''
        try:
            return self.server.reboot()
        except novaExceptions.Conflict:
            return exceptions.Conflict(409)
        except Exception:
            return exceptions.GeneralException
    def delete(self):
        ''' OpenStack implementation for deleting a server '''
        try:
            return self.server.delete()
        except novaExceptions.Conflict:
            return exceptions.Conflict(409)
        except Exception:
            return exceptions.GeneralException
    def get_status(self):
        ''' OpenStack implementation for getting the server status'''
        try:
            return self.server.status
        except novaExceptions.ResourceInErrorState:
            return exceptions.ResourceInErrorState(self.server)
        except Exception:
            return exceptions.GeneralException
    def get_vnc_console(self, console_type='novnc'):
        ''' OpenStack implementation for getting the server VNC Console '''
        try:
            return self.server.get_vnc_console(console_type)
        except novaExceptions.UnsupportedConsoleType:
            return exceptions.UnsupportedConsoleType(console_type)
        except Exception:
            return exceptions.GeneralException
    def get_console_output(self):
        ''' OpenStack implementation for getting the VNC Console Output '''
        try:
            return self.server.get_console_output()
        except Exception:
            return exceptions.GeneralException