import math
import sys
from typing import List, TextIO
from Grafo import Grafo

def buscaLargura(grafo: Grafo, vertice: int):
  if (vertice > grafo.qtdVertices() or vertice <= 0):
    print("Vértice inválido")
    return
  
  conhecido = []
  distancia = []
  ancestral = []
  for i in range(grafo.qtdVertices()):
    conhecido.append(False)
    distancia.append(math.inf)
    ancestral.append(None)
  
  conhecido[vertice - 1] = True
  distancia[vertice - 1] = 0

  fila = []
  fila.append(vertice)

  while len(fila) != 0:
    u = fila.pop(0)
    for v in grafo.vizinhos(u):
      if (not conhecido[v - 1]):
        conhecido[v - 1] = True
        distancia[v - 1] = distancia[u - 1] + 1
        ancestral[v - 1] = u
        fila.append(v)
  
  return [distancia, ancestral]

def printResultado(distancia: "list[int]" = []):
  maior_nivel: int
  for i in range(len(distancia)):
    if (i == 0):
      maior_nivel = distancia[i]
    else:
      if (distancia[i] > maior_nivel):
        maior_nivel = distancia[i]
  
  agrupamento_nivel: dict[int, list[int]] = {}
  for i in range(maior_nivel + 1):
    agrupamento_nivel[i] = []

  for i in range(len(distancia)):
    agrupamento_nivel[distancia[i]].append(i + 1)

  for nivel, vertices in agrupamento_nivel.items():
    print(f"{nivel}:", end="")
    for i in range(len(vertices)):
      print(f" {vertices[i]}", end="," if i != len(vertices) - 1 else "\n")

def main():
  grafo = Grafo()
  if (len(sys.argv) < 3):
    print("É necessário indicar um arquivo e um vértice como argumento do programa\npython buscas.py [arquivo] [inteiro]")
    return

  vertice = int(sys.argv[2])
  if (vertice < grafo.arestas):
    print("Vértice inválido")
    return

  file_name = sys.argv[1]
  file: TextIO = None

  try:
    file = open(file_name, 'r')
  except:
    print("Erro ao abrir o arquivo. Verifique se o nome do arquivo informado está correto")
    return
  
  grafo.ler(file)
  [distancia, _] = buscaLargura(grafo, vertice)
  printResultado(distancia)
  
main()
