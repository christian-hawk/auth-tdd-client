import clientapp

# import logging
 
# log = logging.getLogger(__name__)
# log.info('TESTINGl')

if __name__ == '__main__':
    app = clientapp.create_app()
    app.debug = True
    app.run(host='0.0.0.0', ssl_context=('cert.pem', 'key.pem'), port=443)