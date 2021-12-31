{
    'name': "Odoo FE test",
    'version': "15.0.0.1",
    'summary': "Odoo FE test",
    'description': "Odoo FE test",
    'author': "Ed Chu",
    'website': "https://lumirang.com",
    'category': "Website",
    'license': "Other proprietary",
    'depends': ['contacts', 'website'],
    'data': [
    ],
    'assets': {
        'web.assets_qweb': [
            'fe_test/static/src/xml/qweb.xml',
        ],
        'web.assets_backend': [
            'fe_test/static/src/js/be_script.js',
        ],
        "web.assets_frontend": [
            'fe_test/static/src/js/fe_script.js',
        ],
    },
    'installable': True,
    'application': True,
    'auto_install': False,
}
