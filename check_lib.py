try:
    from khmernltk import word_tokenize
    print("khmer-nltk is installed")
except ImportError:
    print("khmer-nltk is NOT installed")
