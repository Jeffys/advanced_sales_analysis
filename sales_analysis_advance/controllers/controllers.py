# -*- coding: utf-8 -*-
# from odoo import http


# class SalesAnalysisAdvance(http.Controller):
#     @http.route('/sales_analysis_advance/sales_analysis_advance', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sales_analysis_advance/sales_analysis_advance/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('sales_analysis_advance.listing', {
#             'root': '/sales_analysis_advance/sales_analysis_advance',
#             'objects': http.request.env['sales_analysis_advance.sales_analysis_advance'].search([]),
#         })

#     @http.route('/sales_analysis_advance/sales_analysis_advance/objects/<model("sales_analysis_advance.sales_analysis_advance"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sales_analysis_advance.object', {
#             'object': obj
#         })
