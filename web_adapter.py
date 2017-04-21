import urllib3
from bs4 import BeautifulSoup

class WebAdapter

    def load_data():
        urllib3.disable_warnings()
        http = urllib3.PoolManager()
        data = http.request('GET', this.data_src)

        try:
            assert data.status == 200
            this.status = data.status
            this.data = BeautifulSoup(data.data, 'html.parser')
            return True
        except AssertionError:
            return False



