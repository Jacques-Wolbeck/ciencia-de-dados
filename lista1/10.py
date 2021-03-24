import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_val_score

#definindo o nome das colunas, já que o dataset não possui
names = ['Sepal length', 'Sepal width', 'Petal length', 'Petal width', 
                'Class']
iris = pd.read_csv('lista1/iris.data', names= names)


featureCols = ['Sepal length', 'Sepal width', 'Petal length', 'Petal width']


# dividindo os dados em feature e target
x = iris[featureCols]
y = iris['Class']

neighbors = list(range(1,20,2)) #definindo uma lista de valores impares para modificar o k do KNN durante o loop

kList = [] #lista para salvar os valores de k testados
cvScores = [] #Lista para salvar os scores do F-measure

for k in neighbors:
    knn = KNeighborsClassifier(n_neighbors = k)
    scores = cross_val_score(knn, x, y, cv = 10, scoring = 'f1_macro') #calculando os scores com F-measure
    kList.append(k)
    cvScores.append(scores.mean())

for k in kList:
    for score in cvScores:
        print("Para k=",k,"temos o score de:",score)



