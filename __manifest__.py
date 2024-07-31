# -*- coding: utf-8 -*-
{
    'name': "Advanced Sales Analysis",

    'summary': """
        This custom Odoo module enhances the Sales Analysis report by providing additional financial insights. It introduces three key metrics to give a more detailed view of the sales pipeline and cash flow status.
    """,

    'description': """
        This custom Odoo module enhances the Sales Analysis report by providing additional financial insights. It introduces three key metrics to give a more detailed view of the sales pipeline and cash flow status.
    """,

    'author': "Doodex",
    'website': "https://www.doodex.net/",

    'category': 'Sales',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','sale','account','sale_management'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
    ],

}
