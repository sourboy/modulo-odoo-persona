from odoo import models, fields
"""
1-Modelo de tipo de persona
-Campo char para indicar el tipo de persona
-Campo booleano para indicar si el registro está activo o no
"""
class TipoPersona(models.Model):
    _name = 'tipo.persona'
    _description = 'Se descrive los tipo de personas'

    type_person = fields.Char('Tipo de Persona')
    active = fields.Boolean('Activo')
    