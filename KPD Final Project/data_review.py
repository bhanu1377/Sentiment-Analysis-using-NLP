__author__ = 'Nithin'
import nltk
from csv import reader
from string import punctuation
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
import pickle
import random
import csv



def all_words_t(data):
    ps = PorterStemmer()
    stop_words = set(stopwords.words('english'))
    all_words = []
    for inst in data:
        temp = inst[1]
        for p in list(punctuation):
            temp=temp.replace(p,'')
        temp = temp.split()
        for word in temp:
            if word not in stop_words:
                all_words.append(word.lower())

    return all_words

def find_features(all_words, review):
    ps = PorterStemmer()
    stop_words = set(stopwords.words('english'))
    for p in list(punctuation):
            review = review.replace(p,'')
    review = review.split()
    words = set(review)
    for word in words:
        if word not in stop_words:
            word = word.lower()
    features = {}
    for w in all_words:
        features[w] = (w in words)

    return features



def main():

    with open("final_train.csv", "r") as f:
        data_train = list(reader(f))


    all_words = all_words_t(data_train)
    all_words = nltk.FreqDist(all_words)

    #featuresets = [(find_features(all_words,rev), category) for (rev, category) in data_train]
    featuresets = []


    for polarity, review in data_train:
        features = find_features(all_words,review)
        featuresets.append([features,polarity])

    random.shuffle(featuresets)
    print(len(featuresets))

    training_set = featuresets[:2000]
    testing_set = featuresets[2000:]

    classifier = nltk.NaiveBayesClassifier.train(training_set)
    print("Classifier accuracy percent:",(nltk.classify.accuracy(classifier, testing_set))*100)
    classifier.show_most_informative_features(15)
    save_classifier = open("naivebayes.pickle","wb")
    pickle.dump(classifier, save_classifier)
    save_classifier.close()















if __name__ == '__main__':
    main()