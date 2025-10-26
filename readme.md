# 🔍 Fake Docs - Validador de Documentos com Azure AI

Aplicação web desenvolvida com Streamlit para validação e extração de informações de cartões de visita utilizando Azure Document Intelligence (Form Recognizer) e Azure Blob Storage.

## 📋 Descrição

Este projeto faz parte do **Desafio 2 do Bootcamp DIO - Azure AI-102** e tem como objetivo demonstrar a integração entre:

- **Azure Blob Storage**: Para armazenamento seguro de documentos
- **Azure Document Intelligence (Form Recognizer)**: Para análise e extração de dados de cartões de visita
- **Streamlit**: Para interface web interativa e amigável

## 🚀 Funcionalidades

- ✅ Upload de arquivos (PDF, PNG, JPG, JPEG)
- ✅ Armazenamento automático no Azure Blob Storage
- ✅ Análise inteligente de cartões de visita
- ✅ Extração de informações:
  - Nome do contato
  - Empresa
  - Telefone
  - Email
  - Website
- ✅ Validação visual com feedback em tempo real
- ✅ Exibição da imagem enviada

## 🛠️ Tecnologias Utilizadas

- **Python 3.12**
- **Streamlit**: Framework para criação de aplicações web
- **Azure AI Form Recognizer**: Serviço de IA para análise de documentos
- **Azure Blob Storage**: Armazenamento em nuvem
- **python-dotenv**: Gerenciamento de variáveis de ambiente

## 📦 Dependências

```txt
azure-core
azure-ai-formrecognizer
azure-storage-blob
streamlit
python-dotenv
```

## ⚙️ Configuração

### 1. Pré-requisitos

- Conta no [Microsoft Azure](https://azure.microsoft.com/)
- Python 3.8 ou superior instalado
- Git (opcional)

### 2. Criar Recursos no Azure

#### 2.1 Azure Document Intelligence (Form Recognizer)

1. Acesse o [Portal do Azure](https://portal.azure.com)
2. Crie um novo recurso **Document Intelligence** ou **Form Recognizer**
3. Anote o **Endpoint** e a **Key**

#### 2.2 Azure Storage Account

1. Crie uma **Storage Account**
2. Dentro dela, crie um **Container** (ex: `documentos`)
3. Copie a **Connection String** em: _Access Keys > Connection string_

### 3. Configurar Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto:

```env
AZURE_DOCUMENT_INTELLIGENCE_ENDPOINT=https://seu-recurso.cognitiveservices.azure.com/
AZURE_DOCUMENT_INTELLIGENCE_KEY=sua_chave_aqui
AZURE_STORAGE_CONNECTION_STRING=DefaultEndpointsProtocol=https;AccountName=...
CONTAINER_NAME=documentos
```

### 4. Instalação

Clone o repositório:

```bash
git clone https://github.com/phNaka/AnaliseDocumento.git
cd fake-docs
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

## 🎯 Como Usar

1. Execute a aplicação:

```bash
streamlit run app.py
```

2. Acesse no navegador: `http://localhost:8501`

3. Faça upload de um cartão de visita (imagem ou PDF)

4. Aguarde a análise e visualize os resultados extraídos

## 📁 Estrutura do Projeto

```
fake-docs/
│
├── app.py                      # Aplicação principal Streamlit
├── requirements.txt            # Dependências do projeto
├── .env                        # Variáveis de ambiente (não commitar!)
├── .gitignore                  # Arquivos ignorados pelo Git
│
├── services/
│   ├── blob_service.py         # Serviço de upload para Blob Storage
│   └── documento_service.py    # Serviço de análise de documentos
│
└── uteis/
    └── config.py               # Configurações e variáveis de ambiente
```

## 🔐 Segurança

⚠️ **IMPORTANTE**:

- Nunca commite o arquivo `.env` para o repositório
- Mantenha suas chaves e connection strings em segredo
- Use o `.gitignore` para excluir arquivos sensíveis

Adicione ao `.gitignore`:

```
.env
__pycache__/
*.pyc
.vscode/
```

## 🐛 Solução de Problemas

### Erro: "ModelNotFound"

- Verifique se está usando `azure-ai-formrecognizer` (não `azure-ai-documentintelligence`)
- Confirme que o recurso do Azure está na região correta

### Erro: "ModuleNotFoundError"

```bash
pip install -r requirements.txt --upgrade
```

### Erro de Conexão com Azure

- Verifique as credenciais no arquivo `.env`
- Confirme que o recurso está ativo no Portal do Azure

## 📝 Melhorias Futuras

- [ ] Suporte para múltiplos tipos de documentos (RG, CNH, Notas Fiscais)
- [ ] Histórico de documentos analisados
- [ ] Exportação de dados em CSV/JSON
- [ ] Interface multilíngue
- [ ] Detecção de documentos fraudulentos

## 👨‍💻 Autor

Desenvolvido como parte do Bootcamp DIO - Azure AI-102

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 🤝 Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para:

1. Fazer um Fork do projeto
2. Criar uma branch para sua feature (`git checkout -b feature/MinhaFeature`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova feature'`)
4. Push para a branch (`git push origin feature/MinhaFeature`)
5. Abrir um Pull Request

---

⭐ Se este projeto te ajudou, não esqueça de dar uma estrela no repositório!
