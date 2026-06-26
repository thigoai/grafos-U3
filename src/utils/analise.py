import os
import time

from utils import gerador
from algoritmos.gale_shapley import gale_shapley
from algoritmos.local_search import local_search 

from utils.io_utils import carregar_caso_teste, imprimir_grafico_terminal, salvar_log_analise

TAMANHOS_GS = [10, 50, 100, 200, 400, 600, 800, 1000, 1200, 1500, 2000]

TAMANHOS_LS = [50, 100, 150]

N_REPETICOES = 30


def executar_analise_gale_shapley(pasta_casos, tamanhos=None):
    if tamanhos is None:
        tamanhos = TAMANHOS_GS

    tempos = []
    print("\nAnalisando Gale-Shapley...")
    
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
        print(f"N={n:<4} | {tempo:.4f} segundos.")

    return tamanhos, tempos


def executar_analise_local_search(pasta_casos, tamanhos=None, n_passos=200):
    if tamanhos is None:
        tamanhos = TAMANHOS_LS

    tempos = []
    tamanhos_executados = [] 
    print(f"\nAnalisando Local Search (Passos: {n_passos})...")

    for n in tamanhos:
        for i in range(N_REPETICOES):
            nome_arquivo = f"teste_N{n}.txt"
            caminho = os.path.join(pasta_casos, nome_arquivo)

            gerador.salvar_caso_teste(nome_arquivo, n, n, p1=0.4, p2=0.4)
            H, M, H_rank, M_rank = carregar_caso_teste(caminho)

            inicio = time.time()
            local_search(H, M, H_rank, M_rank, n_passos)
            fim = time.time()

            tempo = fim - inicio
            tempos.append(tempo)
            tamanhos_executados.append(n) 
            print(f"N={n:<4} | {tempo:.4f} segundos.")

    
    return tamanhos_executados, tempos


def exibir_resultados(tamanhos, tempos, nome_algoritmo="Gale-Shapley"):
    imprimir_grafico_terminal(tamanhos, tempos)
    salvar_log_analise(tamanhos, tempos, nome_algoritmo)
    
    print("Análise concluída :p")