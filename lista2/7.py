import pandas as pd
from sklearn.naive_bayes import GaussianNB
from sklearn.feature_extraction.text import CountVectorizer

# Naive Bayes

def separateTexts(classification):
    #separando os textos por classificação (stmt ou question)
    classList = []
    for index, row in csvData.iterrows():
        if(row['classification'] == classification):
            classList.append(row['text'])
    return classList

def separeteWords(classList, newText, classification, totalWords):
    #classList = (Lista de questões) ou (Lista de stmt)
    #separando as palavras em cada texto e a quantidade de aparições
    countVec = CountVectorizer()
    X = countVec.fit_transform(classList)
    
    wordList = countVec.get_feature_names()#recebendo a lista de palavras de todos os textos do classList
    countList = X.toarray().sum(axis = 0) #somando a quantidade de aparições de cada palavra

    freqWords = dict(zip(wordList, countList))#dicionário com a frequencia de cada palavra

    probNewText = []
    for word in newText:
        if word in freqWords.keys():
            count = freqWords[word]
        else:
            count = 0
        probNewText.append((count + 1)/(len(wordList) + totalWords))
    
    print(classification, dict(zip(newText, probNewText)))
    return probNewText
    #return dict(zip(newText, probNewText))


text = ['They are novels', 'have you read this book', 'who is the author', 'what are the characters', 'This is how i bought the book',
'I like fictions', 'what is your favorite book', 'This is my book']
classification = ['stmt', 'question', 'question', 'question', 'stmt', 'stmt', 'question', 'stmt']

data = {
    'text':text,
    'classification': classification 
}

csvData = pd.DataFrame(data)

countVec = CountVectorizer()
X = countVec.fit_transform(csvData['text'])

totalWords = len(countVec.get_feature_names())#total de palavras no arquivo


newText = ['what','do','you','mean']

stmtList = separateTexts('stmt')
questionList = separateTexts('question')

stmtWordProb = separeteWords(stmtList, newText, 'stmt', totalWords)
questionWordProb = separeteWords(questionList, newText, 'question', totalWords)

stmtResult = 1
questionResult = 1 

for prob in stmtWordProb:
    stmtResult = stmtResult * prob
for prob in questionWordProb:
    stmtResult = questionResult * prob
 
if(stmtResult > questionResult):
    print("O novo texto foi classificado como 'stmt'.")
else:
    print("O novo texto foi classificado como 'question'.")

