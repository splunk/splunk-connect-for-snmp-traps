class HecConfiguration:
    def __init__(self, hec_config):
        self._protocol = hec_config['protocol']
        self._host = hec_config['host']
        self._port = hec_config['port']
        self._endpoint = hec_config['endpoint']
        self._authentication_token = hec_config['authentication_token']

    def endpoint(self):
        from urllib.parse import urlunsplit
        base_url = f'{self._host}:{self._port}'
        return urlunsplit((self._protocol, base_url, self._endpoint, '', ''))

    def authentication_token(self):
        return self._authentication_token
