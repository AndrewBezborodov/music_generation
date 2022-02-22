from core.session import *
from core.objects.nodes.inputnode_midi import InputNodeMidi

import unittest

class TestStringMethods(unittest.TestCase):
    
    def __init__(self, *args, **kwargs):
        self.session = Session()
        self.input_node_midi = InputNodeMidi(self.session)
        
        
        super(TestStringMethods, self).__init__(*args, **kwargs)

"""    def test_add_new_element(self):
        self.input_node_midi.run_record([9,0,15,0])
        self.assertEqual(
            list(self.input_node_midi.out_fields['buttons_pushed'].get_value().keys()),[15]
        )
        
    def test_delete_exist_element(self):
        self.input_node_midi.run_record([8,0,15,0])
        self.assertEqual(
            len(self.input_node_midi.out_fields['buttons_pushed'].get_value()),0
        )
        
    def test_many_notes(self):
        self.input_node_midi.run_record([9,0,1,0, 9,0,2,0, 9,0,3,0])
        self.assertEqual(
            list(self.input_node_midi.out_fields['buttons_pushed'].get_value().keys()),
            [1,2,3]
        )
"""


