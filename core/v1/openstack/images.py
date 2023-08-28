'''
OpenStack implementation for Images
'''

import zope.interface
from novaclient import client as noclient
import core.v1.abstract.cloud.images as AbstractCloud

@zope.interface.implementer(AbstractCloud.Images)
class OpenstackImages:
    ''' OpenStack implementation for Images '''
    def get_name(self, image):
        ''' Retrun image name '''
        try:
            return image.name
        except Exception as exception:
            print("Cannot get the image name:" + exception)
            return exception
    def get_id(self, image):
        ''' Retrun image id '''
        try:
            return image.id
        except Exception as exception:
            print("Cannot get the image id:" + exception)
            return exception
    def list(self, session):
        ''' List all images available for a user '''
        try:
            return noclient.Client(session=session, version='2.0').glance.list()
        except Exception as exception:
            print("Cannot list the images:" + exception)
            return exception
    def get_disk_format(self, image):
        ''' Return image disk format '''
        try:
            return image.disk_format
        except Exception as exception:
            print("Cannot get the disk format:" + exception)
            return exception
    def get_min_ram(self, image):
        ''' Return image min RAM '''
        try:
            return image.min_ram
        except Exception as exception:
            print("Cannot get the image min ram:" + exception)
            return exception
    def get_min_disk(self, image):
        ''' Return image min Disk space in GB '''
        try:
            return image.min_disk
        except Exception as exception:
            print("Cannot get the min disk:" + exception)
            return exception
    def get_protected(self, image):
        ''' Return if the image is protected '''
        try:
            return image.protected
        except Exception as exception:
            print("Cannot check if the image protected:" + exception)
            return exception
    def get_visibility(self, image):
        ''' Return image Visibility '''
        try:
            return image.visibility
        except Exception as exception:
            print("Cannot check if the image visibile:" + exception)
            return exception
    def get_updated_at(self, image):
        ''' Return image updated date '''
        try:
            return image.updated_at
        except Exception as exception:
            print("Cannot get the image update date:" + exception)
            return exception
    def get_created_at(self, image):
        ''' Return image create date '''
        try:
            return image.created_at
        except Exception as exception:
            print("Cannot the image creation date:" + exception)
            return exception
    def get_status(self, image):
        ''' Return image status '''
        try:
            return image.status
        except Exception as exception:
            print("Cannot get the image status:" + exception)
            return exception
    def get_image_state(self, image):
        ''' Return image state '''
        try:
            return image.image_state
        except Exception as exception:
            print("Cannot get the image state:" + exception)
            return exception
    def get_image_type(self, image):
        ''' Return image type '''
        try:
            return image.image_type
        except Exception as exception:
            print("Cannot the image type:" + exception)
            return exception
    def get_size(self, image):
        ''' Return image size '''
        try:
            return image.size
        except Exception as exception:
            print("Cannot the image size:" + exception)
            return exception
