import pandas as pd
from spellchecker import SpellChecker

df = pd.read_csv("C:\\Users\\Franc\\OneDrive\\Documents\\words.csv")
df.head()
def spellcheckpossibles(word):
    return SpellChecker().candidates(word)

def spellcheckmostlikely(word):
    return SpellChecker().correction()

df.applymap(spellcheckpossibles)

df.applymap(spellcheckmostlikely)