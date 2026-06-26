from utils.gerador import *
import random

INF = 10**9

def local_search(H, M, H_rank, M_rank, n_passos):
    H, M = list(H), list(M)
    genero_dominante = 'M'

    def pares_bloqueadores(C):
        pb = []
        conjuge = {}
        for h, m in C:
            conjuge[h] = m 
            conjuge[m] = h
    
        for h in H:
            for m in M:
                if conjuge.get(h) == m:
                    continue
                h_conj = conjuge.get(h)
                m_conj = conjuge.get(m)
    
                if H_rank[h].get(m, INF) < H_rank[h].get(h_conj, INF) and M_rank[m].get(h, INF) < M_rank[m].get(m_conj, INF):
                    pb.append((h, m))
        return pb
    
    def pares_bloqueadores_undom(pb): 
        nonlocal genero_dominante
        if genero_dominante == 'H':
            rank_pri, rank_sec = H_rank, M_rank
            index_pri, index_sec = 0, 1
            genero_dominante = 'M'  
        else:
            rank_pri, rank_sec = M_rank, H_rank
            index_pri, index_sec = 1, 0
            genero_dominante = 'H'  

        melhor_prim = {}
        for h, m in pb:
            a = h if index_pri == 0 else m
            b = m if index_pri == 0 else h
            if a not in melhor_prim or rank_pri[a][b] < rank_pri[a][melhor_prim[a]]:
                melhor_prim[a] = b

        candidatos = [(h, melhor_prim[h]) for h in melhor_prim] if index_pri == 0 else [(melhor_prim[m], m) for m in melhor_prim]

        melhor_sec = {}
        for h, m in candidatos:
            a = h if index_sec == 0 else m
            b = m if index_sec == 0 else h
            if a not in melhor_sec or rank_sec[a][b] < rank_sec[a][melhor_sec[a]]:
                melhor_sec[a] = b

        final_pb = [(h, melhor_sec[h]) for h in melhor_sec] if index_sec == 0 else [(melhor_sec[m], m) for m in melhor_sec]
        return final_pb

    def casamento_aleatorio():
        H_list, M_list = list(H), list(M)
        random.shuffle(H_list)
        random.shuffle(M_list)
        n = random.randint(0, min(len(H_list), len(M_list)))
        return [(H_list[i], M_list[i]) for i in range(n)] 

    def vizinhos(C, upb):
        viz = []
        for h, m in upb:
            novo = [(h2, m2) for (h2, m2) in C if h2 != h and m2 != m]
            novo.append((h, m))
            viz.append(novo)
        return viz

    def solteiros(C):
        casados = set()
        for h, m in C:
            casados.add(h)
            casados.add(m)
        return (set(H) | set(M)) - casados

    def pontos(C, pb):
        envolvidos_em_pb = set()
        for h, m in pb:
            envolvidos_em_pb.add(h)
            envolvidos_em_pb.add(m)

        return len(solteiros(C) - envolvidos_em_pb) + len(pb)

    atual = casamento_aleatorio()
    atual_pb = pares_bloqueadores(atual)
    atual_upb = pares_bloqueadores_undom(atual_pb)
    atual_pontos = pontos(atual, atual_pb) 

    melhor_estavel = None
    melhor_estavel_solteiros = INF

    for i in range(n_passos):
        
        if not atual_pb: 
            s = len(solteiros(atual))
            if s < melhor_estavel_solteiros:
                melhor_estavel = atual.copy()
                melhor_estavel_solteiros = s

            atual = casamento_aleatorio()
            atual_pb = pares_bloqueadores(atual)
            atual_upb = pares_bloqueadores_undom(atual_pb)
            atual_pontos = pontos(atual, atual_pb)
            continue

        vizs = vizinhos(atual, atual_upb)

        if vizs and random.random() < 0.2:
            atual = random.choice(vizs)
            atual_pb = pares_bloqueadores(atual)
            atual_upb = pares_bloqueadores_undom(atual_pb)
            atual_pontos = pontos(atual, atual_pb)
            continue

        melhor_viz = atual
        melhor_pb = atual_pb
        melhor_upb = atual_upb
        melhor_pontos = atual_pontos

        for viz in vizs:
            viz_pb = pares_bloqueadores(viz)
            viz_upb = pares_bloqueadores_undom(viz_pb)
            viz_pontos = pontos(viz, viz_pb)

            if viz_pontos < melhor_pontos:
                melhor_viz = viz
                melhor_pb = viz_pb
                melhor_upb = viz_upb
                melhor_pontos = viz_pontos

        atual = melhor_viz
        atual_pb = melhor_pb
        atual_upb = melhor_upb
        atual_pontos = melhor_pontos

    return melhor_estavel if melhor_estavel else atual