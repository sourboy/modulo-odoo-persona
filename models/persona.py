from odoo import models, fields

class Persona(models.Model):
    _name = 'persona'
    _description = 'Persona'

    name = fields.Char('Nombre')
    active = fields.Boolean('Activo')
    lastname = fields.Char('Apellido')
    age = fields.Integer('Edad')
    address = fields.Text('Dirección')
    email = fields.Char('Correo')
    phone = fields.Char('Teléfono')
    birthdate = fields.Date('Fecha de nacimiento')
    photo = fields.Binary('Foto')
    gender = fields.Selection([('male', 'Masculino'), ('female', 'Femenino')], 'Género')
    sheelife_ids = fields.One2many('hoja.vida', 'person_id', 'Hoja de vida') 
    type_person_id  = fields.Many2one('tipo.persona', 'Tipo de Persona')