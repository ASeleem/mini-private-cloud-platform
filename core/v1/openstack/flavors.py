'''
OpenStack implementation for Flavors
'''

import zope.interface
from novaclient import client as noclient
import core.v1.abstract.cloud.flavors as AbstractCloud

@zope.interface.implementer(AbstractCloud.Flavors)
class OpenstackFlavors:
    ''' OpenStack implementation for Flavors '''
    def list(self, session):
        ''' List all flavors available for a user '''
        try:
            return noclient.Client(session=session, version='2.0').flavors.list()
        except Exception as exception:
            print("Cannot list the flavors:" + exception)
            return exception
    def get_id(self, flavor):
        ''' Retrun flavor id '''
        try:
            return flavor.id
        except Exception as exception:
            print("Cannot get flavor id:" + exception)
            return exception
    def get_vcpus(self, flavor):
        ''' Return flavor vcpus '''
        try:
            return flavor.vcpus
        except Exception as exception:
            print("Cannot get flavor vcpus:" + exception)
            return exception
    def get_ram(self, flavor):
        ''' Return flavor RAM '''
        try:
            return flavor.ram
        except Exception as exception:
            print("Cannot get the flavor ram:" + exception)
            return exception
    def get_disk(self, flavor):
        ''' Return flavor Disk space in GB '''
        try:
            return flavor.disk
        except Exception as exception:
            print("Cannot get the flavor disk:" + exception)
            return exception
    def get_ephemeral(self, flavor):
        ''' Return flavor Ephemeral Disk space in GB '''
        try:
            return flavor.ephemeral
        except Exception as exception:
            print("Cannot get the flavor ephemeral:" + exception)
            return exception
    def get_swap(self, flavor):
        ''' Return flavor Swap Disk space in MB '''
        try:
            if flavor.swap:
                return flavor.swap
            return '0'
        except Exception as exception:
            print("Cannot get the flavor swap:" + exception)
            return exception
    def get_rxtx_factor(self, flavor):
        ''' Return flavor RX/TX Factor '''
        try:
            return flavor.rxtx_factor
        except Exception as exception:
            print("Cannot get the rx/tx factor:" + exception)
            return exception
    def is_public(self, flavor):
        ''' Return if the flavor is public: Boolean '''
        try:
            return flavor.is_public
        except Exception as exception:
            print("Cannot check if the flavor is public:" + exception)
            return exception
    def create(self, session, name, ram, vcpus, disk,
               ephemeral=0, swap=0, rxtx_factor=1.0, is_public=True):
        ''' Create a Server '''
        try:
            return noclient.Client(session=session, version='2.0').flavors.create(
                name=name,
                ram=ram,
                vcpus=vcpus,
                disk=disk,
                ephemeral=ephemeral,
                swap=swap,
                rxtx_factor=rxtx_factor,
                is_public=is_public,
                )
        except Exception as exception:
            print("Cannot create a flavor:" + exception)
            return exception
    def delete(self, flavor):
        ''' Delete a Server '''
        try:
            return flavor.delete()
        except Exception as exception:
            print("Cannot delete the flavor:" + exception)
            return exception
