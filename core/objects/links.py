
class Links():
    def __init__(self):
        self.links = []
        self.element_in2elements_out = {}
        self.element_out2element_in_fields = {}
        
    def add_link(self, link):
        self.links.append(link)
        self.element_in2elements_out[link.element_in] = link.element_out
        
        if link.element_out not in self.element_out2element_in_fields:
            self.element_out2element_in_fields[link.element_out] = [link.element_in]
        else:
            self.element_out2element_in_fields[link.element_out].append(link.element_in)
        
        

    def remove_link(self, link):
        remove_index = self.links.index(link)
        print('BAD INDEX')
        self.links.pop(remove_index)
        
        self.element_in2elements_out.pop(link.element_in)
        index = self.element_out2element_in_fields[link.element_out].index(link.element_in)
        return self.element_out2element_in_fields[link.element_out].pop(index)
        
    def __dict__(self):
        return list(map(lambda link: link.__dict__(), self.links))

        