import pickle
import numpy
numpy.random.seed(42)


words_file = "../text_learning/your_word_data.pkl" 
authors_file = "../text_learning/your_email_authors.pkl"
    
def my_func(words_file, authors_file):
    '''
    I will use this code later in the lesson so I made it a function
    '''
    
    ### The words (features) and authors (labels), already largely processed.
    ### These files should have been created from the previous (Lesson 10)
    ### mini-project.
    word_data = pickle.load( open(words_file, "r"))
    authors = pickle.load( open(authors_file, "r") )



     ### test_size is the percentage of events assigned to the test set (the
    ### remainder go into training)
    ### feature matrices changed to dense representations for compatibility with
    ### classifier functions in versions 0.15.2 and earlier
    from sklearn import model_selection
    features_train, features_test, labels_train, labels_test = model_selection.train_test_split(word_data, authors, test_size=0.1, random_state=42)

    from sklearn.feature_extraction.text import TfidfVectorizer
    vectorizer = TfidfVectorizer(sublinear_tf=True, max_df=0.5,
                                 stop_words='english')
    features_train = vectorizer.fit_transform(features_train)
    features_test  = vectorizer.transform(features_test).toarray()
    
    print vectorizer.get_feature_names()[21795]

    ### a classic way to overfit is to use a small number
    ### of data points and a large number of features;
    ### train on only 150 events to put ourselves in this regime
    features_train = features_train[:150].toarray()
    labels_train   = labels_train[:150]

    from sklearn.tree import DecisionTreeClassifier

    clf = DecisionTreeClassifier()
    clf.fit(features_train, labels_train)

    return clf, vectorizer, features_train, features_test, labels_train, labels_test


(clf, vectorizer, features_train, features_test, labels_train, labels_test) = my_func(words_file, authors_file)
#my_func(words_file, authors_file)
#print 'Number of training points = {0}'.format(len(features_train))


score = clf.score(features_test, labels_test)
print score
#import math
#print clf.feature_importances_.max()
"""
myArr = clf.feature_importances_
newArr = []
newArr = [(x, myArr[x]) for x in range(len(myArr)) if myArr[x] > 0.2]
"""
