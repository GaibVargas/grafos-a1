import math
import sys
from typing import TextIO
from Grafo import Grafo

def inicilizacao(qtdVertices: int):
  distancia: list[int] = []
  ancestral: list[int] = []
  for i in range(qtdVertices):
    distancia.append(math.inf)
    ancestral.append(None)
  return [distancia, ancestral]

def relaxamento(grafo: Grafo, aresta: "tuple[int, int]", distancia: "list[float]", ancestral: "list[int]"):
  u = aresta[0] - 1
  v = aresta[1] - 1
  if (distancia[v] > distancia[u] + grafo.custo[u][v]):
    distancia[v] = distancia[u] + grafo.custo[u][v]
    ancestral[v] = u + 1
  if (distancia[u] > distancia[v] + grafo.custo[v][u]):
    distancia[u] = distancia[v] + grafo.custo[v][u]
    ancestral[u] = v + 1

def constroiMensagens(origem: int, vertice: int, ancestral: "list[int]", acc_msg: str):
  msg = ""
  if (origem != vertice):
    msg += constroiMensagens(origem, ancestral[vertice - 1], ancestral, acc_msg)
    return f"{msg} {vertice},"
  return acc_msg

def bellmanFord(grafo: Grafo, vertice: int):
  [d, a] = inicilizacao(grafo.qtdVertices())
  d[vertice - 1] = 0

  for i in range(grafo.qtdVertices() - 2):
    for aresta in grafo.vetor_arestas:
      relaxamento(grafo, aresta, d, a)
  
  for aresta in grafo.vetor_arestas:
    # Verifica existência de ciclo negativo
    if (d[aresta[1] - 1] > d[aresta[0] - 1] + grafo.custo[aresta[0] - 1][aresta[1] - 1]):
      return (False, None, None)
    if (d[aresta[0] - 1] > d[aresta[1] - 1] + grafo.custo[aresta[1] - 1][aresta[0] - 1]):
      return (False, None, None)
  
  return (True, d, a)

def main():
  grafo = Grafo()
  if (len(sys.argv) < 3):
    print("É necessário indicar um arquivo e um vértice como argumento do programa\npython bellman-ford.py [arquivo] [inteiro]")
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
  [resultado, d, a] = bellmanFord(grafo, vertice)

  if (not resultado):
    print("Ciclo negativo identificado")
    return
  
  for i in range(grafo.qtdVertices()):
    if (i == vertice - 1): continue
    print(f"{i + 1}:", end="")
    mensagem = constroiMensagens(vertice, i + 1, a, "")
    print(f"{mensagem[:len(mensagem) - 1]}; d={d[i]}")
    
main()