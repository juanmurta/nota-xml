import xmltodict
import pandas as pd
import openpyxl
import os


# ler o xml e pegar as informações desejadas modelo 55
def ler_xml(nota):
    with open(nota, 'rb') as arquivo:
        documento = xmltodict.parse(arquivo)
    dic_notafiscal = documento['nfeProc']['NFe']['infNFe']
    valor_total = dic_notafiscal['total']['ICMSTot']['vNF']
    cnpj_vendeu = dic_notafiscal['emit']['CNPJ']
    nome_vendeu = dic_notafiscal['emit']['xNome']
    cpf_comprou = dic_notafiscal['dest']['CPF']
    nome_comprou = dic_notafiscal['dest']['xNome']
    produtos = dic_notafiscal['det']
    lista_produtos = []

    for produto in produtos:
        valor_produto = produto['prod']['vProd']
        nome_produto = produto['prod']['xProd']
        lista_produtos.append((nome_produto, valor_produto))

    # passando os dados para um dicionario
    resposta = {'valor total': [valor_total],
                'cnpj_vendeu': [cnpj_vendeu],
                'nome_vendeu': [nome_vendeu],
                'cpf_comprou': [cpf_comprou],
                'nome_comprou': [nome_comprou],
                'lista_produtos': [lista_produtos]
                }
    return resposta

# ler o xml e pegar as informações desejadas nota de serviço
def ler_xml_servico(nota):
    with open(nota, 'rb') as arquivo:
        documento = xmltodict.parse(arquivo)
    dic_notafiscal = documento['ConsultarNfseResposta']['ListaNfse']['CompNfse']['Nfse']['InfNfse']
    valor_total = dic_notafiscal['Servico']['Valores']['ValorServicos']
    cnpj_vendeu = dic_notafiscal['PrestadorServico']['IdentificacaoPrestador']['Cnpj']
    nome_vendeu = dic_notafiscal['PrestadorServico']['RazaoSocial']
    cpf_comprou = dic_notafiscal['TomadorServico']['IdentificacaoTomador']['CpfCnpj']['Cnpj']
    nome_comprou = dic_notafiscal['TomadorServico']['RazaoSocial']
    produtos = dic_notafiscal['Servico']['Discriminacao']

    # passando os dados para um dicionario
    resposta = {'valor total': [valor_total],
                'cnpj_vendeu': [cnpj_vendeu],
                'nome_vendeu': [nome_vendeu],
                'cpf_comprou': [cpf_comprou],
                'nome_comprou': [nome_comprou],
                'lista_produtos': [produtos]
                }
    return resposta


lista_arquivos = os.listdir(r'E:\Python\python\Impressionador')

for arquivo in lista_arquivos:
    if 'xml' in arquivo:
        if 'DANFE' in arquivo:
            print(ler_xml(fr'E:\Python\python\Impressionador/{arquivo}'))
        else:
            print(ler_xml_servico(fr'E:\Python\python\Impressionador/{arquivo}'))


# converter informações
tabela = pd.DataFrame.from_dict(resposta)
tabela.to_excel('NFes.xlsx', index=False)
