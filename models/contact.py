from odoo import fields, models

class TopnetContact(models.Model):
    _name = 'topnet.contact'
    _description = 'contact'

    np = fields.Char('nom et prénom', required=True)
    tel = fields.Integer('telelephone', size=8, required=True)
    gsm = fields.Integer('gsm ', size=8, required=True)
    email = fields.Char('email ', required=True)
    nature = fields.Selection ([('financier','financier'),('commercial','commercial'),('administratif','administratif'),('technique','technique')])
