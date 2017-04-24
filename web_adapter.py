import urllib3
from bs4 import BeautifulSoup

class WebAdapter:

    def load_data(self):
        urllib3.disable_warnings()
        http = urllib3.PoolManager()
        data = http.request('GET', self.data_src)

        try:
            assert data.status == 200
            self.status = data.status
            self.data = BeautifulSoup(data.data, 'html.parser')
            return True
        except AssertionError:
            return False



