import SentimentAnalysis

sentences = ["price went down",    # pos...  
            "your website was down and I could not make a payment!",  
            "I was going all the way up and down",
            "I will be happy if price goes DOWN!"]
			

for sentence in sentences:
    vs = SentimentAnalysis.Analyse_Raw(sentence)
    print("{:-<65} {} Result => {}".format(sentence, str(vs), "Pos" if vs["compound"] > 0 else "Neg" if vs["compound"] < 0 else "?"))