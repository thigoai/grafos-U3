import ast
import os


def carregar_caso_teste(caminho_arquivo):
    with open(caminho_arquivo, 'r', encoding='utf-8') as f:
        linhas = f.readlines()

    n, m = map(int, linhas[0].strip().split())
    H = list(range(n))
    M = list(range(m))

    H_rank = [{} for _ in range(n)]
    M_rank = [{} for _ in range(m)]

    modo = None
    for linha in linhas[1:]:
        linha = linha.strip()
        if not linha:
            continue

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
            except (ValueError, SyntaxError):
                prefs_dict = {}

            if modo == 'H':
                H_rank[id_pessoa] = prefs_dict
            elif modo == 'M':
                M_rank[id_pessoa] = prefs_dict

    return H, M, H_rank, M_rank


def listar_casos_teste(pasta, prefixo_excluir='teste_N'):
    return [
        f for f in os.listdir(pasta)
        if f.endswith('.txt') and not f.startswith(prefixo_excluir)
    ]

def salvar_relatorio(nome_algoritmo, nome_arquivo, resultado):
    valor_solucao = len(resultado)
    relatorio = (
        f"RESULTADO DO TESTE\n"
        f"Algoritmo Utilizado: {nome_algoritmo}\n"
        f"Caso de teste: {nome_arquivo}\n"
        f"Total de Casamentos: {valor_solucao}\n"
        f"Pares Formados (Motorista -> Passageiro):\n"
    )

    if resultado:
        for h, m in resultado:
            relatorio += f"  - O funcionário {h} oferecerá carona para {m}\n"
    else:
        relatorio += "  - Nenhum par foi formado.\n"

    nome_base = f"relatorio_{nome_algoritmo.lower().replace(' ', '_')}_{nome_arquivo}"
    
    pasta_relatorios = "../relatorios"
    os.makedirs(pasta_relatorios, exist_ok=True)
    
    nome_relatorio = os.path.join(pasta_relatorios, nome_base)

    with open(nome_relatorio, 'w', encoding='utf-8') as f:
        f.write(relatorio)

    return relatorio, nome_relatorio

def salvar_log_analise(tamanhos, tempos, nome_algoritmo):
    """Salva os tempos de execução da análise em um arquivo de texto."""
    pasta_relatorios = "../relatorios"
    os.makedirs(pasta_relatorios, exist_ok=True)
    
    nome_arquivo = os.path.join(
        pasta_relatorios, 
        f"log_tempos_{nome_algoritmo.lower().replace(' ', '_')}.txt"
    )

    with open(nome_arquivo, 'w', encoding='utf-8') as f:
        f.write(f"Analisando {nome_algoritmo}...\n")
        for n, tempo in zip(tamanhos, tempos):
            f.write(f"N={n:<4} | {tempo:.4f} segundos.\n")
            
    print(f"Log de tempos salvo em: {nome_arquivo}")
    return nome_arquivo

def imprimir_grafico_terminal(xs, ys, max_largura=50, nome_algoritmo="Gale-Shapley"):
    print("\n" + "=" * 65)
    print(f"TEMPO DE EXECUÇÃO")
    print("=" * 65)

    max_y = max(ys) if max(ys) > 0 else 0.0001

    for x, y in zip(xs, ys):
        tamanho_barra = int((y / max_y) * max_largura)
        barra = "█" * tamanho_barra
        print(f" N={x:<4} | {barra} {y:.4f}s")

    print("=" * 65 + "\n")