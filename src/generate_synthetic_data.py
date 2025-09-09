# Script para gerar o dataset sintético
import os
import pandas as pd
import numpy as np
from datetime import datetime, timedelta, date
import random
from faker import Faker
import warnings
warnings.filterwarnings('ignore')

# Configuração inicial
np.random.seed(42)
random.seed(42)
fake = Faker('pt_BR')

# Definir parâmetros para geração dos dados
num_rows = 65000  # Mais de 60.000 linhas

# Criar listas para armazenar os dados
data = {
    'NUMCDC_VINCULADO': [],  # UC
    'SITUACAO_UC': [],
    'SITUACAO_CONTRATO_SIATE': [],
    'CODGRUPO_LEIT': [],
    'TIPO_UC': [],
    'CLIENTE': [],
    'NUMUC_OU_NUMRED': [],
    'CODIGO_RED': [],
    'DESCRICAO_DA_RED': [],
    'FATURA': [],
    'NUMFAT': [],
    'NUMANO_FAT': [],
    'NUMMES_FAT': [],
    'NUMANO_REF': [],
    'NUMMES_REF': [],
    'MES_ANO_REF': [],
    'REF': [],
    'DATA_VENCIMENTO': [],
    'DATA_ACAO_REAVISO': [],
    'DATA_PROTOCOLO_REAVISO': [],
    'DATA_PAGAMENTO': [],
    'DATA_BAIXA': [],
    'DIAS_VENCIDOS': [],
    'VALOR_IMPORTE': [],
    'VALOR_EMISSAO': [],
    'CODIGO_CLASSE': [],
    'DESCRICAO_CLASSE': [],
    'CODIGO_AGRUPAMENTO': [],
    'NOME_AGRUPAMENTO': [],
    'CODIGO_SUBCLASSE': [],
    'DSCCLS_IMP': [],
    'TIPOENVIO_CONTA': [],
    'CODIGO_DA_ATIVIDADE': [],
    'STATUS_HOSPITAL': [],
    'STATUS_ZONA_REMOTAS': []
}

# Função alternativa para gerar datas (compatível com Faker 37.6.0)
def gerar_data_entre(data_inicio, data_fim):
    """Gera uma data aleatória entre duas datas"""
    delta = data_fim - data_inicio
    dias_aleatorios = random.randint(0, delta.days)
    return data_inicio + timedelta(days=dias_aleatorios)

# Gerar dados básicos
ucs = [fake.unique.numerify(text='########') for _ in range(2000)]
codigos_red = [fake.numerify(text='###') for _ in range(3)]
descricoes_red = ['Parcelamento', 'Consumo Final', 'Outros']
classes = {
    1: 'Residencial', 
    2: 'Comercial', 
    3: 'Industrial', 
    4: 'Rural', 
    5: 'Poder Público', 
    6: 'Serviço Público', 
    7: 'Iluminação Pública'
}

# Subclasses
subclasses = {
    1: {1: 'Residencial'},
    2: {1: 'Comercial'},
    3: {1: 'Industrial'},
    4: {1: 'Rural'},
    5: {1: 'Municipal', 2: 'Estadual', 3: 'Federal'},
    6: {1: 'Serviço Público'},
    7: {1: 'Iluminação Pública'}
}

# Agrupamentos para classes 5, 6, 7
agrupamentos = list(range(1, 16))  # 1 a 15
nomes_agrupamentos = {
    1: 'PREFEITURA A',
    2: 'PREFEITURA B', 
    3: 'PREFEITURA C',
    4: 'GOVERNO ESTADUAL',
    5: 'UNIÃO FEDERAL',
    6: 'SANEAMENTO X',
    7: 'LIMPEZA URBANA Y',
    8: 'PAVIMENTAÇÃO Z',
    9: 'PREFEITURA X',
    10: 'EMPRESA DE SANEAMENTO W',
    11: 'SECRETARIA DE OBRAS',
    12: 'SECRETARIA DE SAÚDE',
    13: 'SECRETARIA DE EDUCAÇÃO',
    14: 'DEFESA CIVIL',
    15: 'DEPARTAMENTO DE TRÂNSITO'
}

