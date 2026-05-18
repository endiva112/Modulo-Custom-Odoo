# -*- coding: utf-8 -*-
# from odoo import http


# class VetClinic(http.Controller):
#     @http.route('/vet_clinic/vet_clinic', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/vet_clinic/vet_clinic/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('vet_clinic.listing', {
#             'root': '/vet_clinic/vet_clinic',
#             'objects': http.request.env['vet_clinic.vet_clinic'].search([]),
#         })

#     @http.route('/vet_clinic/vet_clinic/objects/<model("vet_clinic.vet_clinic"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('vet_clinic.object', {
#             'object': obj
#         })

