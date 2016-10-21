import string
import re
import nltk
import cPickle as pickle
from random import randint

class TextGenerator:
    def __init__(self, index2WordFile, word2IndexFile, corpus):
        self.index2WordFile = index2WordFile
        self.word2IndexFile = word2IndexFile
        self.sequenceOfIndices = []
        self.word2Index = {}
        self.index2Word = {}
        self.corpusWordsCount = None

        with open(corpus, 'r') as f:
            content = ''.join(f.readlines()).replace("\n", "")
            words = nltk.word_tokenize(content)
            self.tokens = [word.lower() for word in words]
            for word in self.tokens:
                if word in self.word2Index:
                    index = self.word2Index[word]
                else:
                    index = len(self.word2Index)
                    self.word2Index[word] = index
                    self.index2Word[index] = word
                self.sequenceOfIndices.append(index)

            with open(index2WordFile, 'wb') as handle:
                pickle.dump(self.index2Word, handle)

            with open(word2IndexFile, 'wb') as handle:
                pickle.dump(self.word2Index, handle)

        self.corpusWordsCount = len(self.tokens)

    def generateSequence(self, length):
        maxIndex = self.corpusWordsCount - length
        startIndex = randint(0, maxIndex)
        return self.sequenceOfIndices[startIndex: startIndex + length]

    def saveSamplesToFile(self, length, samplesCount, fileToSave):
        samples = [self.generateSequence(length) for _ in range(samplesCount)]
        with open(fileToSave, "w+") as text_file:
            for sample in samples:
                strSentence = " ".join([str(index) for index in sample]) + "\n"
                text_file.write(strSentence)

    def getTextFromTokenSequence(self, lineOfTokens):
        endOfSentenceSigns = ['.', '?', '!']
        sentenceSigns = [':', ';', ',', '\'', '\'s']
        sequencesToSkip = ["''", "``"]
        isEndOfSentence = False
        strWords = ""
        indices = [int(strIndex) for strIndex in lineOfTokens.split(" ")]
        words = [self.index2Word[index] for index in indices if index in self.index2Word]
        for word in words:
            if word in sequencesToSkip:
                continue
            if word in sentenceSigns:
                strWords += word
                continue
            if word in endOfSentenceSigns:
                strWords += word
                isEndOfSentence = True
            else:
                if isEndOfSentence:
                    word = word.title()
                    isEndOfSentence = False
                strWords += " %s" % word
        return strWords.lstrip()


        #strWords = " ".join(words)
if __name__ == "__main__":
    testInput = "./target_generate/generator_sample.txt"
    generator = TextGenerator('index2word.pickle', 'word2index.pickle', '../corpus_tools/data/source/dickens.txt')
    with open(testInput, 'r') as f:
        sentences = f.readlines()

    for strSentence in sentences:
        strWords = generator.getTextFromTokenSequence(strSentence)
        #indices = [int(strIndex) for strIndex in strSentence.split(" ")]
        #words = [generator.index2Word[index] for index in indices if index in generator.index2Word]
        #strWords = " ".join(words)
        print strWords

