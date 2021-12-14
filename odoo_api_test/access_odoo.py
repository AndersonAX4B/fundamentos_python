import xmlrpc.client

url_sh = 'https://focvs-erp-artesp-odoo-homolog-3779491.dev.odoo.com'

db_sh = 'focvs-erp-artesp-odoo-homolog-3779491'
username_sh = 'admin'
password_sh = 'test_and_and_test'


def ambiente_default_test():
    """Teste para buscar informações do banco e do user 'admin'.
    Usado um ambiente padrão disponibilizado pelo próprio Odoo
    """

    info = xmlrpc.client.ServerProxy('https://demo.odoo.com/start').start()
    url, db, username, password = \
        info['host'], info['database'], info['user'], info['password']
    print(url, db, username, password)


def ambiente_sh_test():
    """Método testando a chamada de API dos serviços do Odoo da AX4B hospedado no SH
    """
    common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url_sh))
    print(common.version())

    uid = common.authenticate(db_sh, username_sh, password_sh, {})
    print(uid)

    models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url_sh))
    print(models)

    #  is used to call methods of odoo models via the execute_kw RPC function
    if models.execute_kw(db_sh, uid, password_sh,
                         'res.partner', 'check_access_rights',
                         ['read'], {'raise_exception': False}):
        # Records can be listed and filtered via search()
        models.execute_kw(db_sh, uid, password_sh,
                          'res.partner', 'search',
                          [[['is_company', '=', True]]])

        # Record data is accessible via the read() method
        ids = models.execute_kw(db_sh, uid, password_sh,
                                'res.partner', 'search',
                                [[['is_company', '=', True]]],
                                {'limit': 1})

        [record] = models.execute_kw(db_sh, uid, password_sh,
                                     'res.partner', 'read', [ids])
        # count the number of fields fetched by default
        print(len(record))

        # Picking only three fields deemed interesting.
        print(models.execute_kw(db_sh, uid, password_sh,
                                'res.partner', 'read',
                                [ids], {'fields': ['name', 'country_id', 'comment']}))


ambiente_sh_test()
