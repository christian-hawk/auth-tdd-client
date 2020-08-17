
from flask_oidc import registration, discovery
import json
from httplib2 import RelativeURIError

class ClientHandler:
    __client_url = None
    __client_id = None
    __client_secret = None
    __metadata_url= None
    __op_url = None

    def __init__(self, op_url: str, client_url: str):
        """[intializes]

        :param op_url: [url from oidc provider starting with https]
        :type op_url: str
        :param client_url: [url from client starting with https]
        :type client_url: str
        """
        self.__op_url = op_url
        self.__client_url = client_url
        self.__metadata_url = '%s/.well-known/openid-configuration' % op_url

    def get_client_dict(self) -> dict:
        r = {
            'op_metadata_url' : self.__metadata_url,
            'client_id' : 'None',
            'client_secret' : 'None'
        }

        return r


    def register_client(self, op_data: dict, client_url: str) -> dict:
        """[register client and returns client information]

        :param op_data: [description]
        :type op_data: dict
        :param client_url: [description]
        :type client_url: str
        :return: [client information including client-id and secret]
        :rtype: dict
        """
        redirect_uri = '%s/oidc_callback' % client_url
        reg_info = registration.register_client(op_data, [redirect_uri])
        return reg_info

    def discover(self, op_url: str, disc:discovery=discovery) -> dict :
        """Discover op information on .well-known/open-id-configuration
        :param op_url: [url from OP]
        :type op_url: str
        :param discovery: [flask_oidc.discovery injection], defaults to discovery
        :type discovery: discovery, optional
        :return: [data retrieved from OP url]
        :rtype: dict3
        """
        op_data = {}
        try:
            op_data = disc.discover_OP_information(op_url)
            print(op_data)
            return op_data

        except json.JSONDecodeError as err:
            print('Error trying to decode JSON: %s' % err)

        except RelativeURIError as err:
            print(err)

        except Exception as e:
            print('An unexpected ocurred: %s' % e)

        return op_data

