from odoo import fields, models

class Ville(models.Model):
    _name = 'topnet.ville'
    _description = 'ville'

    nom = fields.Char('nom ville  ', required=True)
    code_p = fields.Integer('code postale ', required=True)
    gouv_id= fields.Many2one ('topnet.gouvernorat' )
