from Grafo import Grafo

def main():
  file = open('test.net', 'r')
  grafo = Grafo()
  grafo.ler(file)

  vertice = 4
  print(grafo.rotulo(vertice))
  print(grafo.vizinhos(vertice))
  print(grafo.grau(vertice))
  print(grafo.peso(4, vertice))
  print(grafo.haAresta(2, vertice))
  
main()