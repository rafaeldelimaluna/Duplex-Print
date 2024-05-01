App para gerenciar impressões duplex manualmente, para impressoras que não contém; instruções via terminal; fácil

# Instruções
## Instalação
- Baixe o arquivo
- use ```pip install -r requirements``` para instalar todos os requerimentos
# Uso
## Interativo CLI
O modo interativo faz diversas perguntas como: nome do arquivo, qualidade de impressão, tipo de midia, ordem (reverso || normal)...
para usá-lo, basta digitar:
```python app.py iterable```
Pronto
## Direto
O modo direto ele somente pergunta o nome do arquivo e sua qualidade
```python app "duplex normal"```
