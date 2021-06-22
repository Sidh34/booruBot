import PARAMETERS
from saucenao_api import SauceNao, VideoSauce, BookSauce

S_N_K = PARAMETERS.SAUCE_NAO_TOKEN


class Sauce:
    def __init__(self, result):
        self.sim = result.similarity
        self.title = result.title
        self.url = result.urls[0]
        self.author = result.author
        if isinstance(result, VideoSauce):
            self.part = result.part
            self.time = result.est_time
        elif isinstance(result, BookSauce):
            self.part = result.part
        else:
            self.time = "placeholder"
            self.part = "placeholder"


def find_sauce(image):
    return Sauce(SauceNao(api_key=S_N_K).from_url(image)[0])
