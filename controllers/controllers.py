# -*- coding: utf-8 -*-
# from odoo import http


# class AaPrueba(http.Controller):
#     @http.route('/aa_prueba/aa_prueba', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/aa_prueba/aa_prueba/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('aa_prueba.listing', {
#             'root': '/aa_prueba/aa_prueba',
#             'objects': http.request.env['aa_prueba.aa_prueba'].search([]),
#         })

#     @http.route('/aa_prueba/aa_prueba/objects/<model("aa_prueba.aa_prueba"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('aa_prueba.object', {
#             'object': obj
#         })
