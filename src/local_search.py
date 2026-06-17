import gale_shapley
import gerador
import random

INF = 10**9

def local_search(H, M, H_rank, M_rank, n_passos):

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
    
                if  H_rank[h].get(m, INF) < H_rank[h].get(h_conj, INF) and M_rank[m].get(h, INF) < M_rank[m].get(m_conj, INF):
                    pb.append((h, m))
    
    
        pb_reduzido = {}
        for h, m in pb:
            if h not in pb_reduzido or H_rank[h].get(m, INF) < H_rank[h].get(pb_reduzido[h], INF):
                pb_reduzido[h] = m
    
        return list(pb_reduzido.items())

    def casamento_aleatorio():
        H_list = list(H)
        M_list = list(M)
        random.shuffle(H_list)
        random.shuffle(M_list)
    
        n = random.randint(0, min(len(H), len(M)))
    
        return [(H[i], M[i]) for i in range(n)]

    def vizinhos(C, pb):
        viz = []

        for h, m in pb:
            novo = [(h2, m2) for (h2, m2) in C if h2 != h and m2 != m]
            novo.append((h, m))
            viz.append(novo)

        return viz

    def pontos(C, pb):
        casados = set()
    
        for h, m in C:
            casados.add(h)
            casados.add(m)
    
        solteiros = (set(H) | set(M)) - casados
    
        return len(solteiros) + len(pb)


    atual = casamento_aleatorio()
    atual_pb = pares_bloqueadores(atual)
    atual_pontos = pontos(atual, atual_pb)

    final = atual
    final_pb = atual_pb
    final_pontos = atual_pontos

    for i in range(n_passos):
        print("step: " + str(i))
        melhor_viz = atual
        melhor_pb = atual_pb
        melhor_pontos = atual_pontos

        vizs = vizinhos(atual, atual_pb)

        if random.random() < 0.2:
            melhor_viz = random.choice(vizs)
            melhor_pb = pares_bloqueadores(melhor_viz)
            melhor_pontos = pontos(melhor_viz, melhor_pb)

            continue

        for viz in vizs:
            viz_pb = pares_bloqueadores(viz)
            viz_pontos = pontos(viz, viz_pb)

            if  viz_pontos < melhor_pontos:
                melhor_viz = viz
                melhor_pb = viz_pb
                melhor_pontos = viz_pontos

        if not atual_pb:
            if atual_pontos < final_pontos:
                final = atual
                final_pb = atual_pb
                final_pontos = atual_pontos

                atual = casamento_aleatorio()
                atual_pb = pares_bloqueadores(atual)
                atual_pontos = pontos(atual, atual_pb)

                continue

        atual = melhor_viz
        atual_pb = melhor_pb
        atual_pontos = melhor_pontos

    if atual_pontos < final_pontos:
        return atual
    else:
        return final

if __name__ == "__main__":
    rh, rm = gerador.gerar_caso_teste(50,50,0.4, 0.4)  

    H = range(50)
    M = range(50)

    ls = local_search(H, M, rh, rm, 1000)
    print(ls)
    print(len(ls))
