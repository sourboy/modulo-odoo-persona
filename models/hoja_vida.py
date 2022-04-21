from odoo import models, fields

class HojaVida(models.Model):
    _name = 'hoja.vida'
    _description = 'Hoja de Vide del Personal'

    profession = fields.Char('Profesión')
    from_job = fields.Date('Trabajo Desde')
    until_job = fields.Date('Trabajo Hasta')
    job_sitio = fields.Selection([('national', 'Nacional'), ('international', 'Internacional')], 'Indique el Citio')
    person_id  = fields.Many2one('persona','Personas')
    
    