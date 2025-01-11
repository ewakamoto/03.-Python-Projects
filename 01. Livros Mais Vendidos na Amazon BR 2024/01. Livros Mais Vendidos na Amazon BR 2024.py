import matplotlib.pyplot as plt
import pandas as pd


# Criando um dicionário básico:
Livro = {'Títulos': ['Café com Deus Pai 2025','A Biblioteca da Meia-Noite','É Assim Que Acaba','É Assim Que Começa','O Homem Mais Rico da Babilônia','Tudo é Rio','A Psicologia Financeira','Verity','Perigoso!','Como Fazer Amigos e Influenciar as Pessoas'],
         'Autores':['Júnior Rostirola','Matt Haig','Colleen Hoover','Colleen Hoover','George S.Clason','Carla Madeira','Morgan Housel','Colleen Hoover','Tim Warnes','Dale Carnegie'],
        'Idioma Original':['Português','Inglês','Inglês','Inglês','Inglês','Português','Inglês','Inglês','Inglês','Inglês']}

# Vamos criar um dataframe do dicionário:
dataframe = pd.DataFrame(Livro, columns=['Títulos', 'Autores', 'Idioma Original'])

x = dataframe.Autores
y = dataframe.Títulos

plt.xlabel('Autores')
plt.ylabel('Títulos')
plt.title('Autores x Títulos')

plt.scatter(x,y)


plt.show()
