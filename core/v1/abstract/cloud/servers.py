'''
Servers Interface: interface defination for server behaviors
'''

import zope.interface

class Servers(zope.interface.Interface):

    ''' Servers Interface '''

    def get_info(self, auth, server):
        ''' Retrun server informations '''
    def list(self, auth):
        ''' List all servers owned by a user '''
    def get_vnc_console(self, auth, server, console_type):
        ''' Return VNC Console URL '''
    def stop(self, auth, server):
        ''' Stop a Server '''
    def start(self, auth, server):
        ''' Start a Server '''
    def reboot(self, auth, server):
        ''' Restart a Server '''
    def create(self, auth, name, image, flavor, *options):
        ''' Create a Server '''
    def delete(self, auth, server):
        ''' Delete a Server '''
