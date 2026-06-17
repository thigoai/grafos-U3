import os

from utils.analise import executar_analise_gale_shapley, exibir_resultados
from utils.io_utils import carregar_caso_teste, listar_casos_teste, salvar_relatorio
from utils.executador import executar, menu_algoritmos

PASTA_CASOS = "../casos_teste"


def menu_principal():
    print("SISTEMA DE CARONAS")
    print("[1] Executar um Caso de Teste Específico")
    print("[2] Analisar Complexidade do Gale-Shapley (Gerar, Salvar e Plotar)")
    return int(input("\nEscolha a opção desejada: "))


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
    print("\nIniciando Análise de Complexidade do Gale-Shapley...")
    os.makedirs(PASTA_CASOS, exist_ok=True)
    tamanhos, tempos = executar_analise_gale_shapley(PASTA_CASOS)
    exibir_resultados(tamanhos, tempos)


def main():
    os.makedirs(PASTA_CASOS, exist_ok=True)

    try:
        opcao = menu_principal()
    except ValueError:
        print("Entrada inválida. Encerrando.")
        return

    if opcao == 1:
        try:
            opcao_executar_caso()
        except ValueError:
            print("Entrada inválida.")
    elif opcao == 2:
        opcao_analise_complexidade()
    else:
        print("Opção inválida.")


if __name__ == "__main__":
    main()