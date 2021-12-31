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
            '/static/src/**/base_import.xml',
        ],
        'web.assets_backend': [
            '/static/src/**/*.js',
        ],
    },
    'installable': True,
    'application': True,
    'auto_install': False,
}
