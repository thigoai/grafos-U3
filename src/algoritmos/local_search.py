import algoritmos.gale_shapley as gale_shapley
import utils.gerador as gerador

# dado um casamento C = [(m_1, w_1)...(m_i, w_i)] 
# Um conjunto H, de homens
# Um conjunto M, de mulheres
# Ranks de preferência H_rank, M_rank
# -> Encontrar pares bloqueadores.
def pares_bloqueadores(C, H, M, H_rank, M_rank):
    pb = []

    def H_par(h):
        for h2, m in C:
            if h2 == h:
                return m
        return None

    def M_par(m):
        for h, m2 in C:
            if m2 == m:
                return h
        return None

    for h in H:
        for m in M:
            if (h, m) in C:
                continue

            if H_rank[h].get(m, 10000000) < H_rank[h][H_par(h)]:
                if M_rank[m].get(h, 1000000) < M_rank[m][M_par(m)]:
                    pb.append((h,m))

    return pb

if __name__ == "__main__":
    rh, rm = gerador.gerar_caso_teste(50,50,0.3,0.3)  

    H = range(50)
    M = range(50)

    C = gale_shapley.gale_shapley(H, M, rh, rm)

    print(C)
    print(pares_bloqueadores(C, H, M, rh, rm))
