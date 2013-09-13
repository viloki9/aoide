import wikipedia, nltk
from .models import SynWord

class WikiParse(object):
    def __init__(self, **kwargs):
        self.keyword = kwargs.get('keyword')
        self.obj = wikipedia.page(self.keyword)

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
        parents, children = self.find_connections(sentence)
        print 'PARENTS: %s' % parents
        print 'CHILDREN: %s' % children

    def find_connections(self, sentence):
        parents, children = [], []
        tokens = nltk.word_tokenize(sentence)
        tagged = nltk.pos_tag(tokens)
        return parents, children



