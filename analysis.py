import operator

from collections import defaultdict

def top_tokens(n, filename):
  count = defaultdict(lambda: 0)
  with open(filename) as f:
    for word in f:
      count[word.strip()] += 1
  return sorted(count.iteritems(), key=operator.itemgetter(1), reverse=True)[:n]

def is_english(word):
  with open('/usr/share/dict/words') as dictionary:
    for english in dictionary:
      if english.strip() == word:
        return True
  return False

def potential_cognates(filename):
  id_tokens = set()
  overlap = set()
  with open(filename) as f:
    for word in f:
      id_tokens.add(word.strip().lower())
  with open('/usr/share/dict/words') as en:
    for word in en:
      if word.strip().lower() in id_tokens:
        overlap.add(word.strip().lower())
  return sorted(overlap)

def proper_nouns(filename):
  nouns = set()
  period = True
  with open(filename) as f:
    for word in f:
      word = word.strip()
      if word == '.':
        period = True
        continue
      if period:
        period = False
        continue
      if word[0].isupper():
        nouns.add(word)
  return sorted(nouns)

def proper_nonenglish_nouns(filename):
  nouns = set()
  period = True
  with open(filename) as f:
    for word in f:
      word = word.strip()
      if word == '.':
        period = True
        continue
      if period:
        period = False
        continue
      if word[0].isupper():
        nouns.add(word)
  with open('/usr/share/dict/words') as en:
    for word in en:
      if word.strip() in nouns:
        nouns.remove(word.strip())
  return sorted(nouns)

def words_like(regex, filename):
  import re
  words = set()
  with open(filename) as f:
    for word in f:
      if re.match(regex, word.strip(), flags=re.IGNORECASE):
        words.add(word.strip())
  return sorted(words)
