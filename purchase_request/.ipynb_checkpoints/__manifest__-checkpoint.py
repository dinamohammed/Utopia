# -*- coding: utf-8 -*-
{
    'name': "purchase_request_field",

    'summary': """
        this module for customization egymentors_inverntory for update purchase_request field to read from
        hr department 
        """,

    'description': """
     this module for customization egymentors_inverntory for update purchase_request field to read from
        hr department 
    """,

    'author': "EgyMentors, Muhammed Ashraf",
    'website': "https://www.egymentors.com",
    'license': 'AGPL-3',
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Inventory',
    'version': '13.1',

    # any module necessary for this one to work correctly
    'depends': ['base','hr','stock','purchase_stock','purchase','egymentors_inventory'],

    # always loaded
    'data': [
        'views/views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}