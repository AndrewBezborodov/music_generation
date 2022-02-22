from core.base_element import BaseElement

class Field(BaseElement):
    
    def __init__(self, name, field_type, default, session, parent):
        self.name = name
        self.field_type = field_type
        self.__value = None
        self.default = default
        # Create session
        super().__init__(session, parent)
        
    def set_value(self, value):
        self.__value = value
        
    def get_value(self):
        return self.__value if self.__value is not None else self.default

    def run():
        pass
    
    def __dict__(self):
        return {'id': self.id, 'name': self.name, 'field_type': self.field_type}
