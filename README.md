App para gerenciar impressões duplex manualmente, para impressoras que não contém; instruções via terminal; fácil

# Instruções
## Instalação
- Baixe o arquivo
- use ```pip install -r requirements``` para instalar todos os requerimentos
# Uso
![image](https://github.com/rafaeldelimaluna/Duplex-Print/assets/140565803/3f37aaa2-f790-4938-adb4-afafcdbd01ab)

Janela de dialogo para prosseguir para o outro lado da impressão

## Interativo CLI
O modo interativo faz diversas perguntas como: nome do arquivo, qualidade de impressão, tipo de midia, ordem (reverso || normal)...
para usá-lo, basta digitar:
```python app.py iterable```
![image](https://github.com/rafaeldelimaluna/Duplex-Print/assets/140565803/f0a8f90f-d272-4aa6-85ff-cff590e3cea8)

Pronto
## Direto
O modo direto ele somente pergunta o nome do arquivo e sua qualidade
```python app "duplex normal"```
![image](https://github.com/rafaeldelimaluna/Duplex-Print/assets/140565803/2478d630-2571-476a-a25e-14d6c5899683)

# Recomendações
Criar aliases para facilitar a vida, como os que criei:\n
Direto:```alias duplexprint="python duplex-print/app.py 'duplex normal'"```

Interativo:```python duplex-print/app.py iterable```
