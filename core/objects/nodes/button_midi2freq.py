from core.base_element import BaseElement
from core.objects.field import Field

from const.field_constants import *
from const.all import *

import time


class ButtonMidi2Freq(BaseElement):
    __name__ = 'ButtonMidi2Freq'
    
    def __init__(self, session):

        super().__init__(session, None)
        
        self.setting_tone = 20
        self.fields = {
            'buttons_pushed': Field('buttons_pushed',DICT, {}, session, self),
            
        }
        self.out_fields = {
            'freq_pushed' : Field('freq_pushed', DICT, {}, session, self)
        }

    # 69 button - 440 GZ
    def button_pushed(self, note):
        return 440 * 2 ** ((note - 69) / 12)

    def run(self):
        buttons_pushed = self.get_field_value('buttons_pushed')
        print(buttons_pushed.keys())
        freq_pushed = {
            self.button_pushed(key) : value
            for key, value in buttons_pushed.items()
        }
        print(freq_pushed.keys())
        self.set_out_field_value('freq_pushed', freq_pushed)
        