# Nomes para diferentes tipos de clientes
nomes_pessoas = [fake.name() for _ in range(3000)]
nomes_empresas = [
    f"{fake.company()} {fake.company_suffix()}" for _ in range(1000)
] + [
    "Comércio de Alimentos LTDA", "Mercado Central", "Padaria Pão Quente",
    "Restaurante Sabor Caseiro", "Loja de Roupas Elegance", "Auto Peças Silva",
    "Farmácia Popular", "Construtora Horizonte", "Metalúrgica Industrial",
    "Agropecuária Campo Verde", "Fazenda Boa Esperança", "Indústria Textil"
]
nomes_orgaos_publicos = [
    "Prefeitura Municipal", "Câmara de Vereadores", "Secretaria de Educação",
    "Secretaria de Saúde", "Secretaria de Obras", "Departamento de Água e Esgoto",
    "Companhia de Saneamento", "Departamento de Iluminação Pública",
    "Secretaria de Meio Ambiente", "Defesa Civil Municipal", "Guarda Municipal",
    "Hospital Municipal", "Escola Municipal", "Creche Municipal", "Posto de Saúde",
    "Centro de Esportes", "Biblioteca Pública", "Museu Municipal"
]

# Códigos de atividade expandidos
codigos_atividade = [
    86101, 8610, 8620, 8690, 8510, 8520, 8530, 8540, 8550, 8560, 8570, 8580, 8590,
    4110, 4120, 4210, 4220, 4310, 4320, 4330, 4340, 4350, 4360, 4370, 4380, 4390,
    4710, 4720, 4730, 4740, 4750, 4760, 4770, 4780, 4790, 4910, 4920, 4930, 4940,
    4950, 4960, 4970, 4980, 4990, 5010, 5020, 5030, 5040, 5050, 5060, 5070, 5080,
    5090, 5110, 5120, 5130, 5140, 5150, 5160, 5170, 5180, 5190, 5210, 5220, 5230
]

nomelgr_options = ['ALD', 'NÃO ALD', 'OUTRA', 'SEM INFO', 'FAZEND', 'ASSENTAM']

print("Gerando dados... Isso pode levar alguns minutos.")

# Mapeamento de UC para cliente (para manter consistência)
uc_cliente_map = {}
uc_titularidade_mudou = {}

for uc in ucs:
    # 80% de chance de manter o mesmo cliente, 20% de mudar
    uc_titularidade_mudou[uc] = random.random() < 0.2

