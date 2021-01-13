from .website.slickcharts import Slickcharts
from pymongo import MongoClient

client = MongoClient()
db = client.capiDB


def run():
    sc = Slickcharts()
    indice_comps = sc.get_index_components()
    db.index.components.insert_many(indice_comps)