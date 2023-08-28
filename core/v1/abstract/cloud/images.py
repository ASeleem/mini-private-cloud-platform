'''
Images Interface: interface defination for images behaviors
'''

import zope.interface

class Images(zope.interface.Interface):

    ''' Images Interface '''

    def get_name(self, auth, image):
        ''' Retrun image name '''
    def get_id(self, auth, image):
        ''' Retrun image id '''
    def list(self, auth):
        ''' List all images available for a user '''
    def get_disk_format(self, auth, image):
        ''' Return image disk format '''
    def get_min_ram(self, auth, image):
        ''' Return image min RAM '''
    def get_min_disk(self, auth, image):
        ''' Return image min Disk space in GB '''
    def get_protected(self, auth, image):
        ''' Return if the image is protected '''
    def get_visibility(self, auth, image):
        ''' Return image Visibility '''
    def get_updated_at(self, auth, image):
        ''' Return image update date '''
    def get_created_at(self, auth, image):
        ''' Return image creation date '''
    def get_status(self, auth, image):
        ''' Return image status '''
    def get_image_state(self, auth, image):
        ''' Return image state '''
    def get_image_type(self, auth, image):
        ''' Return image type '''
    def get_size(self, auth, image):
        ''' Return image size '''
