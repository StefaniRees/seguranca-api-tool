# Ferramenta de Testes de Segurança em API REST

## Como usar

1. Instale as dependências:
```
pip install -r requirements.txt
```

2. Rode os testes com geração de relatório:
```
python run_tests.py
```

## O que está incluído

- Testes de autenticação (token válido, inválido, ausente)
- Verificação de headers de segurança e CORS
- Teste de método HTTP proibido (PUT)