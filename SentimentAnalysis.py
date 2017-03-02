from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

sid = SentimentIntensityAnalyzer()

def Analyse(sentence):
    retval = sid.polarity_scores(sentence)
    if retval['compound'] >= 0:
        return 'pos'
    else:
        return 'neg'

def Analyse_Raw(sentence):
     return sid.polarity_scores(sentence)