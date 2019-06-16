# ====== importação da biblioteca =======
import pandas as pd

# ===== carregando a base de dados a ser trabalhanda ======
dados = pd.read_csv('mercado.csv', header = None)

# ===== Convertendo o modelo Dataframe do pandas para uma lista ======
# ===== O algoritmo apyori não recebe um Dataframe e sim uma lista =====
transacoes = []
for i in range(0, 10):
    transacoes.append([str(dados.values[i,j]) for j in range(0, 4)])

# ===== Importação do método responsável pelas regras ===== 
from apyori import apriori
regras = apriori(transacoes, min_support = 0.3, min_confidence = 0.8, min_lift = 2, max_length = 2)

# ===== Variável que aplica o formato lista nas regras =====
resultados = list(regras)
resultados

resultados2 = [list(x) for x in resultados]
resultados2
resultadoFormatado = []
for j in range(0, 2):
    resultadoFormatado.append([list(x) for x in resultados2[j][2]])
resultadoFormatado
