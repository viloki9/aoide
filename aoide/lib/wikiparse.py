import wikipedia, nltk
from bs4 import BeautifulSoup
from .models import SynWord

KEY_NOUNS = ['NNP']

class WikiParse(object):
    def __init__(self, **kwargs):
        self.keyword = kwargs.get('keyword')
        self.obj = wikipedia.page(self.keyword)
        self.soup = BeautifulSoup(self.obj.html())

    #WARNING: making the assumption that all band pages will
    #have a info box and all relevant information will be
    #provided under the Background Information subheader
    def find_background_info(self):
        infoboxes = self.soup.findall(attr={'class','infobox'})
        background_found = False
        for infobox in infoboxes:
            tr_list = infobox.find_all('tr')
            for tr in tr_list:
                th = tr.find_all('th')
                data = {}
                if not th:
                    continue
                th_str = th[0].string
                if not background_found:
                    if th_str and th_str == 'Background Information':
                        background_found = True
                else:
                    td = tr.find_all('td')
                    td_str = td.string
                    if td_str:
                        data[th_str] = td_str
                    else:
                        alinks = td.find_all('a')
                        data[th_str] = ','.join(alinks)


    def find_inspiration(self):
        sentences = self.obj.content.split('.')
        syn_list = SynWord.objects.get(name='inspiration').synonym
        key_sentences = []
        for sentence in sentences:
            for syn_word in syn_list:
                if syn_word.name in sentence:
                    key_sentences.append(sentence)
        return key_sentences

    def connected_nodes(self):
        sentence = self.find_inspiration()
        parents = self.find_connections(sentence)
        print 'PARENTS: %s' % parents


    #going to make the initial assumption that wikipedia
    #articles rarely mentions whom the band influenced for
    #the sake of getting this to work and to sidestep
    #the complexities of determining the influencer in the
    #sentence.
    def find_connections(self, sentence):
        #parents = []
        tokens = nltk.word_tokenize(sentence)
        tagged = nltk.pos_tag(tokens)
        proper_nouns = [x for x, y in tagged if y in KEY_NOUNS]
        return proper_nouns