# Gerar os dados
for i in range(num_rows):
    if i % 10000 == 0:
        print(f"Processados {i} registros de {num_rows}...")
    
    # Dados básicos
    uc = random.choice(ucs)
    data['NUMCDC_VINCULADO'].append(uc)
    
    # Situação UC (80% ligada, 20% desligada)
    situacao_uc = 'LIGADA' if random.random() < 0.8 else 'DESLIGADA'
    data['SITUACAO_UC'].append(situacao_uc)
    
    # Situação contrato
    situacoes_contrato = ['CONTRATO_INATIVO', 'CONTRATO_ATIVO', 'CONTRATO_ENCERRADO']
    pesos_contrato = [0.1, 0.7, 0.2]
    situacao_contrato = random.choices(situacoes_contrato, weights=pesos_contrato, k=1)[0]
    data['SITUACAO_CONTRATO_SIATE'].append(situacao_contrato)
    
    # Código grupo leitura
    grupos_leitura = ['R', 'H', 'B', 'I']
    cod_grupo_leitura = random.choice(grupos_leitura)
    data['CODGRUPO_LEIT'].append(cod_grupo_leitura)
    
    # Escolher classe primeiro para determinar outros campos
    cod_classe = random.choice(list(classes.keys()))
    data['CODIGO_CLASSE'].append(cod_classe)
    data['DESCRICAO_CLASSE'].append(classes[cod_classe])
    
    # Tipo UC baseado no grupo de leitura e classe
    if cod_classe in [1, 2, 3, 4] and cod_grupo_leitura in ['R', 'H']:
        tipo_uc = 'GRUPO A'
    elif cod_classe in [5, 6, 7] and cod_grupo_leitura in ['R', 'H', 'B']:
        tipo_uc = 'PODER PUBLICO'
    else:
        tipo_uc = 'GRUPO B'
    data['TIPO_UC'].append(tipo_uc)
    
    # Escolher cliente baseado na classe
    if uc not in uc_cliente_map or uc_titularidade_mudou[uc]:
        if cod_classe in [5, 6, 7]:  # Órgãos públicos
            cliente = random.choice(nomes_orgaos_publicos)
        elif cod_classe in [2, 3, 4, 6]:  # Empresas
            cliente = random.choice(nomes_empresas)
        else:  # Pessoas (classes 1, 2, 4)
            cliente = random.choice(nomes_pessoas)
        uc_cliente_map[uc] = cliente
    else:
        cliente = uc_cliente_map[uc]
    
    data['CLIENTE'].append(cliente)
    
    # Código RED (30% de chance de ter código RED)
    if random.random() < 0.3:
        idx_red = random.randint(0, 2)
        codigo_red = codigos_red[idx_red]
        descricao_red = descricoes_red[idx_red]
        num_red = fake.unique.numerify(text='######')  # Número único
    else:
        codigo_red = None
        descricao_red = None
        num_red = uc  # Usa o NUMCDC_VINCULADO
    
    data['CODIGO_RED'].append(codigo_red)
    data['DESCRICAO_DA_RED'].append(descricao_red)
    data['NUMUC_OU_NUMRED'].append(num_red)
    
    # Datas e referências
    ano_ref = random.randint(2020, 2024)
    mes_ref = random.randint(1, 12)
    data['NUMANO_REF'].append(ano_ref)
    data['NUMMES_REF'].append(mes_ref)
    
    # Fatura e NUMFAT
    num_fat = fake.unique.numerify(text='########')
    data['NUMFAT'].append(num_fat)
    data['FATURA'].append(f"{uc}{ano_ref}{mes_ref:02d}")
    
    # Ano e mês da fatura
    data['NUMANO_FAT'].append(ano_ref)
    data['NUMMES_FAT'].append(mes_ref)
    
    # Mês/ano de referência
    data['MES_ANO_REF'].append(f"{mes_ref:02d}/{ano_ref}")
    data['REF'].append(f"01/{mes_ref:02d}/{ano_ref}")
    
    # Datas importantes
    data_inicio = date(ano_ref, mes_ref, 1)
    
    # Determinar o último dia do mês
    if mes_ref == 12:
        data_fim = date(ano_ref + 1, 1, 1) - timedelta(days=1)
    else:
        data_fim = date(ano_ref, mes_ref + 1, 1) - timedelta(days=1)
    
    data_vencimento = gerar_data_entre(data_inicio, data_fim)
    data['DATA_VENCIMENTO'].append(data_vencimento)
    
    # Data ação reaviso (50% de chance de ter)
    if random.random() < 0.5:
        data_acao_reaviso = data_vencimento + timedelta(days=random.randint(1, 15))
        data['DATA_ACAO_REAVISO'].append(data_acao_reaviso)
    else:
        data['DATA_ACAO_REAVISO'].append(None)
    
    # Data protocolo reaviso (30% de chance de ter)
    if random.random() < 0.3:
        if data['DATA_ACAO_REAVISO'][-1] is not None:
            data_protocolo = data['DATA_ACAO_REAVISO'][-1] + timedelta(days=random.randint(1, 5))
            data['DATA_PROTOCOLO_REAVISO'].append(data_protocolo)
        else:
            data['DATA_PROTOCOLO_REAVISO'].append(None)
    else:
        data['DATA_PROTOCOLO_REAVISO'].append(None)
    
    # Data pagamento (80% de chance de ter pago)
    if random.random() < 0.8:
        # Permite pagamento de até 15 dias antes até 60 dias depois do vencimento
        dias_apos_vencimento = random.randint(-15, 60)
        data_pagamento = data_vencimento + timedelta(days=dias_apos_vencimento)
        data['DATA_PAGAMENTO'].append(data_pagamento)
        data['DIAS_VENCIDOS'].append(dias_apos_vencimento)
    else:
        data['DATA_PAGAMENTO'].append(None)
        # Para não pagos, calcula dias desde o vencimento até hoje
        data['DIAS_VENCIDOS'].append((date.today() - data_vencimento).days)
    
    # Data baixa (se tem pagamento, tem baixa)
    if data['DATA_PAGAMENTO'][-1] is not None:
        data_baixa = data['DATA_PAGAMENTO'][-1] + timedelta(days=random.randint(0, 3))
        data['DATA_BAIXA'].append(data_baixa)
    else:
        data['DATA_BAIXA'].append(None)
    
    # Valores equilibrados por classe (emissão = bruto, importe = líquido)
    # Define faixas de valor por classe para evitar outliers
    faixas_valor = {
        1: (100, 800),        # Residencial: R$ 100-800
        2: (600, 30000),      # Comercial: R$ 600-30.000
        3: (5000, 200000),     # Industrial: R$ 5.000-200.000
        4: (200, 10000),      # Rural: R$ 200-10.000
        5: (1000, 50000),    # Poder Público: R$ 1.000-50.000
        6: (800, 20000),     # Serviço Público: R$ 800-20.000
        7: (300, 10000)      # Iluminação Pública: R$ 300-10.000
    }

    # Valor de emissão (bruto) baseado na classe
    min_valor, max_valor = faixas_valor[cod_classe]
    valor_emissao = round(random.uniform(min_valor, max_valor), 2)

    # Para 5% dos casos, permite valores maiores (até 1 milhão) para classes institucionais
    if random.random() < 0.05 and cod_classe in [5, 6, 3]:
        valor_emissao = round(random.uniform(10000, 1000000), 2)

    data['VALOR_EMISSAO'].append(valor_emissao)

    # Valor importe (líquido) - SEMPRE menor ou igual à emissão (com descontos)
    # Em 70% dos casos tem desconto, em 30% paga valor integral
    if random.random() < 0.7:
        # Desconto de 1% a 15%
        desconto_percentual = random.uniform(0.01, 0.15)
        valor_importe = round(valor_emissao * (1 - desconto_percentual), 2)
    else:
        # Paga valor integral
        valor_importe = valor_emissao

    data['VALOR_IMPORTE'].append(valor_importe)
    
    # Código de agrupamento e nome (apenas para classes 5, 6, 7)
    if cod_classe in [5, 6, 7]:
        cod_agrupamento = random.choice(agrupamentos)
        nome_agrupamento = nomes_agrupamentos[cod_agrupamento]
    else:
        cod_agrupamento = None
        nome_agrupamento = None
    
    data['CODIGO_AGRUPAMENTO'].append(cod_agrupamento)
    data['NOME_AGRUPAMENTO'].append(nome_agrupamento)
    
    # Código e descrição da subclasse
    if cod_classe in subclasses:
        cod_subclasse = random.choice(list(subclasses[cod_classe].keys()))
        desc_subclasse = subclasses[cod_classe][cod_subclasse]
        data['CODIGO_SUBCLASSE'].append(cod_subclasse)
        data['DSCCLS_IMP'].append(desc_subclasse)
    else:
        data['CODIGO_SUBCLASSE'].append(None)
        data['DSCCLS_IMP'].append(None)
    
    # Tipo envio conta
    tipos_envio = ['Email', 'Correio', 'Online', 'Física']
    data['TIPOENVIO_CONTA'].append(random.choice(tipos_envio))
    
    # Código da atividade
    cod_atividade = random.choice(codigos_atividade)
    data['CODIGO_DA_ATIVIDADE'].append(cod_atividade)
    
    # Status hospital
    status_hospital = 'SIM' if cod_atividade in [86101, 8610] else 'NAO'
    data['STATUS_HOSPITAL'].append(status_hospital)
    
    # Status zona remotas - só classe 4 (Rural) pode ter SIM
    nomelgr = random.choice(nomelgr_options)
    if cod_classe == 4:  # Apenas classe Rural
        status_zona_remota = 'SIM' if any(x in nomelgr for x in ['ALD', 'FAZEND', 'ASSENTAM']) else 'NÃO'
    else:
        status_zona_remota = 'NÃO'  # Para outras classes, sempre NÃO
    data['STATUS_ZONA_REMOTAS'].append(status_zona_remota)

