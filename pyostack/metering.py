import ceilometerclient.client as clclient
import logging
log = logging.getLogger(__name__)


class Metering:
    '''Wrapper for the OpenStack MEtering service (Ceilometer)'''
    def __init__(self, conf):
        creds = self._get_creds(conf)
        self.ceilo = clclient.get_client(2, **creds)

    def _get_creds(self, conf):
        d = {}
        d['username'] = conf.get("environment", "OS_USERNAME")
        d['api_key'] = conf.get("environment", "OS_PASSWORD")
        d['auth_url'] = conf.get("environment", "OS_AUTH_URL")
        d['project_id'] = conf.get("environment", "OS_TENANT_NAME")
        return d

    def meter_list(self, query):
        return self.ceilo.meters.list()

