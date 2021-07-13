{
'name': ' Gestion des dossiers clients  ',
'description': ' Gérer les dossiers clients  ',
'author': 'GHARBI Rima',
'website': 'www.topnet.tn',
'depends': ['base','website','sale', 'mail','crm'],

'data': [
   'security/ir.model.access.csv',
   'views/client.xml',
   'views/templates.xml'
       ],

'images': ['static/description/logo-topnet.png'],

'installable': True,
'application': True,
'auto_install': False,       
}
