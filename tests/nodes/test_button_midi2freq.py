from core.session import *
from core.objects.nodes.button_midi2freq import ButtonMidi2Freq

import unittest

class TestStringMethods(unittest.TestCase):
    
    def __init__(self, *args, **kwargs):
        self.session = Session()
        self.button_midi2freq = ButtonMidi2Freq(self.session)
        self.button_midi2freq.setting_tone = 10
        
        
        super(TestStringMethods, self).__init__(*args, **kwargs)

    def test_generate_freq_pushed(self):
        
        self.button_midi2freq.set_field_value(
            self.button_midi2freq.fields['buttons_pushed'], {22:1, 34:1})
        self.button_midi2freq.run()
        self.assertEqual(
            self.button_midi2freq.out_fields['freq_pushed'].get_value(),
            {20.0:1, 40.0:1}
        )





