#!/usr/bin/env python
"""
pip install urllib3
pip install bs4

"""
from coordinator import CoOrdinator

coordinator = CoOrdinator()
coordinator.farm()

# print('Harvesting top apps')
# if not top_apps.harvest:
#     print('Error harvesting top apps')
# else:
#     print('Harvesting top apps complete')
