from odoo import fields, models
from odoo.exceptions import ValidationError


class Client(models.Model):
    _name = 'topnet.clt'
    _inherit = ['mail.thread.cc', 'mail.activity.mixin']
    _description = 'Client'
    _rec_name= 'npg'
     

    npg= fields.Char('Nom et prénom du gérant ', required= True)
    cin = fields.Integer('CIN / passeport ', required= True)
    raison= fields.Char('Raison sociale', required= True)
    registre  = fields.Char('Registre de commerce ', required= True)
    code_TVA = fields.Char ('Code_TVA', required= True)
    exonere= fields.Boolean('Exonere' ,required= True )
    code_douane = fields.Char('Code_douane', required= True)
    activite = fields.Char('Activite de l entreprise', required=True)
    adresse = fields.Text('Adresse' , required= True)
    ville  = fields.Integer('Ville' , required= True )
    code_postal = fields.Char('Code_postal' , required= True)
    tel = fields.Integer ('Tel' ,size=8 , required= True)
    faxe = fields.Integer('Faxe ', size=8)
    adr_ins= fields.Char('Adresse d installation', required= True )
    ville_ins = fields.Integer('Ville', required=True)
    code_postal_ins = fields.Integer('Code_postal', required=True)

    #contact_id= fields.One2many('topnet.contact','clt_id')


    email = fields.Char('Email principal' , required= True)
    type_offre= fields.Char("Type de l'offre", required= True )
    Debit= fields.Char('Débit ', required= True)


    active = fields.Boolean(default=True)



