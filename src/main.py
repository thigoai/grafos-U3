import os

from utils.analise import executar_analise_gale_shapley, executar_analise_local_search, exibir_resultados
from utils.io_utils import carregar_caso_teste, listar_casos_teste, salvar_relatorio
from utils.executador import executar, menu_algoritmos
from utils.gerador import salvar_caso_teste

PASTA_CASOS = "../casos_teste"

def opcao_executar_caso():
    arquivos = listar_casos_teste(PASTA_CASOS)
    if not arquivos:
        print("Nenhum caso de teste comum encontrado. Use o gerador primeiro.")
        return

    print("\nCASOS DE TESTE DISPONÍVEIS")
    for idx, arq in enumerate(arquivos):
        print(f"[{idx + 1}] {arq}")

    escolha = int(input("\nEscolha o número do caso de teste: ")) - 1
    if escolha < 0 or escolha >= len(arquivos):
        print("Escolha inválida.")
        return

    arquivo_escolhido = arquivos[escolha]
    caminho = os.path.join(PASTA_CASOS, arquivo_escolhido)

    alg_escolha = menu_algoritmos()

    print(f"\nCarregando '{arquivo_escolhido}'...")
    H, M, H_pref, M_pref = carregar_caso_teste(caminho)

    try:
        nome_algoritmo, resultado = executar(alg_escolha, H, M, H_pref, M_pref)
    except NotImplementedError as e:
        print(f"\n[!] {e}")
        return
    except Exception as e:
        print(f"\n[!] ERRO: {e}")
        return

    relatorio, nome_arquivo_relatorio = salvar_relatorio(
        nome_algoritmo, arquivo_escolhido, resultado
    )
    print("\n" + relatorio)
    print(f"Relatório gravado em: {nome_arquivo_relatorio}")


def opcao_analise_complexidade():
    print("\n[1] Analisar Gale-Shapley")
    print("[2] Analisar Local Search")
    escolha = int(input("Qual algoritmo deseja analisar? "))
    
    os.makedirs(PASTA_CASOS, exist_ok=True)
    
    if escolha == 1:
        tamanhos, tempos = executar_analise_gale_shapley(PASTA_CASOS)
    elif escolha == 2:
        tamanhos, tempos = executar_analise_local_search(PASTA_CASOS, n_passos=200)
    else:
        print("Opção inválida.")
        return

    exibir_resultados(tamanhos, tempos)

def opcao_gerar_caso():
    print("\nGERADOR DE CASOS DE TESTE")
    nome = input("Nome do arquivo (ex: meu_teste.txt): ")
    if not nome.endswith('.txt'):
        nome += '.txt'
    
    try:
        n = int(input("Quantidade de motoristas (N): "))
        m = int(input("Quantidade de passageiros (M): "))
        
        p1 = float(input("Probabilidade de listas incompletas (p1) [ex: 0.1]: "))
        p2 = float(input("Probabilidade de empates (p2) [ex: 0.2]: "))
        
        salvar_caso_teste(nome, n, m, p1=p1, p2=p2)
        print(f"\n[+] Sucesso! O arquivo '{nome}' foi criado.")
        print("Você já pode selecioná-lo na Opção 1 do menu principal.")
    except ValueError:
        print("[!] Erro: Você deve digitar números inteiros para N e M, e decimais (com ponto) para as probabilidades.")


def menu_principal():
    print("\n" + "="*30)
    print("SISTEMA DE CARONAS")
    print("="*30)
    print("[1] Executar um Caso de Teste Específico")
    print("[2] Analisar Complexidade (Gerar, Salvar e Plotar)")
    print("[3] Gerar um Novo Caso de Teste Aleatório")
    return int(input("\nEscolha a opção desejada: "))

def main():
    os.makedirs(PASTA_CASOS, exist_ok=True)

    while True: 
        try:
            opcao = menu_principal()
        except ValueError:
            print("Entrada inválida. Encerrando.")
            break

        if opcao == 1:
            try:
                opcao_executar_caso()
            except ValueError:
                print("Entrada inválida.")
        elif opcao == 2:
            opcao_analise_complexidade()
        elif opcao == 3:
            opcao_gerar_caso()
        else:
            print("Opção inválida.")
            
        if input("\nDeseja voltar ao menu principal? (s/n): ").strip().lower() != 's':
            print("Encerrando o sistema...")
            break

if __name__ == "__main__":
    main()