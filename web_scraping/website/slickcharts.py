from bs4 import BeautifulSoup
from datetime import datetime
from ..driver.chrome_driver import Driver


class Slickcharts:
    def __init__(self, base_url=None, indice=None, indice_ids=None):
        self.base_url = base_url or "https://www.slickcharts.com"
        self.indice = indice or ["/sp500", "/nasdaq100", "/dowjones"]
        self.indice_ids = indice_ids or ["GSPC", "NDX", "DJI"]

    def get_index_components(self):
        fmt = lambda s: s.find_element_by_tag_name("tbody").is_displayed()
        with Driver() as d:
            return [
                {
                    "symbol": self.indice_ids[i],
                    "components": self.get_components(d.get_page_source(self.base_url + ind, fmt)),
                }
                for i, ind in enumerate(self.indice)
            ]

    @staticmethod
    def get_components(markup):
        soup = BeautifulSoup(markup, "lxml")
        tbody = soup.find("tbody")
        return [tr.find_all("td")[2].get_text() for tr in tbody.find_all("tr")]
