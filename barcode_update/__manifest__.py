# -*- coding: utf-8 -*-
{
    'name': "barcode_update",

    'summary': """
       Update Barcode view for delete display name of product 
       """,

    'description': """
       Update Barcode view for delete display name of product 
    """,

    'author': "EgyMentors@MuhammedAhsraf",
    'website': "https://www.egymentors.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Inventory',
    'version': '13.0',

    # any module necessary for this one to work correctly
    'depends': ['base','stock','product','sale','delivery', 'purchase'],

    # always loaded
    'data': [
        'views/barcode_update_view.xml',
    ],
    # only loaded in demonstration mode
    'installable': True,
    'application': True,
    'auto_install': False,
}
