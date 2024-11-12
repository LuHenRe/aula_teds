def duracao(xi, yi, xf, yf):
    if yi > yf and xi < xf:
        return (f"O JOGO DUROU {xf-xi-1} HORA(S) E {60-(yi-yf)} MINUTO(S)")
    elif xi > xf and yi > yf:
        return (f"O JOGO DUROU {24-xi-xf} HORA(S) E {yi-yf} MINUTOS(S)")
    elif xi > xf and yi < yf:
        return (f"O JOGO DUROU {24-xi-xf} HORA(S) E {yf-yi} MINUTOS(S)")
    elif xi == xf and yi == yf:
        return (f"O JOGO DUROU {24+xf-xi} HORA(S) E {yf-yi} MINUTO(S)")
    else:
        return (f"O JOGO DUROU {xf-xi} HORA(S) E {yf-yi} MINUTO(S)")

HI, MI, HF, MF = map(int, input().split())
print(duracao(HI, MI, HF, MF))
