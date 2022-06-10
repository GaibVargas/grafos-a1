from typing import TextIO
import math

class Grafo:
  def __init__(self):
    self.vertices = 0
    self.arestas = 0
    self.vetor_arestas = []
    self.rotulos: list[str] = []
    self.custo: list[list[float]]
  
  def qtdVertices(self):
    return self.vertices
  
  def qtdArestas(self):
    return self.arestas

  def grau(self, vertice: int):
    if (vertice > self.vertices):
      raise Exception("Vértice não existe")
    if (vertice <= 0):
      raise Exception("Vértice é um número positivo")
    vizinhos = self.vizinhos(vertice)
    return len(vizinhos)

  def rotulo(self, vertice: int):
    if (vertice > self.vertices):
      raise Exception("Vértice não existe")
    if (vertice <= 0):
      raise Exception("Vértice é um número positivo")
    return self.rotulos[vertice - 1]

  def vizinhos(self, vertice: int):
    if (vertice > self.vertices):
      raise Exception("Vértice não existe")
    if (vertice <= 0):
      raise Exception("Vértice é um número positivo")
    vizinhos = []
    vertice = vertice - 1
    for i in range(self.vertices):
      if (self.custo[vertice][i] != 0 and self.custo[vertice][i] != math.inf):
        vizinhos.append(i + 1)
    return vizinhos

  def haAresta(self, origem: int, destino: int):
    if (origem > self.vertices or destino > self.vertices):
      raise Exception("Vértices inválidos")
    if (origem <= 0 or destino <= 0):
      raise Exception("Vértice é um número positivo")
    
    custo = self.custo[origem - 1][destino - 1]
    if (custo == math.inf):
      return False
    return True

  def peso(self, origem: int, destino: int):
    if (origem > self.vertices or destino > self.vertices):
      raise Exception("Vértices inválidos")
    if (origem <= 0 or destino <= 0):
      raise Exception("Vértice é um número positivo")
    return self.custo[origem - 1][destino - 1]

  def ler(self, arquivo: TextIO):
    lendo_vertices = False
    lendo_arestas = False
    while True:
      linha = arquivo.readline()
      if not linha:
        break
      
      if (linha.find("*vertices") != -1):
        [_, numero] = linha.split()
        self.vertices = int(numero)
        self.iniciar_matriz_custo()
        lendo_vertices = True
        continue

      if (linha.find("*edges") != -1):
        lendo_vertices = False
        lendo_arestas = True
        continue

      if (lendo_vertices):
        if (linha.find('"') != -1):
          rotulo = linha[linha.find('"'):len(linha)-1]
        else:
          [_, rotulo] = linha.split()
        self.rotulos.append(rotulo)
      elif (lendo_arestas):
        [origem, destino, custo] = linha.split()
        origem = int(origem)
        destino = int(destino)
        custo = float(custo)
        self.custo[origem - 1][destino - 1] = custo
        self.custo[destino - 1][origem - 1] = custo
        self.vetor_arestas.append((origem, destino))
        self.arestas += 1
  
  def iniciar_matriz_custo(self):
    self.custo = []
    for i in range(self.vertices):
      self.custo.append([math.inf] * self.vertices)
    for i in range(self.vertices):
      self.custo[i][i] = 0