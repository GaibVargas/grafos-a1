import sys
from typing import TextIO
from Grafo import Grafo

def vizinhoNaoVisitado(grafo: Grafo, vertice: int, arestas_conhecidas: "dict[tuple[int], bool]"):
  vizinhos = grafo.vizinhos(vertice)
  for vizinho in vizinhos:
    if ((vizinho, vertice) in arestas_conhecidas and 
        not arestas_conhecidas[(vizinho, vertice)]): 
      return [True, (vizinho, vertice)]

    if ((vertice, vizinho) in arestas_conhecidas and 
        not arestas_conhecidas[(vertice, vizinho)]): 
      return [True, (vertice, vizinho)]

  return [False, None]

def verticesComAdjNaoVisitada(ciclo: "list[int]", arestas_conhecidas: "dict[tuple[int], bool]"):
  vertices = set()
  for vertice in ciclo:
    for aresta in arestas_conhecidas.keys():
      if ((vertice in aresta) and (not arestas_conhecidas[aresta])):
        vertices.add(vertice)
  return vertices

def buscarSubciclo(grafo: Grafo, vertice: int, arestas_conhecidas: "dict[tuple[int], bool]"):
  ciclo = [vertice]
  vertice_inicial = vertice

  while(True):
    [haVizinho, aresta] = vizinhoNaoVisitado(grafo, vertice, arestas_conhecidas)
    if (not haVizinho):
      return [False, None]
    
    arestas_conhecidas[aresta] = True
    vertice = aresta[0] if vertice != aresta[0] else aresta[1]
    ciclo.append(vertice)
    if (vertice_inicial == vertice):
      break
  
  verticesComAdjNaoVisitada_ = verticesComAdjNaoVisitada(ciclo, arestas_conhecidas)
  for v in verticesComAdjNaoVisitada_:
    [resultado, subciclo] = buscarSubciclo(grafo, v, arestas_conhecidas)

    if (not resultado):
      return [False, None]
    
    ciclo[ciclo.index(v):ciclo.index(v) + 1] = subciclo
    return [True, ciclo]
  return [True, ciclo]

def hierholzer(grafo: Grafo):
  arestas_conhecidas = {}
  for aresta in grafo.vetor_arestas:
    arestas_conhecidas[aresta] = False
  vertice_inicial = grafo.vetor_arestas[0][0]

  [resultado, ciclo] = buscarSubciclo(grafo, vertice_inicial, arestas_conhecidas)
  if (not resultado):
    return [False, None]
  else:
    if (False in arestas_conhecidas): return [False, None]
    return [True, ciclo]

def main():
  grafo = Grafo()
  if (len(sys.argv) < 2):
    print("É necessário indicar um arquivo como argumento do programa\npython ciclo_euleriano.py [arquivo]")
    return

  file_name = sys.argv[1]
  file: TextIO = None

  try:
    file = open(file_name, 'r')
  except:
    print("Erro ao abrir o arquivo. Verifique se o nome do arquivo informado está correto")
    return
  
  grafo.ler(file)
  [resultado, ciclo] = hierholzer(grafo)
  
  print_resultado = "1" if resultado else "0"
  print(print_resultado)
  if resultado: print(ciclo)
  
main()