import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import normaltest

#Código das questões 4 e 5 da lista 1 de Ciência de dados

csvData = pd.read_csv('lista1/diabetes_app.csv')
#Peguei esse dataset de uma aula antiga de apredizagem de máquina

#Questão 4

#Foram escolhidos os dados de duas colunas para colocar em v1 e v2
v1 = csvData['BloodPressure'] #Pressão Arterial Diastólica
v2 = csvData['BMI'] #Índice de Massa Corporal

#Calculando média e mediana de v1 e v2
v1Mean = v1.mean()
v1Median = v1.median()
v2Mean = v2.mean()
v2Median = v2.median()

print("-------------------------------")
print(csvData)
print("-------------------------------")
print("a) Mediana de V1 < Média de V1")
print("resposta: ",v1Median,"<",v1Mean)
print("-------------------------------")
print("b) Mediana de V2 > Média de V2")
print("resposta: ",v2Median,">",v2Mean)

#Questão 5

#Histogramas de cada variável, v1 e v2


plt.hist(v1)
plt.title('Distribuição de Pressão Arterial')
plt.xlabel('Blood Pressure')
plt.ylabel('Pessoas')
plt.grid(True)
plt.show()


plt.hist(v2)
plt.title('Distribuição de Índice de Massa Corporal')
plt.xlabel('BMI')
plt.ylabel('Pessoas')
plt.grid(True)
plt.show()
plt.close()
