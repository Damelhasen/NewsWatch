from textblob import TextBlob
wiki = TextBlob("I love the Product. It is amazing and works great!")
print(wiki.sentiment.polarity*100)