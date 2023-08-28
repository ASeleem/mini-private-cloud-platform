'''
Networks Interface: interface defination for network behaviors
'''

import zope.interface

class NetworkManager(zope.interface.Interface):

    ''' NetworkManager Interface '''
    def list_networks(self, auth):
        ''' List all networks owned by a user or can user access '''
    # TODO: Complete NetworkManager Interface

class Network(zope.interface.Interface):
    ''' Network Interface '''
    # TODO: Network Definition

class Subnet(zope.interface.Interface):
    ''' Subnet Interface '''
    # TODO: Subnet Definition
class Router(zope.interface.Interface):
    ''' Router Interface '''
    # TODO: Router Definition
