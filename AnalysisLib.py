import SentimentAnalysis

sentences = [
            "*******ATTENTION DOCUMENT PROCESSING: prepare expense verification form from 2016/2017 to be sent to One exchange******************",
            "price went down",    # pos...  
            "your website was down and I could not make a payment!",  
            "I was going all the way up and down",
            "I will be happy if price goes DOWN!"]
			

for sentence in sentences:
    vs = SentimentAnalysis.Analyse_Raw(sentence)
    print("{:-<65} {} Result => {}".format(sentence, str(vs), "Pos" if vs["compound"] > 0 else "Neg" if vs["compound"] < 0 else "?"))