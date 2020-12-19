# -*- coding: utf-8 -*-
from odoo import http

# class MyModule(http.Controller):
#     @http.route('/external_product_updater/external_product_updater/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/external_product_updater/external_product_updater/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('external_product_updater.listing', {
#             'root': '/external_product_updater/external_product_updater',
#             'objects': http.request.env['external_product_updater.external_product_updater'].search([]),
#         })

#     @http.route('/external_product_updater/external_product_updater/objects/<model("external_product_updater.external_product_updater"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('external_product_updater.object', {
#             'object': obj
#         })