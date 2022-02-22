from core.objects.link import Link
from core.objects.links import Links
from core.objects.nodes.outputnode import OutPutNode
from core.objects.nodes.inputnode import InputNode
from core.objects.nodes.inputnode_midi import InputNodeMidi
from core.objects.nodes.sqrnode import SqrNode
from core.objects.nodes.button_midi2freq import ButtonMidi2Freq
from core.objects.field import Field
import pandas as pd


class Session:
    def __init__(self):
        self.objects = {}
        self.parents = {}
        self.i = 0
        self.links = Links()

        self.type_node2class = {
            cls.__name__: cls for cls in [InputNode, SqrNode, OutPutNode]
        }

        self.stats = [{}]

    def add_link(self, link):
        self.links.add_link(link)

    def add_object(self, element):
        self.i += 1
        self.objects[self.i] = element
        return self.i

    def add_node(self, node_type):
        element = self.type_node2class[node_type](self)
        return element.id

    def write2file(self):
        print('WRITE TO FILE')
        pd.DataFrame.from_records(self.stats).to_csv('statistic/first.csv', index=False)
        print('WRITE TO FILE')
