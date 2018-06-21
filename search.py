import math

class VectorCompare:
  def __init__(self, documents):
    if type(documents) != dict:
      raise ValueError('Argument must be a dictionary')

    self.wordVectors = {}
    self.documents = documents

    for pos, item in documents.items():
      self.wordVectors[pos] = self.vector(item.lower())

  def magnitudeOfVector(self, vector):
    if type(vector) != dict:
      raise ValueError('Argument must be a dictionary')

    total = 0
    for _, wordOccurences in vector.items():
      total += wordOccurences ** 2

    return math.sqrt(total)

  def relation(self, vector1, vector2):
    if type(vector1) != dict:
      raise ValueError('Argument1 must be a dictionary')

    if type(vector2) != dict:
      raise ValueError('Argument2 must be a dictionary')

    topValue = 0
    for word, wordOccurences in vector1.items():
      if word in vector2:
        topValue += wordOccurences * vector2[word]

    magnitudeOfVectors = self.magnitudeOfVector(vector1) * self.magnitudeOfVector(vector2)

    if magnitudeOfVectors == 0:
      return 0
    
    return topValue / magnitudeOfVectors


  def vector(self, document):
    if type(document) != str:
      raise ValueError('Argument must be a String')

    vector = {}
    for word in document.split(' '):
      if word in vector:
        vector[word] += 1
      else: 
        vector[word] = 1

    return vector


  def match(self, searchTerm):
    vectorizedSearchTerm = v.vector(searchTerm.lower())

    matches = []
    for i in range(len(self.wordVectors)):
      relation = v.relation(vectorizedSearchTerm, self.wordVectors[i])
      
      if relation != 0:
        matches.append((relation, self.documents[i]))

    matches.reverse()

    return matches

documents = {
  0: 'With data growing at an exponential rate, perceived to be over 150 ZB of data available by 2025, it is now recognized that we need to prioritize bringing processing to data versus relying on data movement through Internet bandwidth that is growing at a much slower pace.',
  1: 'Microsoft Research Open Data is an outcome of the Microsoft Research Outreach Data science program and was made possible by a collaboration between many teams at Microsoft, Microsoft researchers, our industry partners, and our academic advisors.',
  2: 'We would love to hear your comments and feedback! Please send us a note via the Feedback feature on the site http://microsoftopendata.com and tell us what you think.',
  3: 'To the extent possible, the repository meets the highest standards for data sharing to ensure that datasets are findable, accessible, interoperable and reusable; the entire corpus does not contain personally identifiable information.',
  4: 'You can browse available datasets and download them or copy them directly to an Azure subscription through an automated workflow.',
}

v = VectorCompare(documents)

searchTerm = input('Enter Search Term: ')

matches = v.match(searchTerm)

for match in matches:
  print(match)