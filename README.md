# previsao_imprestimo
## Criado a partir de uma competição do Kaggle

A empresa Dream Housing Finance lida com todos os tipos de empréstimos à habitação. Eles estão presentes em todas as áreas urbanas, semi-urbanas e rurais. O cliente primeiro solicita um empréstimo à habitação e depois a empresa valida a elegibilidade do cliente para o empréstimo.

A empresa deseja automatizar o processo de elegibilidade do empréstimo (em tempo real) com base nos detalhes do cliente fornecidos durante o preenchimento do formulário de inscrição on-line. Esses detalhes são sexo, estado civil, escolaridade, número de dependentes, renda, valor do empréstimo, histórico de crédito e outros. Para automatizar esse processo, eles forneceram um conjunto de dados para identificar os segmentos de clientes elegíveis para o valor do empréstimo, para que possam atingir especificamente esses clientes.

[Na parte 1 do projeto] (https://github.com/warleyguerra/previsao_imprestimo/blob/main/Parte1.ipynb), foi onde fiz os tratamentos de: **valores nulos, tipo das colunas e encoding**,
Utilizei os modelos de *árvore de decisão, Regressão Logística e KNeighborsClassifier* e usei **método de validaçao cruzada no melhor modelo em todas as partes do projeto**
obtive os seguintes resultados de **acurácia:**
0	Modelo Árvore	0.669951
1	Modelo Knn	0.600985
2	Modelo Regressão	0.724138
**Parte 1 Resultado no analyticsvidhya:  0.743055555555556**
 
[Na parte 2 do projeto] (https://github.com/warleyguerra/previsao_imprestimo/blob/main/Parte2.ipynb), foi onde tratei os **Outliers**,
Obtive **melhora** na Acurácia nos modelos de **Árvore e Regressão**, no *Knn tive um desempenho inferior.*

Modelo	        inicial   Outliers
0	Modelo Árvore	0.669951	0.677215
1	Modelo Knn	  0.600985	0.575949
2	 Regressão	  0.724138  0.753165

Apesar de melhorar a Acurácia nos modelos, o resultado no analyticsvidhya  foi o mesmo.
**Parte 2 Resultado no analyticsvidhya:  0.743055555555556**

[Na parte 3 do projeto] (https://github.com/warleyguerra/previsao_imprestimo/blob/main/Parte3.ipynb), foi onde testei um modelo de **Deep Learning**,
Obtive uma Acurácia melhor, mas o resultado de avaliação na competição foi inferior, isso pode ter ocorrido porque o modelo sofreu um *Overffiting**,
*Isso aconteceu, porque minha base de treino é muito pequena, ela é composta por 614 linhas,*
**Exemplos de métodos para evitar Overffiting do  modelo:**

- Aumentar o tamanho do conjunto de dados de treinamento, se possível.
- Simplificar a arquitetura do modelo, reduzindo o número de camadas ou unidades.
- Aplicar técnicas de regularização, como dropout, L1 ou L2 regularization.
- Realizar validação cruzada para avaliar o desempenho em diferentes divisões dos dados.
- Tunar os hiperparâmetros cuidadosamente para encontrar a melhor combinação.
- Coletar mais dados, se possível, para melhorar a generalização do modelo.
Nesse caso optei por **não usar Deep Learning**
****Parte 3 Resultado no analyticsvidhya:  0.722222222222222**

  ### Resultado Final

  Modelo	          Acurácia
0	Modelo Árvore	    0.677215
1	Modelo Knn	      0.575949
2	Modelo Regressão	0.753165
3	modelo_dl	        0.781250

**Mesmo o modelo dl(deep learning) tendo acurácia melhor, optei por usar o modelo de Regressão Logística, pois foi mais constante, não sofreu overffiting e teve resultado melhor no analyticsvidhya**
### Regressão Logística *Acurácia*: 0.753165 , *Resultado no analyticsvidhya*: 0.743055555555556
