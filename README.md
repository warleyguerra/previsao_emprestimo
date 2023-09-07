# previsao_emprestimo
## Criado a partir de uma competição do AnalyticsVidhya

### Descrição

A empresa Dream Housing Finance lida com todos os tipos de empréstimos à habitação. Eles estão presentes em todas as áreas urbanas, semi-urbanas e rurais. O cliente primeiro solicita um empréstimo à habitação e depois a empresa valida a elegibilidade do cliente para o empréstimo.

A empresa deseja automatizar o processo de elegibilidade do empréstimo (em tempo real) com base nos detalhes do cliente fornecidos durante o preenchimento do formulário de inscrição on-line. Esses detalhes são sexo, estado civil, escolaridade, número de dependentes, renda, valor do empréstimo, histórico de crédito e outros. Para automatizar esse processo, eles forneceram um conjunto de dados para identificar os segmentos de clientes elegíveis para o valor do empréstimo, para que possam atingir especificamente esses clientes.

### Métricas de Avaliação, Modelos e Tratamento dos Dados;

[Na parte 1 do projeto](https://github.com/warleyguerra/previsao_imprestimo/blob/main/Parte1.ipynb), foi onde fiz os tratamentos de: **valores nulos, tipo das colunas e encoding**,<br>
Utilizei os modelos de *árvore de decisão, Regressão Logística e KNeighborsClassifier* e usei **método de validaçao cruzada no melhor modelo em todas as partes do projeto**<br>
Foi Utilizado as métricas de avaliação: ***Acurácia e Matriz de confusão***<br>
obtive os seguintes resultados de **acurácia:**<br>
0	Modelo Árvore	0.669951<br>
1	Modelo Knn	0.600985<br>
2	Modelo Regressão	0.724138<br>
**Parte 1 Resultado no analyticsvidhya:  0.743055555555556**<br>
 
[Na parte 2 do projeto](https://github.com/warleyguerra/previsao_imprestimo/blob/main/Parte2.ipynb), foi onde tratei os **Outliers**,<br>
Obtive **melhora** na Acurácia nos modelos de **Árvore e Regressão**, no *Knn tive um desempenho inferior.*<br>

Modelo	          Outliers<br>
0	Modelo Árvore		0.677215<br>
1	Modelo Knn	  	0.575949<br>
2	 Regressão	   0.753165<br>

Apesar de melhorar a Acurácia nos modelos, o resultado no analyticsvidhya  foi o mesmo.<br>
**Parte 2 Resultado no analyticsvidhya:  0.743055555555556**<br>

[Na parte 3 do projeto](https://github.com/warleyguerra/previsao_imprestimo/blob/main/Parte3.ipynb), foi onde testei um modelo de **Deep Learning**,<br>
Obtive uma Acurácia melhor, mas o resultado de avaliação na competição foi inferior, isso pode ter ocorrido porque o modelo sofreu um *Overffiting**,<br>
*Isso aconteceu, porque minha base de treino é muito pequena, ela é composta por 614 linhas,*<br>
**Exemplos de métodos para evitar Overffiting do  modelo:**<br>

- Aumentar o tamanho do conjunto de dados de treinamento, se possível.<br>
- Simplificar a arquitetura do modelo, reduzindo o número de camadas ou unidades.<br>
- Aplicar técnicas de regularização, como dropout, L1 ou L2 regularization.<br>
- Realizar validação cruzada para avaliar o desempenho em diferentes divisões dos dados.<br>
- Tunar os hiperparâmetros cuidadosamente para encontrar a melhor combinação.<br>
- Coletar mais dados, se possível, para melhorar a generalização do modelo. <br>
Nesse caso optei por **não usar Deep Learning**, pois não teria como conseguir *mais dados para treino*, e toda ***tentativa de evitar Overffiting poderia ser muito trabalhosa e entregar o mesmo resultado final.***<br>
**Parte 3 Resultado no analyticsvidhya:  0.722222222222222**<br>

  ### Resultado Final

  Modelo	          Acurácia<br>
0	Modelo Árvore	    0.677215<br>
1	Modelo Knn	      0.575949<br>
2	Modelo Regressão	0.753165<br>
3	modelo_dl	        0.781250<br>

**Mesmo o modelo dl(deep learning) tendo acurácia melhor, optei por usar o modelo de Regressão Logística, pois foi mais constante, não sofreu overffiting e teve resultado melhor no analyticsvidhya**<br>
### Regressão Logística *Acurácia*: 0.753165 , *Resultado no analyticsvidhya*: 0.743055555555556<br>

### Deploy
Fiz um deploy simples, na minha máquina local;<br>
Utilizei o *Streamlit* para fazer o deploy, crei um arquivo *Joblib* do melhor modelo e carreguei no *Streamlit*;<br>
Nesse modelo, o usuário tem as caixas de diálogo para preencher e um botão para gerar o resultado baseado no treinamento que o modelo teve.<br>



![image](https://github.com/warleyguerra/previsao_emprestimo/assets/92888785/6262edd1-435c-427e-818f-c899a38bbd0b)

