'''
Servers Interface: interface defination for flavor behaviors
'''

import zope.interface

class Flavors(zope.interface.Interface):

    ''' Flavors Interface '''

    def get_id(self, auth, flavor):
        ''' Retrun flavor id '''
    def list(self, auth):
        ''' List all flavors available for a user '''
    def get_vcpus(self, auth, flavor):
        ''' Return flavor vcpus '''
    def get_ram(self, auth, flavor):
        ''' Return flavor RAM '''
    def get_disk(self, auth, flavor):
        ''' Return flavor Disk space in GB '''
    def get_ephemeral(self, auth, flavor):
        ''' Return flavor Ephemeral Disk space in GB '''
    def get_swap(self, auth, flavor):
        ''' Return flavor Swap Disk space in MB '''
    def get_rxtx_factor(self, auth, flavor):
        ''' Return flavor RX/TX Factor '''
    def is_public(self, auth, flavor):
        ''' Return if the flavor is public: Boolean '''
    def create(self, auth, name, ram, vcpus, disk, ephemeral, swap, rxtx_factor, is_public):
        ''' Create a Server '''
    def delete(self, auth, flavor):
        ''' Delete a Server '''
