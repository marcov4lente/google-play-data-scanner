from web_adapter import WebAdapter

class TopApps(WebAdapter)

    data_src = 'https://play.google.com/store/apps/collection/topselling_free'
    data = None

    define scan():

        if not this.load_data():
            return false




