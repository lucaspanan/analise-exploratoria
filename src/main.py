# 1. Importação das bibliotecas
import pandas as pd 
import seaborn as sns
import numpy as np 
import matplotlib.pyplot as pyplot

def carregar_dados():
    df = pd.read_csv("data/mkt_data.csv")
    return df

def inspecionar_dados(df,numericos):
    print(df.info())

    #com o (df.select_dtypes) selecionei todos os tipos de dados que estão dentro da variavel na parte de colunas
    print(df.select_dtypes(include=numericos).columns)

    #ver quantidade de duplicados
    print("quantidade de dados duplicados:",df.duplicated().sum())

    return df

def main():
     #coloquei todos os formatos que python reconhece como numerico em uma variavel
    numericos=["int16",'int32','int64','float16','float32','float64']
    
    # 2. Leitura dos dados
    df= carregar_dados()
    # ==================================================
    #criando uma copia do datafame original
    df_copy = df.copy()
    # 3. Inspeção inicial dos dados
    df= inspecionar_dados(df,numericos)
    # ==================================================

    # 4. Limpeza e preparação dos dados
    #eliminar a coluna 'Unnamed: 0'
    df= df.drop("Unnamed: 0", axis= 1)

    #ver quantidades de nullos 
    print("nome das colunas e quantidade de nulos que á nelas", df.isnull().sum())

    #ver ocorrencias da coluna 
    #nessa coluna so aparece 5.0 e o resto é nullo que indica que aquela pessoa não tem aquela determinada variavel, no caso ela não tem phd
    #por tanto essa coluna pode se tornar um booleano; 1 se ela fez e 0(nulo) se ela não fez
    print("quantidade do registro na coluna,", df['education_PhD'].value_counts())

    #colocando todas as colunas que tem valores nulos em uma variavel
    #coloque dentro de uma variavel as colunas com algum valor nulo e transforme em lista
    colunas_Com_nulos= df.columns[df.isnull().any()].tolist()

    #substituir por booleano
    for item in colunas_Com_nulos:
        df["booleano_"+str(item)]= np.where(df[item].isnull(), 0, 1)
    #se for nulo, substituimos por 0, caso contrario subistituirmos por 1

    # ==================================================
    # 5. Estatística descritiva

    # usamos o df_copy, pois o df tem colunas booleanas criadas acima.
    print("principais estatisticas das colunas numericas de interesse: \n",df_copy.select_dtypes(include=numericos).describe())

    #ver histograma para acopanhar os salarios 
    df['Income'].hist()


    #mostrar boxplot da coluna income
    sns.boxplot(df["Income"])
    #pyplot.show()

    #calcular o coeficiente de variação da coluna income
    desvio= df["Income"].std()
    media = df["Income"].mean()
    cv = desvio / media * 100

    print("o coeficiente de variação é de: ",cv)

    #calculando o skew >0 positivo calda para a direita <0 negativo calda pra a esquerda =0 Distribuição normal 
    print("\nos salarios parecem bem distribuidos na nossa base:",df["Income"].skew())

    # ==================================================
    # 6. Visualização dos dados
    #grafico de barras por educação 
    #ver grafico de quantidade da coluna education lavel

    #definir tamanho da figura
    pyplot.figure(figsize=(8,5))

    sns.countplot(data=df, x="education_level")
    #adicionar titulo
    pyplot.title("Distribuição dos clientes por nivel de escolaridade")
    #nome do eixo X
    pyplot.xlabel("Nivel de escolaridade")
    #nome do eixo Y
    pyplot.ylabel("quantidade de Clientes")

    #ajusta automaticamente os espaçamentos
    pyplot.tight_layout()
    pyplot.show()


    #ver grafico de contidade da coluna marital 
    pyplot.figure(figsize=(8,5))

    sns.countplot(data=df, x="marital_status")

    pyplot.title("DIstribuição dos clientes por estado civil")
    pyplot.xlabel("estado Civil")
    pyplot.ylabel("quantidade de clientes")

    pyplot.tight_layout()
    pyplot.show()

    pyplot.figure(figsize=(8,5))

    sns.boxplot(data=df, x="marital_status", y="kids")

    pyplot.title("Distribuição do numero de filhos por estado civil")
    pyplot.xlabel("Estado civil")
    pyplot.ylabel("numero de filhos")

    pyplot.tight_layout()
    pyplot.show()


    #para cada estado civiu quero analisar o status de filhos
    print(df.groupby("marital_status")["kids"].describe())
    #calcular media de filhos por estatos civil
    print(df.groupby("marital_status")["kids"].mean())
    #calcular mediana de filhos por estatus civil
    print(df.groupby("marital_status")["kids"].median())

    #as pessoas gastam mais ou menos em nossa plataforma quando tem filhos? veja nas colunas expenses e kids
    sns.boxplot(x='kids', y='expenses', data=df)
    pyplot.show()

    #vamos calcular a media de expenses por status de união
    #calculando a media de gastos
    print("media de gastos",df.groupby("kids")["expenses"].mean())
    #calculando a mediana
    print("mediana dos gastos",df.groupby("kids")["expenses"].median())

    #pessoas que tem um maior salario gastam mais? veja nas colunas income e expenses 
    #vamos fazer um grafico de dispersão mostrando expenses versus income
    pyplot.figure(figsize=(8,5))

    pyplot.scatter(df["expenses"], df["Income"])

    pyplot.title("Relação entre renda e gastos")
    pyplot.xlabel("renda")
    pyplot.ylabel("gastos")

    pyplot.tight_layout()
    pyplot.savefig("images/renda_vs_gastos.png", dpi=300)
    pyplot.show()

    print(df["expenses"].corr(df["Income"]))
    #A correlação de pearson é dada pela fórmula abaixo. O resultado foi 0.82.
    #Aparentemente existe uma correlação diretamente proporcional, em que pessoas que ganham mais também gastam mais
    #aparece como importado em cativeiro para usar em uma grande guerra para que nao possapara 
 

if __name__ == "__main__":
    main()