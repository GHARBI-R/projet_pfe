from odoo import fields, models

class Gouvernorat(models.Model):
    _name = 'topnet.gouvernorat'
    _description = 'gouvernorat'

    nom = fields.Char('nom gouvernorat  ', required=True)
    ville_id = fields.One2many('topnet.ville', 'gouv_id')