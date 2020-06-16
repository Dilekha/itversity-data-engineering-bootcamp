import os
DB_DETAILS = {
    'DEV': {
        'SOURCE_DB' : {
            'DB_TYPE':'mysql',
            'DB_HOST':'34.94.114.182',
            'DB_PASS':os.environ.get('SOURCE_DB_PASS'),
            'DB_USER':os.environ.get('SOURCE_DB_USER'),
            'DB_NAME':'retail',
        },
        'TARGET_DB': {
            'DB_TYPE':'postgres',
            'DB_HOST':'34.94.114.182',
            'DB_NAME':'retail_dw',
            'DB_USER':os.environ.get('TARGET_DB_USER'),
            'DB_PASS':os.environ.get('TARGET_DB_PASS'),
        }
    }
}

