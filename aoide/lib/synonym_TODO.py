from aoide.lib.models import SynBase, SynWord

def create_synonym(txtword, root=None):
    if root:
        syn = SynWord()
    else:
        syn = SynBase()
    syn.name = txtword
    if root:
        syn.synonym_root = root
    syn.save()
    return syn

def run_inspiration():
    word_list = ['inspiration', 'borrow', 'influence']
    rootword = create_synonym('inspire')
    for word in word_list:
        word_obj = create_synonym(word, rootword)




