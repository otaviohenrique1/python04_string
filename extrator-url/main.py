# url = "https://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100"
url = "bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar"
# print(url)

# Sanitização da URL
# url.replace(" ", "")
url.strip()

# Validação da URL
if url == "":
    # raise => parecido com o throw
    raise ValueError("A URL esta vazia")

# [inicio:final]
# [0:19] => pega substring que comeca no 0 e vai ate o 18
# url_base = url[0:19]

# Separa base e os parâmetros
indice_interrogacao = url.find("?")
url_base = url[:indice_interrogacao]
# print(url_base)
url_parametros = url[indice_interrogacao + 1 :]
print(url_parametros)

# Busca o valor de um parâmetro
parametro_busca = "quantidade"
indice_parametro = url_parametros.find(parametro_busca)
# print(indice_parametro)
indice_valor = indice_parametro + len(parametro_busca) + 1
indice_e_comercial = url_parametros.find("&", indice_valor)
if indice_e_comercial == -1:
    valor = url_parametros[indice_valor:]
else:
    valor = url_parametros[indice_valor:indice_e_comercial]

print(valor)
