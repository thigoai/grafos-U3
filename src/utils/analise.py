import os
import time

from utils import gerador
from algoritmos.gale_shapley import gale_shapley
from utils.io_utils import carregar_caso_teste, imprimir_grafico_terminal

TAMANHOS_PADRAO = [10, 50, 100, 200, 400, 600, 800, 1000, 1200, 1500, 2000]


def executar_analise_gale_shapley(pasta_casos, tamanhos=None):
    
    if tamanhos is None:
        tamanhos = TAMANHOS_PADRAO

    tempos = []

    for n in tamanhos:
        nome_arquivo = f"teste_N{n}.txt"
        caminho = os.path.join(pasta_casos, nome_arquivo)

        gerador.salvar_caso_teste(nome_arquivo, n, n, p1=0, p2=0)

        H, M, H_rank, M_rank = carregar_caso_teste(caminho)

        inicio = time.time()
        gale_shapley(H, M, H_rank, M_rank)
        fim = time.time()

        tempo = fim - inicio
        tempos.append(tempo)
        print(f"{nome_arquivo} - {tempo:.4f} segundos.")

    return tamanhos, tempos


def exibir_resultados(tamanhos, tempos):
    imprimir_grafico_terminal(tamanhos, tempos)
    print("Análise concluída :p")