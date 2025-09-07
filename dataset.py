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
    'NOMEDST': [],
    'DSCCLS_IMP': [],
    'TIPOENVIO_CONTA': [],
    'CODIGO_DA_ATIVIDADE': [],
    'STATUS_HOSPITAL': [],
    'ALDEIA': []
}

# Função alternativa para gerar datas (compatível com Faker 37.6.0)
def gerar_data_entre(data_inicio, data_fim):
    """Gera uma data aleatória entre duas datas"""
    delta = data_fim - data_inicio
    dias_aleatorios = random.randint(0, delta.days)
    return data_inicio + timedelta(days=dias_aleatorios)

# Gerar dados básicos
ucs = [fake.unique.numerify(text='########') for _ in range(2000)]
clientes = [fake.name() for _ in range(5000)]
codigos_red = [fake.numerify(text='###') for _ in range(10)]
descricoes_red = ['Comercial', 'Residencial', 'Industrial', 'Rural', 'Poder Público', 
                  'Iluminação Pública', 'Serviço Público', 'Agricultura', 'Comércio', 'Indústria']
classes = {
    1: 'Residencial', 
    2: 'Comercial', 
    3: 'Industrial', 
    4: 'Rural', 
    5: 'Poder Público', 
    6: 'Serviço Público', 
    7: 'Iluminação Pública'
}
agrupamentos = [fake.numerify(text='##') for _ in range(5)]
nomelgr_options = ['ALD', 'NÃO ALD', 'OUTRA', 'SEM INFO']

print("Gerando dados... Isso pode levar alguns minutos.")

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
    grupos_leitura = ['R', 'H', 'B', 'C', 'I']
    cod_grupo_leitura = random.choice(grupos_leitura)
    data['CODGRUPO_LEIT'].append(cod_grupo_leitura)
    
    # Tipo UC
    if cod_grupo_leitura in ['R', 'H'] and random.random() < 0.8:
        tipo_uc = 'GRUPO A'
    elif cod_grupo_leitura in ['R', 'H', 'B'] and random.random() < 0.2:
        tipo_uc = 'PODER PUBLICO'
    else:
        tipo_uc = 'GRUPO B'
    data['TIPO_UC'].append(tipo_uc)
    
    # Cliente
    data['CLIENTE'].append(random.choice(clientes))
    
    # Número UC ou número RED (50% de chance para cada)
    if random.random() < 0.5:
        data['NUMUC_OU_NUMRED'].append(uc)
    else:
        data['NUMUC_OU_NUMRED'].append(fake.numerify(text='######'))
    
    # Código RED e descrição
    idx_red = random.randint(0, 9)
    data['CODIGO_RED'].append(codigos_red[idx_red])
    data['DESCRICAO_DA_RED'].append(descricoes_red[idx_red])
    
    # Datas e referências
    ano_ref = random.randint(2020, 2024)
    mes_ref = random.randint(1, 12)
    data['NUMANO_REF'].append(ano_ref)
    data['NUMMES_REF'].append(mes_ref)
    
    # Fatura
    num_fat = fake.numerify(text='########')
    data['NUMFAT'].append(num_fat)
    data['FATURA'].append(f"{uc}{ano_ref}{mes_ref:02d}")
    
    # Ano e mês da fatura (podem ser diferentes da referência)
    data['NUMANO_FAT'].append(ano_ref)
    data['NUMMES_FAT'].append(mes_ref)
    
    # Mês/ano de referência
    data['MES_ANO_REF'].append(f"{mes_ref:02d}/{ano_ref}")
    data['REF'].append(f"01/{mes_ref:02d}/{ano_ref}")
    
    # Datas importantes - CORREÇÃO AQUI
    # Usando a função personalizada em vez de fake.date_between
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
        dias_apos_vencimento = random.randint(0, 60)
        data_pagamento = data_vencimento + timedelta(days=dias_apos_vencimento)
        data['DATA_PAGAMENTO'].append(data_pagamento)
        data['DIAS_VENCIDOS'].append(dias_apos_vencimento)
    else:
        data['DATA_PAGAMENTO'].append(None)
        data['DIAS_VENCIDOS'].append((date.today() - data_vencimento).days)
    
    # Data baixa (se tem pagamento, tem baixa)
    if data['DATA_PAGAMENTO'][-1] is not None:
        data_baixa = data['DATA_PAGAMENTO'][-1] + timedelta(days=random.randint(0, 3))
        data['DATA_BAIXA'].append(data_baixa)
    else:
        data['DATA_BAIXA'].append(None)
    
    # Valores
    valor_emissao = round(random.uniform(50, 1500), 2)
    data['VALOR_EMISSAO'].append(valor_emissao)
    
    # Valor importe (pode ter acréscimos)
    acrescimos = round(random.uniform(0, 100), 2)
    valor_importe = valor_emissao + acrescimos
    data['VALOR_IMPORTE'].append(round(valor_importe, 2))
    
    # Código e descrição da classe
    cod_classe = random.choice(list(classes.keys()))
    data['CODIGO_CLASSE'].append(cod_classe)
    data['DESCRICAO_CLASSE'].append(classes[cod_classe])
    
    # Código de agrupamento
    data['CODIGO_AGRUPAMENTO'].append(random.choice(agrupamentos))
    
    # Nome DST
    data['NOMEDST'].append(fake.city())
    
    # Descrição classe impressa
    data['DSCCLS_IMP'].append(classes[cod_classe])
    
    # Tipo envio conta
    tipos_envio = ['Email', 'Correio', 'Online', 'Física']
    data['TIPOENVIO_CONTA'].append(random.choice(tipos_envio))
    
    # Código da atividade
    cod_atividade = random.choice([86101, 8610, 8620, 8690, 8510])
    data['CODIGO_DA_ATIVIDADE'].append(cod_atividade)
    
    # Status hospital
    status_hospital = 'SIM' if cod_atividade in [86101, 8610] else 'NAO'
    data['STATUS_HOSPITAL'].append(status_hospital)
    
    # Aldeia
    nomelgr = random.choice(nomelgr_options)
    aldeia = 'SIM' if 'ALD' in nomelgr else 'NÃO'
    data['ALDEIA'].append(aldeia)

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
    'DESCRICAO_CLASSE', 'CODIGO_AGRUPAMENTO', 'NOMEDST', 'DSCCLS_IMP', 'TIPOENVIO_CONTA',
    'CODIGO_DA_ATIVIDADE', 'STATUS_HOSPITAL', 'ALDEIA'
]

df = df[colunas_ordenadas]

# Salvar como Excel
nome_arquivo = 'historico_pagamento_contas_energia.xlsx'
df.to_excel(nome_arquivo, index=False, engine='openpyxl')

print(f"Base de dados gerada com sucesso! Arquivo salvo como '{nome_arquivo}'")
print(f"Tamanho do dataset: {len(df)} linhas e {len(df.columns)} colunas")

# Mostrar uma amostra dos dados
print("\nPrimeiras 5 linhas do dataset:")
print(df.head())