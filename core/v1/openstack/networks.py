'''
OpenStack implementation for Networks
'''

import zope.interface
from neutronclient.v2_0 import client as neuclient
import core.v1.abstract.cloud.networks as AbstractCloud

@zope.interface.implementer(AbstractCloud.NetworkManager)
class OpenstackNetworkManager:
    ''' OpenStack implementation for NetworkManager '''
    def list_networks(self, session):
        ''' List all networks owned by a user or can user access '''
        try:
            return neuclient.Client(session=session).list_networks()['networks']
        except Exception as exception:
            print("Cannot list the servers:" + exception)
            return exception
