# -*- coding: utf-8 -*-
# from odoo import http


# class Temple(http.Controller):
#     @http.route('/temple/temple', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/temple/temple/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('temple.listing', {
#             'root': '/temple/temple',
#             'objects': http.request.env['temple.temple'].search([]),
#         })

#     @http.route('/temple/temple/objects/<model("temple.temple"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('temple.object', {
#             'object': obj
#         })

