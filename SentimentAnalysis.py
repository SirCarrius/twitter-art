#later we will read these from a JSON file
import nltk
import Image

def get_words_in_tweets(tweets):
	all_words = []
	for (words, sentiment) in tweets:
		all_words.extend(words)
	return all_words

def get_word_features(wordlist):
	wordlist = nltk.FreqDist(wordlist)
	word_features = wordlist.keys()
	return word_features

def extract_features(document):
    document_words = set(document)
    features = {}
    for word in word_features:
        features['contains(%s)' % word] = (word in document_words)
    return features

pos_tweets = [('I love this car', 'positive'),
              ('This view is amazing', 'positive'),
              ('I feel great this morning', 'positive'),
              ('I am so excited about the concert', 'positive'),
              ('He is my best friend', 'positive'),
              ('A dream is the bearer of new possibility, the enlarged horizon, the great hope', 'positive'),
              ('I am exquisite', 'positive'),
              ('Stop being afraid of what could go wrong and start being positive about what could go right', 'positive'),
              ('I am healthy', 'positive'),
              ('I am good', 'positive'),
              ('I am intelligent', 'positive'),
              ('I am lucky', 'positive'),
              ('Life is crazy man, do not waste a second of it', 'positive'),
              ('You create your own future by your thoughts and actions', 'positive'),
              ('I believe this is a sign of greater things to come', 'positive'),
              ('Always looking forward to what the future holds for me', 'positive'),
              ('Good will always come', 'positive'),
              ('Another positive, fun day! It is a choice', 'positive'),
              ('Remember when your down. The only way to go is back up. So think #positive. Stay #healthy', 'positive'),
              ('I am wondrous', 'positive'),
              ('I feel happy', 'positive'),
              ('You are nice', 'positive')]



neg_tweets = [('I do not like this car', 'negative'),
              ('This view is horrible', 'negative'),
              ('I feel tired this morning', 'negative'),
              ('I am not looking forward to the concert', 'negative'),
              ('He is my enemy', 'negative'),
              ('I feel terrible', 'negative'),
              ('I am shit man', 'negative'),
              ('Fuck exams', 'negative'),
              ('Sometimes I just dont understand people', 'negative'),
              ('I hate the clergy for telling the congregation to avoid a necessary social revolution', 'negative'),
              ('My soul is as black as soy sauce', 'negative'),
              ('Cant tell if I am sad or just tired', 'negative'),
              ('I hate getting to know people', 'negative'),
              ('I am not your fucking counselor', 'negative'),
              ('Don\'t fucking raise your voice to me', 'negative'),
              ('Don\'t talk to me just to criticize the way I choose to live', 'negative'),
              ('I have a problem with seeing problems', 'negative'),
              ('Another sleepless night', 'negative'),
              ('I just don\'t anymore about this', 'negative'),
              ('There is nothing that I truly feel like I am great at', 'negative'),
              ('My life is cold even in the summer', 'negative'),
              ('Life is dark', 'negative')]

tweets = []
for (words, sentiment) in pos_tweets + neg_tweets:
	words_filtered = [e.lower() for e in words.split() if len (e) >= 3]
	tweets.append((words_filtered, sentiment))


word_features = get_word_features(get_words_in_tweets(tweets))

training_set = nltk.classify.apply_features(extract_features, tweets)
classifier = nltk.NaiveBayesClassifier.train(training_set)

#print classifier.show_most_informative_features(32)

#tweet = ['I am not good at this', 'I hate my life', 'I feel good', 'My life is cold', 'Life is dark']
with open("positivetweets.txt", "r") as ins:
    tweet = []
    for line in ins:
        tweet.append(line)
countPos = 0
countNeg = 0
for x in range (0, len(tweet)):
  if (classifier.classify(extract_features(tweet[x].split()))) == 'positive':
    countPos+=1
    print 'red world'
  else:
    countNeg+=1
    print 'blue word'
print countPos
print countNeg
img = Image.new( 'RGB', (255,255), "black") # create a new black image
pixels = img.load() # create the pixel map
if countPos > countNeg:
  for i in range(img.size[0]):    # for every pixel:
    for j in range(img.size[1]):
        pixels[i,j] = (countPos*i, countNeg*j, countPos+countNeg) # set the colour accordingly
   
    #img.show()
elif countPos == countNeg:
  #img = Image.new( 'RGB', (255,255), "black") # create a new black image
  #pixels = img.load() # create the pixel map
   
  for i in range(img.size[0]):    # for every pixel:
    for j in range(img.size[1]):
        pixels[i,j] = (countPos*i, countNeg*j, 2*countPos) # set the colour accordingly
   
    #img.show()
else:
  #img = Image.new( 'RGB', (255,255), "black") # create a new black image
  #pixels = img.load() # create the pixel map
   
  for i in range(img.size[0]):    # for every pixel:
    for j in range(img.size[1]):
        pixels[i,j] = (countPos*i, countNeg*j, 5*countNeg-countNeg) # set the colour accordingly
   
    #img.show()
img.show()
