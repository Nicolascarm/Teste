faturamento_diario = [22174.1664, 24537.6698, 26139.6134, 0.0, 0.0, 26742.6612, 0.0, 42889.2258, 46251.174, 11191.4722, 0.0, 0.0, 3847.4823, 373.7838, 2659.7563,
          48924.2448, 18419.2614, 0.0, 0.0, 35240.1826, 43829.1667, 18235.6852, 4355.0662, 13327.1025, 0.0, 0.0, 25681.8318, 1718.1221, 13220.495, 8414.61]

menor_faturamento_diario = min(filter(lambda x: x > 0, faturamento_diario))

maior_faturamento_diario = max(filter(lambda x: x > 0, faturamento_diario))

media_faturamento_diario = sum(filter(lambda x: x > 0, faturamento_diario)) / len(list(filter(lambda x: x > 0, faturamento_diario)))

dias_acima_da_media = len(list(filter(lambda x: x > media_faturamento_diario, faturamento_diario)))

print("Menor valor de faturamento diário: R$ {:.2f}".format(menor_faturamento_diario))
print("Maior valor de faturamento diário: R$ {:.2f}".format(maior_faturamento_diario))
print("Número de dias com faturamento acima da média mensal: {}".format(dias_acima_da_media))
