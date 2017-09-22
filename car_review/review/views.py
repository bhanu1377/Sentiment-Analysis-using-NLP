from django.shortcuts import render, HttpResponseRedirect
from csv import reader
from .models import cars
from string import punctuation
from nltk.corpus import stopwords
import nltk
import pickle

# Create your views here.

def home(request):
    with open('/Users/Nithin/Desktop/KPDWebsite/car_review/review/ratings_2007.csv', 'r') as f:
        ratings_2007 = list(reader(f))

    with open('/Users/Nithin/Desktop/KPDWebsite/car_review/review/ratings_2008.csv', 'r') as f:
        ratings_2008 = list(reader(f))

    with open('/Users/Nithin/Desktop/KPDWebsite/car_review/review/ratings_2009.csv', 'r') as f:
        ratings_2009 = list(reader(f))

    ratings_2007 = ratings_2007[1:]
    ratings_2008 = ratings_2008[1:]
    ratings_2009 = ratings_2009[1:]


    all_cars = cars.objects.all()
    for car in ratings_2007:
        car_name = car[0]
        car_year = int(car[1])
        car_ratings = int(car[2])
        car_score = float(car[3])
        temp = cars(car_name = car_name, car_year = car_year, car_ratings = car_ratings, car_score = car_score)
        temp.save()

    for car in ratings_2008:
        car_name = car[0]
        car_year = int(car[1])
        car_ratings = int(car[2])
        car_score = float(car[3])
        temp = cars(car_name = car_name, car_year = car_year, car_ratings = car_ratings, car_score = car_score)
        temp.save()

    for car in ratings_2009:
        car_name = car[0]
        car_year = int(car[1])
        car_ratings = int(car[2])
        car_score = float(car[3])
        temp = cars(car_name = car_name, car_year = car_year, car_ratings = car_ratings, car_score = car_score)
        temp.save()

    context = {'all_cars': all_cars}


    return render(request,'review/cars.html',context)

def find_features(all_words, review):
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




def take_review(request):
    info_year = request.POST['year']
    info_car_make = request.POST['cars']
    info_review = request.POST['message']
    all_cars = cars.objects.all()
    context = {'all_cars': all_cars}
    car_name = ""
    car_year = 0
    car_ratings = 0
    car_score = 0.0
    for car in all_cars:
        if car.car_name == str(info_car_make) and car.car_year == int(info_year):
            car_name = car.car_name
            car_year = car.car_year
            car_ratings = car.car_ratings
            car_score = car.car_score

    classifier_f = open("/Users/Nithin/Desktop/KPDWebsite/car_review/review/naivebayes.pickle", "rb")
    classifier = pickle.load(classifier_f)
    classifier_f.close()
    all_words = open("/Users/Nithin/Desktop/KPDWebsite/car_review/review/all_words.pickle", "rb")
    all_words = nltk.FreqDist(all_words)
    features_test = find_features(all_words,str(info_review))
    x = (classifier.classify(features_test))
    print(x)
    if int(x) == 0:
        car_score = ((car_score*car_ratings)+10)/(car_ratings+1)
        car_ratings += 1
        for car in all_cars:
            if car.car_name == str(info_car_make) and car.car_year == int(info_year):
                car.car_score = car_score
                car.car_ratings = car_ratings
                car.save()
    elif int(x) == 1:
        car_score = ((car_score*car_ratings))/(car_ratings+1)
        car_ratings += 1
        for car in all_cars:
            if car.car_name == str(info_car_make) and car.car_year == int(info_year):
                car.car_score = car_score
                car.car_ratings = car_ratings
                car.save()
    return render(request, 'review/cars.html', context)

def takereviewtwo(request):
    info_year = request.POST['year2']
    info_car_make = request.POST['cars2']
    all_cars = cars.objects.all()
    car_name = ""
    car_year = 0
    car_ratings = 0
    car_score = 0.0
    for car in all_cars:
        if car.car_name == str(info_car_make) and car.car_year == int(info_year):
            car_name = car.car_name
            car_year = car.car_year
            car_ratings = car.car_ratings
            car_score = car.car_score
    context = {'all_cars':all_cars,'car_name':car_name,'car_year':car_year,'car_ratings':car_ratings,'car_score':car_score}
    return render(request, 'review/takereviewtwo.html', context)









def submit(request):

    info_car_option = request.POST['car_option']

    if int(info_car_option)==1:
        all_cars = cars.objects.all()
        context = {'all_cars': all_cars}
        return render(request, 'review/option1.html', context)
    elif int(info_car_option) == 2:
        all_cars = cars.objects.all()
        context = {'all_cars': all_cars}
        return render(request, 'review/option2.html', context)









