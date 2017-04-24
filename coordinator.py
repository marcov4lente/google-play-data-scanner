from top_apps import TopApps

class CoOrdinator:

    def __init__(self):
        self.farms = {
            'Top Apps': TopApps
        }

    def farm(self):

        for key, farm in self.farms.items():
            print('Harvesting '+key)
            farm = farm()
            farm.harvest()
            print('Harvesting '+key+' complete.')


