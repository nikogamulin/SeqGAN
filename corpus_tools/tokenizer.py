#import Stemmer
import nltk
import pickle
import re
#stemmer = Stemmer.Stemmer('english')
word2index = {}
index2word = {}
maxSentenceLength = 0
sequenceOfIndicesSentences = []
MODEL_FILE = '../MLE_SeqGAN/save/target_params.pkl'
SENTENCES_FILE = '../MLE_SeqGAN/save/real_data.txt'
with open('./data/source/dickens.txt', 'r') as f:
    content = ''.join(f.readlines()).replace("\n", "")
    sentences = re.split(r' *[\.\?!][\'"\)\]]* *', content)
model = pickle.load(open(MODEL_FILE, "rb"))
for sentence in sentences:
    sequenceOfIndices = []
    words = nltk.word_tokenize(sentence.replace('\n', ''))
    sentenceLength = len(words)
    if sentenceLength > 20:
        continue
    if sentenceLength > maxSentenceLength:
        maxSentenceLength = sentenceLength
    for word in words:
        #wordStemmed = stemmer.stemWord(word.lower())
        wordStemmed = word.lower()
        if wordStemmed in word2index:
            index = word2index[wordStemmed]
        else:
            index = len(word2index) + 1
            word2index[wordStemmed] = index
            index2word[index] = wordStemmed
        sequenceOfIndices.append(index)
    sequenceOfIndicesSentences.append(sequenceOfIndices)

with open('index2word.pickle', 'wb') as handle:
    pickle.dump(index2word, handle)

with open('word2index.pickle', 'wb') as handle:
    pickle.dump(word2index, handle)

sentencesModified = []
for sentence in sequenceOfIndicesSentences:
    sentenceLength = len(sentence)
    diff = maxSentenceLength - sentenceLength
    wordsToAppend = [0] * diff
    sentencesModified.append(sentence + wordsToAppend)

for sentence in sentencesModified:
    strSentence = " ".join([str(index) for index in sentence]) + "\n"
    with open(SENTENCES_FILE, "a") as text_file:
        text_file.write(strSentence)