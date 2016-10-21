import cPickle as pickle

DEBUG = True

#FILE_TO_PROCESS_DEMO = '../MLE_SeqGAN/save/real_data.txt'
#FILE_TO_PROCESS_DEMO = '../MLE_SeqGAN/target_generate/eval_file.txt'
FILE_TO_PROCESS_DEMO = '../MLE_SeqGAN/target_generate/generator_sample.txt'
index2word = pickle.load(open("index2word.pickle", "rb"))

def getSentences(filename = FILE_TO_PROCESS_DEMO):
    strSentences = []
    with open(filename, 'r') as f:
        sentences = f.readlines()

    for strSentence in sentences:
        indices = [int(strIndex) for strIndex in strSentence.split(" ")]
        words = [index2word[index] for index in indices if index in index2word]
        strWords = " ".join(words)
        if DEBUG:
            print strWords
        strSentences.append(strWords)
    return strSentences

if __name__ == "__main__":
    test = getSentences()
