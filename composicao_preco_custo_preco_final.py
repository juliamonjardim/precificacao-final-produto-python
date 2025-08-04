# Na Prática, Introdução a Lógica de Programação e ambiente Python
# Programa de auxilio ao calculo do preço de custo e preço final

# v_couro = valor do couro para fabricação unitária
v_couro = float(input('Digite o valor do COURO: '))
# v_solado = valor do solado para fabricação unitária
v_solado = float(input('Digite o valor do SOLADO: '))
# v_cordoes = valor de cordões e ilhoses para fabricação unitária
v_cordoes = float(input('Digite o valor de CORDÕES E ILHOSES: '))
# v_insumos = valor dos insumos diversos para fabricação unitária
v_insumos = float(input('Digite o valor de INSUMOS: '))
# v_MaoObra = valor de mão de obra para fabricação unitária
v_MaoObra = float(input('Digite o valor da MÃO DE OBRA: '))
# v_marketing = valor de Marketing e Propaganda dividido pela produção
v_marketing = float(input('Digite o valor de MARKETING: '))
# v_vendas = valor do custo de vendas dividido pela produção
v_vendas = float(input('Digite o valor dos CUSTOS DE VENDA: '))

# CALCULO DO PREÇO DE CUSTO
preco_custo = (v_couro*0.30)+(v_solado*0.20)+(v_cordoes*0.05)+(v_insumos*0.05)+(v_MaoObra*0.20)+(v_marketing*0.10)+(v_vendas*0.10)
print('O preço de custo unitário deste modelo de sapato é: R$ {preco_custo:.2f}')

# CALCULANDO O PREÇO FINAL:
# CALCULO DO PREÇO ADICIONANDO LUCRO DO FABRICANTE
Preco_Lucro= preco_custo*1.30
# CALCULO DO PREÇO ADICIONANDO PERDAS DE CAPITAL
Preco_Perdas= Preco_Lucro*1.15
# CALCULO DO PREÇO ADICIONANDO IMPOSTOS FEDERAIS
Preco_IPI_CONFINS= Preco_Perdas*1.15
# CALCULO DO PREÇO ADICIONANDO MARGEM DE VENDAS
Preco_Venda= Preco_IPI_CONFINS*1.25
# CALCULO DO PREÇO ADICIONANDO IMPOSTOS ESTADUAIS E MUNICIPAIS
Preco_ICMS_INSS= Preco_Venda*1.30

# PREÇO FINAL, ACRESCIDO DE TODOS OS IMPOSTOS E MARGENS DE LUCRO
Preco_FINAL = Preco_ICMS_INSS
print('O preço final ao consumidor deste modelo de sapato é: R$ {preco_FINAL:.2f}')
