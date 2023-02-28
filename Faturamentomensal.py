faturamento_estados = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}

valor_total = sum(faturamento_estados.values())

percentual_estados = {}
for estado, faturamento in faturamento_estados.items():
    percentual = (faturamento / valor_total) * 100
    percentual_estados[estado] = percentual

for estado, percentual in percentual_estados.items():
    print(f'{estado}: {percentual:.2f}%')
