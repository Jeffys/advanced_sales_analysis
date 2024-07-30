# -*- coding: utf-8 -*-
{
    'name': "advanced_sales_analysis",

    'summary': """
        This custom Odoo module enhances the Sales Analysis report by providing additional financial insights. It introduces three key metrics to give a more detailed view of the sales pipeline and cash flow status.
    """,

    'description': """
        This custom Odoo module enhances the Sales Analysis report by providing additional financial insights. It introduces three key metrics to give a more detailed view of the sales pipeline and cash flow status.
    """,

    'author': "Doodex",
    'website': "https://www.doodex.net/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Sales',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','sale','account'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
    ],

}
