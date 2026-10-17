import pandas as pd

dados_clientes = {
    "id_cliente": [1, 2, 3, 4],
    "nome": ["Ana", "Bruno", "Carla", "Daniel"],
    "cidade": ["Juiz de Fora", "São Paulo", "Rio de Janeiro", "São Paulo"]
}

df_clientes = pd.DataFrame(dados_clientes)

dados_pedidos = {
    "id_pedido": [101, 102, 103, 104, 105],
    "id_cliente": [1, 2, 2, 3, 5],
    "valor": [200.0, 150.0, 300.0, 500.0, 100.0]
}

df_pedidos = pd.DataFrame(dados_pedidos)

print(df_clientes)
print(df_pedidos)


#pd.merge(df_esquerda, df_direita, on"coluna_chave", how"tipo")
#on → coluna usada como chave nas duas tabelas.
#how → tipo de junção:
#"inner": só o que existe nas duas tabelas.
#"left": todos da esquerda, batendo com o que existir na direita.
#"right": todos da direita, batendo com o que existir na esquerda.
#"outer": todos de ambos os lados (com nulos quando não houver correspondência).


#inner join
df_inner = pd.merge(df_pedidos, df_clientes, on="id_cliente", how="inner")
print(df_inner)

#left join
df_left = pd.merge(df_clientes, df_pedidos, on="id_cliente", how="left")
print(df_left)

#right join
df_right = pd.merge(df_clientes, df_pedidos, on="id_cliente", how="right")
print(df_right)

#outer join
df_outer = pd.merge(df_clientes, df_pedidos, on="id_cliente", how="outer")
print(df_outer)



print("------------------------------------------------------------------------------------")

dados_pedidos2 = {
    "id_pedido": [101, 102, 103],
    "cliente_id": [1, 2, 3],
    "valor": [200.0, 150.0, 300.0]
}

df_pedidos2 = pd.DataFrame(dados_pedidos2)

df_merge = pd.merge(df_clientes, df_pedidos2, left_on="id_cliente", right_on="cliente_id",how="inner")
print(df_merge)
df_merge = df_merge.drop(columns=["cliente_id"])
print(df_merge)


print("------------------------------------------------------------------------------------")



#Tipos de relacionamento: one-to-one, many-to-one, many-to-many
#6.1. One-to-one (1 para 1)
#Cada linha de uma tabela corresponde a exatamente uma linha da outra.
#Exemplo: tabela de clientes + tabela de documentos (CPF único).
#Na prática com merge, o número de linhas não se multiplica.

#6.2. Many-to-one (muitos para 1)
#Vários registros de uma tabela apontam para um único registro da outra.
#Exemplo:
#Muitos pedidos (df_pedidos) para um cliente (df_clientes).
#É exatamente o caso de id_cliente em df_pedidos.
#Quando você faz merge, as informações do cliente são repetidas em várias linhas, uma para cada pedido.

#6.3. Many-to-many (muitos para muitos)
#É quando ambos os lados podem ter várias repetições da chave.
#Exemplo:
#Tabela A: associações de aluno x curso (várias linhas por aluno).
#Tabela B: outro conjunto com aluno x atividade.
#Merges many-to-many podem aumentar bastante o número de linhas, pois cada combinação é criada.
#É importante ficar atento para não multiplicar linhas sem querer.



print("------------------------------------------------------------------------------------")


dados_jan = {
    "data": ["2024-01-01", "2024-01-02", "2024-01-03"],
    "loja": ["Centro", "Centro", "Shopping"],
    "valor": [1000.0, 1500.0, 2000.0]
}

dados_fev = {
    "data": ["2024-02-01", "2024-02-02"],
    "loja": ["Centro", "Shopping"],
    "valor": [1800.0, 2200.0]
}

df_jan = pd.DataFrame(dados_jan)
df_fev = pd.DataFrame(dados_fev)

print(df_jan)
print(df_fev)

df_1_bimestre = pd.concat([df_jan, df_fev], ignore_index=True)
print(df_1_bimestre)


print(df_jan.shape)
print(df_fev.shape)
print(df_1_bimestre.shape)



df_a = pd.DataFrame({"A": [1, 2, 3]})
df_b = pd.DataFrame({"B": [4, 5, 6]})

df_lado = pd.concat([df_a, df_b], axis=1)
print(df_lado)










