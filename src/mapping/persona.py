
from py_sqlo.src.entity_options.mapping import Mapping

class PersonaMapping(Mapping):

    def primer_nombre_apellido(self):
        return "CONCAT_WS(' ', SUBSTRING_INDEX("+self.pt()+".nombres , ' ', 1 ), SUBSTRING_INDEX("+self.pt()+""".apellidos , ' ', 1 )
)"""

    def primer_nombre_apellido(self):
        return "CONCAT_WS(' ', SUBSTRING_INDEX("+self.pt()+".apellidos , ' ', 1 ), SUBSTRING_INDEX("+self.pt()+""".nombres , ' ', 1 )      
)"""
