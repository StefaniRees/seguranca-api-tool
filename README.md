
# Ferramenta de Testes de Segurança em API REST

## Como usar

1. Instale as dependências necessárias com o comando:

```bash
pip install -r requirements.txt
````

2. Execute os testes com geração de relatório HTML usando:

```bash
python run_tests.py
```

## O que está incluído

* Testes de autenticação:

  * Token válido
  * Token inválido
  * Token ausente

* Verificação de headers de segurança e CORS para garantir que as respostas da API contenham os cabeçalhos corretos para proteção e controle de acesso.

* Teste de método HTTP proibido (PUT), para verificar se métodos não permitidos são bloqueados corretamente.

## Detalhes Técnicos

A ferramenta é escrita em Python, utilizando as bibliotecas `pytest` para execução dos testes e `requests` para fazer as requisições HTTP à API.

Os resultados dos testes são compilados em um relatório HTML, que pode ser acessado após a execução para análise detalhada dos casos testados.

## Estrutura do Projeto

* `run_tests.py`: Script principal para rodar todos os testes e gerar o relatório.
* `tests/`: Diretório contendo os scripts de testes automatizados.
* `requirements.txt`: Lista das dependências Python necessárias.

## Requisitos

* Python 3.x instalado
* Acesso à API REST que será testada (endpoints configurados no código dos testes)