print("Dados gerados. Criando DataFrame...")

# Criar DataFrame
df = pd.DataFrame(data)

# Reordenar as colunas conforme a query SQL
colunas_ordenadas = [
    'NUMCDC_VINCULADO', 'SITUACAO_UC', 'SITUACAO_CONTRATO_SIATE', 'CODGRUPO_LEIT', 'TIPO_UC',
    'CLIENTE', 'NUMUC_OU_NUMRED', 'CODIGO_RED', 'DESCRICAO_DA_RED', 'FATURA', 'NUMFAT',
    'NUMANO_FAT', 'NUMMES_FAT', 'NUMANO_REF', 'NUMMES_REF', 'MES_ANO_REF', 'REF',
    'DATA_VENCIMENTO', 'DATA_ACAO_REAVISO', 'DATA_PROTOCOLO_REAVISO', 'DATA_PAGAMENTO',
    'DATA_BAIXA', 'DIAS_VENCIDOS', 'VALOR_IMPORTE', 'VALOR_EMISSAO', 'CODIGO_CLASSE',
    'DESCRICAO_CLASSE', 'CODIGO_AGRUPAMENTO', 'NOME_AGRUPAMENTO', 'CODIGO_SUBCLASSE',
    'DSCCLS_IMP', 'TIPOENVIO_CONTA', 'CODIGO_DA_ATIVIDADE', 'STATUS_HOSPITAL', 'STATUS_ZONA_REMOTAS'
]

df = df[colunas_ordenadas]

# Salvar como Parquet com compressão Brotli
nome_arquivo_parquet = fr'data\raw\historico_pagamento_contas_energia.parquet'
df.to_parquet(nome_arquivo_parquet, compression='brotli', index=False)

print(f"Base de dados gerada com sucesso!")
print(f"Arquivo Parquet salvo como: '{nome_arquivo_parquet}'")
print(f"Tamanho do dataset: {len(df)} linhas e {len(df.columns)} colunas")

# Mostrar uma amostra dos dados
print("\nPrimeiras 5 linhas do dataset:")
print(df.head())

# Mostrar informações sobre os arquivos
print(f"Tamanho do arquivo Parquet: {os.path.getsize(nome_arquivo_parquet) / 1024 / 1024:.2f} MB")