import json
import sys
#argv[0] is script name. pass command line arguments to puthon script AFINN-111.txt and output.txt
sentiment_dt =sys.argv[1]
twitter_dt = sys.argv[2]

#To create list of dictionaries from output.txt file
def tweetword(twitter_dt):
    twitter_list = []
    twitterRec = open(twitter_dt)

for line in twitterRec:
    twitter_list.append(json.loads(line))
    return twitter_list
    
#To create list of dictionary from AFINN-111 file for the scores  
def sentimentword(sentiment_dt):
    sentRec = open(sentiment_dt)
    scores = {}
    for line in sentRec:
        term, score  = line.split("\t")  
        scores[term] = float(score)  

    return scores
    
    
    
  def main():
    tweets = tweetword (twitter_dt)
    sentiment = sentimentword(sentiment_dt)
    
 #To tokenize the tweets and to get the sentiment score for each word   
    for index in range(len(tweets)):
        tweet = tweets[index]["text"].split()
        sentiScore = 0
        for word in tweet:
            word = word.rstrip('?:!.,;"!@')
            word = word.replace("\n", "")
            
            if not (word.encode('utf-8', 'ignore') == ""):
                if word.encode('utf-8') in sentiment.keys():
                    sentiScore = sentiScore + float(sentiment[word])
                    
                else:
                    sentiScore = sentiScore 

        print float(sentiScore)
   
    
if __name__ == '__main__':
    main()
  