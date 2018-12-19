{ 
    'name': "Automated Rate", 
    'summary': "Banguat automated rate", 
    'description': """Retreives Banguat daily Dollar rate and adds it to the currency rate""", 
    'author': "Pitaya Tech", 
    'license': "AGPL-3", 
    'website': "http://www.pitaya.tech", 
    'category': 'Uncategorized', 
    'version': '12.0.1.0.0',
    'data': [
	    'data/automated_rate_data.xml',
        'security/ir.model.access.csv',
    ],
    'depends': ['base'],
}