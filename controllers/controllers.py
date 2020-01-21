# -*- coding: utf-8 -*-
from odoo import http

# class /home/mymodules/cstSendEmail(http.Controller):
#     @http.route('//home/mymodules/cst_send_email//home/mymodules/cst_send_email/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('//home/mymodules/cst_send_email//home/mymodules/cst_send_email/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('/home/mymodules/cst_send_email.listing', {
#             'root': '//home/mymodules/cst_send_email//home/mymodules/cst_send_email',
#             'objects': http.request.env['/home/mymodules/cst_send_email./home/mymodules/cst_send_email'].search([]),
#         })

#     @http.route('//home/mymodules/cst_send_email//home/mymodules/cst_send_email/objects/<model("/home/mymodules/cst_send_email./home/mymodules/cst_send_email"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('/home/mymodules/cst_send_email.object', {
#             'object': obj
#         })