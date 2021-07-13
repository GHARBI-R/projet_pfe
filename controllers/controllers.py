from odoo import http
from odoo.http import request


class Topnet(http.Controller):
     @http.route('/topnet/client/', auth='public' , website= True)
     def topnet_client (self, **kw):
         
         clients = request.env['topnet.clt'].sudo().search([])
         return request.render("Topnet.clients_page", {
            'clients': clients
        })


#     @http.route('/location_app/location_app/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('location_app.listing', {
#             'root': '/location_app/location_app',
#             'objects': http.request.env['location_app.location_app'].search([]),
#         })

#     @http.route('/location_app/location_app/objects/<model("location_app.location_app"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('location_app.object', {
#             'object': obj
#         })
