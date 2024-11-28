{
    'name': 'Sale Extended',
    'version': '16.1',
    'depends': ['mail', 'sale_management', 'sale'],
    'data': [
        'security/ir.model.access.csv',
        'data/sequence_view.xml',
        'wizard/sale_wizard_views.xml',
        'views/sale_order_views.xml',
        'views/teacher_views.xml',
    ],

    'demo':[
        'demo/demo_data_view.xml'
    ],
}
