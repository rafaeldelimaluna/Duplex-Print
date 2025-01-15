App para realizar impressão duplex de modo manual, em impressoras que não contém a funcionalidade; instruções via terminal; fácil

# Instruções
## Instalação
- Baixe o repositório;
- Na pasta do projeto, utilize no terminal ```pip install -r requirements``` para instalar todos os requerimentos;

# Modos de utilização
  O App contém 3 modos de utilização, todos via CLI:
  - Prompt GUI;
  - Prompt;
  - Iterable;
## Breve descrição de cada um
### Prompt GUI
Em seu início, ele indica uma lista de arquivos com extensão ```.pdf``` do diretório atual, e ao lado a quantidade de páginas.
#### Exemplo:
![image](https://github.com/user-attachments/assets/2415018b-b0c6-43d9-8450-7278806ca1a2) 

No diretório atual, temos três arquivos: PA.pdf, PG.pdf, "Questões PA e PG.pdf";
Ao chamarmos o app pelo modo "Prompt GUI", ele iniciará a lista no terminal:
![image](https://github.com/user-attachments/assets/2cab4a55-83b6-4e74-a0e4-40ab33172791)
com isso, podemos escolher qual arquivo queremos imprimir.
No exemplo, escolhi "PG.pdf", como isso, vamos para a próxima parte: a escolha da qualidade
de impressão:
![image](https://github.com/user-attachments/assets/1d9a6e27-474a-4b88-8d2d-f1aa3a0306f7)
Ao selecionarmos "Ok", ele manda a primeira parte da impressão ser impressão ser executada, e exibe no
terminal a seguinte mensagem de status:
![image](https://github.com/user-attachments/assets/05b685d1-6344-4f69-a8a6-e82e1d3c9233)

Ao terminar a primeira parte, devemos inverter a face do bloco de papéis que foi impresso, ou seja, a parte que saiu é a que vemos, é a parte impressa; devemos virar esse bloco de papéis impresso para ver o seu verso. Após isso, devemos colocar na impressora este bloco. A interface gráfica entra em ação:
![image](https://github.com/user-attachments/assets/1fa3da1e-7d7f-4aa2-a9b0-cf4e90fcf674)


### Interativo CLI
O modo interativo faz diversas perguntas como: nome do arquivo, qualidade de impressão, tipo de midia, ordem (reverso || normal)...
para usá-lo, basta digitar:
```python app.py iterable```
Pronto

## Direto
O modo direto ele somente pergunta o nome do arquivo e sua qualidade
```python app "duplex normal"```
![image](https://github.com/rafaeldelimaluna/Duplex-Print/assets/140565803/2478d630-2571-476a-a25e-14d6c5899683)

# Recomendações
Criar aliases para facilitar a vida, como os que criei:\n
Direto:```alias duplexprint="python duplex-print/app.py 'duplex normal'"```

Interativo:```python duplex-print/app.py iterable```
