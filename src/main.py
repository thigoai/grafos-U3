import os
import ast
from gale_shapley import gale_shapley
# from local_search import local_search

def carregar_caso_teste(caminho_arquivo):
    H_pref = {}
    M_pref = {}
    
    with open(caminho_arquivo, 'r', encoding='utf-8') as f:
        linhas = f.readlines()
        
    n, m = map(int, hashtags := linhas[0].strip().split())
    n, m = int(hashtags[0]), int(hashtags[1])
    H = list(range(1, n + 1))
    M = list(range(1, m + 1))
    
    modo = None
    for linha in linhas[1:]:
        linha = linha.strip()
        if not linha: continue
        
        if "Oferecem Carona:" in linha:
            modo = 'H'
            continue
        elif "Recebem Carona:" in linha:
            modo = 'M'
            continue
            
        if ':' in linha:
            partes = linha.split(':', 1)
            id_pessoa = int(partes[0].strip())
            dict_str = partes[1].strip()
            
            try:
                prefs_dict = ast.literal_eval(dict_str)
                prefs_lista = [k for k, v in sorted(prefs_dict.items(), key=lambda item: item[1])]
            except:
                prefs_lista = []
                
            if modo == 'H':
                H_pref[id_pessoa] = prefs_lista
            elif modo == 'M':
                M_pref[id_pessoa] = prefs_lista

    return H, M, H_pref, M_pref

def main():
    pasta_casos = "../casos_teste"
    
    if not os.path.exists(pasta_casos):
        print(f"Pasta '{pasta_casos}' não encontrada.")
        print("Por favor, execute 'gerador.py' primeiro para gerar os casos de teste.")
        return

    arquivos = [f for f in os.listdir(pasta_casos) if f.endswith('.txt')]
    if not arquivos:
        print("Nenhum caso de teste (.txt) encontrado no banco de dados.")
        return

    print("\nCASOS DE TESTE")
    for idx, arq in enumerate(arquivos):
        print(f"[{idx + 1}] {arq}")
    
    try:
        escolha = int(input("\nEscolha o número do caso de teste: ")) - 1
        if escolha < 0 or escolha >= len(arquivos):
            print("Escolha inválida.")
            return
    except ValueError:
        print("Entrada inválida. Digite um número.")
        return
        
    arquivo_escolhido = arquivos[escolha]
    caminho_completo = os.path.join(pasta_casos, arquivo_escolhido)
    
    print("\nABORDAGENS ALGORÍTMICAS")
    print("[1] Algoritmo de Gale-Shapley")
    print("[2] Local Search")
    
    try:
        alg_escolha = int(input("\nEscolha o número do algoritmo a ser executado: "))
        if alg_escolha not in [1, 2]:
            print("Escolha inválida.")
            return
    except ValueError:
        print("Entrada inválida. Digite um número.")
        return

    print(f"\nCarregando '{arquivo_escolhido}'...")
    H, M, H_pref, M_pref = carregar_caso_teste(caminho_completo)
    
    resultado = []
    nome_algoritmo = ""

    if alg_escolha == 1:
        print("Executando Algoritmo de Gale-Shapley...")
        nome_algoritmo = "Gale-Shapley"
        try:
            resultado = gale_shapley(H, M, H_pref, M_pref)
        except Exception as e:
            print(f"\n[!] ERRO INESPERADO NO GALE-SHAPLEY: {e}")
            return
            
    elif alg_escolha == 2:
        print("Executando Algoritmo de Local Search...")
    

    valor_solucao = len(resultado)
    
    relatorio = f"RESULTADO DO TESTE\n"
    relatorio += f"Algoritmo Utilizado: {nome_algoritmo}\n"
    relatorio += f"Caso de teste: {arquivo_escolhido}\n"
    relatorio += f"Total de Casamentos (Valor da Solução): {valor_solucao}\n"
    relatorio += f"Pares Formados (Motorista -> Passageiro):\n"
    
    if resultado:
        for h, m in resultado:
            relatorio += f"  - O funcionário {h} oferecerá carona para {m}\n"
    else:
        relatorio += "  - Nenhum par foi formado (ou algoritmo pendente de implementação).\n"
        
    print("\n" + relatorio)
    
    sufixo_alg = nome_algoritmo.lower().replace(" ", "_")
    nome_relatorio = f"relatorio_{sufixo_alg}_{arquivo_escolhido}"
    with open(nome_relatorio, 'w', encoding='utf-8') as f:
        f.write(relatorio)
    print(f"Relatório gravado em: {nome_relatorio}")

if __name__ == "__main__":
    main()