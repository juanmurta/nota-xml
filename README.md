# 💻 Ler xml de notas fiscais

# 📕 Descrição
Este projeto consiste em um script Python para extrair informações de arquivos XML de notas fiscais (modelo 55 e notas de serviço) e convertê-las em uma tabela Excel. Ele utiliza as bibliotecas xmltodict, pandas, e openpyxl para manipulação de dados e exportação. O script identifica automaticamente os arquivos XML na pasta especificada, processa as informações relevantes, como valores totais, CNPJ/CPF, nomes das partes envolvidas, e detalhes dos produtos ou serviços, e gera uma planilha Excel consolidada.

# ☕ Como Usar
1. Instale as dependências necessárias:
  - Execute pip install xmltodict pandas openpyxl no terminal para instalar as bibliotecas necessárias.
  - Organize os arquivos XML:
  - Coloque os arquivos XML das notas fiscais na pasta especificada no código (por padrão, E:\Python\python\Impressionador).
  - Edite o caminho da pasta:
  - Ajuste o caminho da variável lista_arquivos no script para apontar para a pasta onde estão os arquivos XML.
  - Execute o script:
  - Execute o script Python em seu ambiente de desenvolvimento ou terminal.
  - Saída gerada:
  - O script criará um arquivo Excel chamado NFes.xlsx na mesma pasta do script, contendo as informações extraídas.

# 🛠️ Funcionalidades
1. Processamento de Notas Fiscais Modelo 55:
2. Extrai informações como valor total, CNPJ do emitente, nome do emitente, CPF do destinatário, nome do destinatário e lista de produtos (nome e valor).
3. Processamento de Notas de Serviço:
4. Extrai informações como valor total do serviço, CNPJ do prestador, nome do prestador, CPF/CNPJ do tomador, nome do tomador e discriminação dos serviços.
4. Exportação para Excel:
5. Converte os dados extraídos em uma tabela Excel organizada.

# 🚨 Observações Importantes
Certifique-se de que os arquivos XML seguem os padrões esperados (modelo 55 ou nota de serviço). Caso contrário, o script pode gerar erros.
O script assume que os arquivos XML têm extensões .xml e utiliza palavras-chave como 'DANFE' para diferenciar entre notas fiscais modelo 55 e notas de serviço.
Para evitar sobrescrita acidental, renomeie ou mova o arquivo gerado (NFes.xlsx) antes de executar o script novamente.

# Contribuindo para api-flask-faturamento
1. Para contribuir com api-flask-faturamento, siga estas etapas:
2. Bifurque este repositório.
3. Crie um branch: `git checkout -b <nome_branch>`.
4. Faça suas alterações e confirme-as: `git commit -m '<mensagem_commit>'`.
5. Envie para o branch original: `git push origin api-flask-faturamento/<local>`.
6. Crie a solicitação de pull.

Como alternativa, consulte a documentação do GitHub em [como criar uma solicitação pull](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request).
