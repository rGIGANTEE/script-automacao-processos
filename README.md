# Controle de Efetivo e Material - Automacao com Python

## 📌 Sobre o Projeto

Este projeto automatiza a importação de dados de um arquivo CSV para um arquivo Excel para controle de efetivo militar e materiais dentro do quartel. Ele permite que os dados sejam constantemente atualizados sem perder informações anteriores.

## 🚀 Funcionalidades

* Leitura de um arquivo CSV contendo informações sobre militares ou materiais.

* Atualização contínua de um arquivo Excel sem sobrescrever dados existentes.

* Criação automática do diretório onde os arquivos são armazenados.

* Tratamento de erros, garantindo que arquivos corrompidos não causem falhas no sistema.

## 🛠️ Tecnologias Utilizadas

* Python

* pandas (Manipulação de dados)

* openpyxl (Manipulação de arquivos Excel)

* os (Gerenciamento de diretórios e arquivos)

## 📌 Dependências

Antes de executar o script, instale as bibliotecas necessárias:

```bash
    pip install -r requirements.txt
```

## ▶️ Como Executar

Coloque o arquivo CSV na pasta arquivos/ com o nome arquivo_csv.csv.

```bash
    python main.py
```

Os dados serão adicionados ao arquivo_excel.xlsx. Se o arquivo não existir, será criado automaticamente.

## 📌 Melhorias Futuras

* Implementação de interface gráfica para facilitar o uso por usuários sem conhecimento técnico.

* Criação de logs de alterações, permitindo auditoria das modificações nos dados.

* Integração com banco de dados, para maior segurança e escalabilidade.

## 🤝 Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir problemas (issues) e enviar solicitações de pull (pull requests).