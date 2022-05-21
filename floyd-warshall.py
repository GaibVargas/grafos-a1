import sys
from copy import deepcopy
from typing import TextIO
from Grafo import Grafo

def floydWarshall(grafo: Grafo):
  d = deepcopy(grafo.custo)
  for k in range(grafo.qtdVertices()):
    for u in range(grafo.qtdVertices()):
      for v in range(grafo.qtdVertices()):
        d[u][v] = min(d[u][v], d[u][k] + d[k][v])
  return d

def main():
  grafo = Grafo()
  if (len(sys.argv) < 2):
    print("É necessário indicar um arquivo como argumento do programa\npython floyd-warshall.py [arquivo]")
    return

  file_name = sys.argv[1]
  file: TextIO = None

  try:
    file = open(file_name, 'r')
  except:
    print("Erro ao abrir o arquivo. Verifique se o nome do arquivo informado está correto")
    return
  
  grafo.ler(file)
  distancia = floydWarshall(grafo)
  for i in range(grafo.qtdVertices()):
    print(f"{i+ 1}: ", end="")
    for j in range(grafo.qtdVertices()):
      print(distancia[i][j], end=", " if j != len(distancia[i]) - 1 else "")
    print()
  print(grafo.custo)

main()