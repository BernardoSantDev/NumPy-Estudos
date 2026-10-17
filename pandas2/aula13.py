import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dados_exercicio = {
    "idade": [18, 22, 25, 30, 35, 40, 45, 50, 27, 33, 38, 42, 48, 55],
    "minutos_exercicio_semana": [60, 120, 150, 200, 90, 80, 60, 45, 180, 160, 100, 70, 50, 30],
    "sexo": ["F", "M", "F", "M", "F", "F", "M", "M", "F", "M", "F", "M", "F", "M"]
}

df_ex = pd.DataFrame(dados_exercicio)
print(df_ex)


sns.set_theme(style="whitegrid")

plt.figure(figsize=(8, 4))
sns.histplot(data=df_ex, x="minutos_exercicio_semana", bins=8, kde=False)
#data=df_ex → DataFrame.
#x="minutos_exercicio_semana" → coluna no eixo X.
#bins=8 → número de faixas do histograma.
#kde=False → desativa curva de densidade (padrão é False, mas você pode ativar).

plt.title("Distribuição de minutos de exercício por semana")
plt.xlabel("Minutos por semana")
plt.ylabel("Frequência")
plt.tight_layout()
plt.show()


#Podemos comparar a distribuição entre homens e mulheres
sns.histplot(data=df_ex, x="minutos_exercicio_semana", bins=8, hue="sexo", multiple="stack")
#multiple pode ser "stack", "dodge", "layer"
plt.title("Distribuição de minutos de exercício por semana por sexo")
plt.xlabel("Minutos por semana")
plt.ylabel("Frequência")
plt.tight_layout()
plt.show()


plt.figure(figsize=(6, 4))
sns.boxplot(data=df_ex, x="sexo", y="minutos_exercicio_semana")
plt.title("Minutos de exercício por semana por sexo")
plt.xlabel("Sexo")
plt.ylabel("Minutos por semana")
plt.tight_layout()
plt.show()


#GRAFICO DISPERSAO SIMPLES
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df_ex, x="idade", y="minutos_exercicio_semana")
plt.title("Relação entre idade e minutos de exercício por semana")
plt.xlabel("Idade")
plt.ylabel("Minutos de exercício por semana")
plt.tight_layout()
plt.show()

#GRFICO DISPERSÃO COM HUE
plt.figure(figsize=(8, 5))
sns.scatterplot(
    data=df_ex,
    x="idade",
    y="minutos_exercicio_semana",
    hue="sexo"
)
plt.title("Relação entre idade e minutos de exercício por semana por sexo")
plt.xlabel("Idade")
plt.ylabel("Minutos de exercício por semana")
plt.tight_layout()
plt.show()


print("-------------------------------------------------------------------------------")


dados_notas = {
    "turma": ["A", "A", "A", "A", "B", "B", "B", "B", "C", "C", "C", "C"],
    "nota": [7.0, 8.5, 6.0, 9.0, 5.5, 6.5, 7.0, 8.0, 9.5, 8.5, 7.5, 9.0]
}

df_notas = pd.DataFrame(dados_notas)
print(df_notas)


plt.figure(figsize=(6, 4))
sns.boxplot(data=df_notas, x="turma", y="nota")
plt.title("Distribuição de notas por turma")
plt.xlabel("Turma")
plt.ylabel("Nota")
plt.tight_layout()
plt.show()


#Distribuição geral de notas: histplot ou kdeplot
plt.figure(figsize=(8, 4))

sns.histplot(data=df_notas, x="nota", bins=8, kde=True)
#kde=True adiciona uma curva de densidade, aproximando a distribuição contínua.
plt.title("Distribuição geral de notas")
plt.xlabel("Nota")
plt.ylabel("Frequência")
plt.tight_layout()
plt.show()
#Você pode também usar sns.kdeplot diretamente se quiser apenas a curva:
plt.figure(figsize=(8, 4))
sns.kdeplot(data=df_notas, x="nota", fill=True)
plt.title("Densidade de notas")
plt.xlabel("Nota")
plt.tight_layout()
plt.show()








