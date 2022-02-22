from core.base_element import BaseElement
from core.objects.field import Field

from const.field_constants import *


class InputNode(BaseElement):
    __name__ = 'InputNode'
    
    def __init__(self, session, device_name):

        
        super().__init__(session, None)
        
        self.fields = {
            'device_name': Field('device_name',TEXT, '', session, self)
        }
        self.out_fields = {
            'freq' : Field('freq', VECTOR, 5, session, self), 
            'output' : Field('output', VECTOR, 0, session, self)
        }
        
    def run(self):
        # Пока костыль я виде одной ноты
        return 5
