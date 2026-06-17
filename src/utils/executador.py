from algoritmos.gale_shapley import gale_shapley
# from algoritmos.local_search import local_search

ALGORITMOS = {
    1: "Gale-Shapley",
    2: "Local Search",
}


def executar(alg_escolha, H, M, H_pref, M_pref):
    """
    Executa o algoritmo selecionado e retorna (nome_algoritmo, resultado).

    Parâmetros
    ----------
    alg_escolha : int
        Índice do algoritmo (ver ALGORITMOS).
    H, M : list
        Listas de IDs dos grupos.
    H_pref, M_pref : list[dict]
        Rankings de preferência de cada participante.

    Retorna
    -------
    tuple[str, list]
        Nome do algoritmo usado e lista de pares formados.

    Raises
    ------
    ValueError
        Se alg_escolha não corresponder a nenhum algoritmo disponível.
    NotImplementedError
        Se o algoritmo ainda não estiver implementado.
    """
    nome = ALGORITMOS.get(alg_escolha)
    if nome is None:
        raise ValueError(f"Algoritmo {alg_escolha} não reconhecido.")

    if alg_escolha == 1:
        resultado = gale_shapley(H, M, H_pref, M_pref)
    elif alg_escolha == 2:
        raise NotImplementedError("Local Search ainda não implementado.")

    return nome, resultado


def menu_algoritmos():
    """Imprime as opções de algoritmo e retorna a escolha do usuário."""
    print("\nABORDAGENS ALGORÍTMICAS")
    for idx, nome in ALGORITMOS.items():
        print(f"[{idx}] {nome}")
    return int(input("\nEscolha o algoritmo a ser executado: "))