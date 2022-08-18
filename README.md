# Monografia

Playlist de apresentação do trabalho dispionível no Youtube<br>
<a href="https://www.youtube.com/watch?v=ilTZ3nKNl18&list=PLNngDNiSpYllv3hIy3huurlDm0fTGYyA8" target="_blank"><img src="https://img.shields.io/badge/YouTube-FF0000?style=for-the-badge&logo=youtube&logoColor=white" target="_blank"></a>
</div>

## Introdução
O presente trabalho trata sobre como algoritmos generativos que são usados para a produção de artes plásticas e podem ser usados de maneira análoga para a criação de designs de joias. Portanto,  finalidade dos códigos aqui apresentados é implementar os algoritmos generativos responsáveis por criar o design das peças. Demonstranto, assim, o potencial que o uso destes algoritmo têm na criação de produtos exclusivos e inovadores.<br>

## Código
Os códigos se encontram escritos em Python. A princípio se desenvolveu os códigos dentro do próprio Blender, mas ao notar que alguns algoritmos eram muito pesados para o Blender optou-se por desenvolver os códigos e os processamentos fora dele. E, assim, usar um script apenas para ler e printar os resultados do processamento no Blender.<br>

Note que neste caso, os arquivos com extensão .py podem ser executados dentro do Blender. Enquanto os arquivos .ipynb devem ser rodados fora e então impressos no Blender.<br>

### Pasta DLA_Code

Nela se encontram 4 arquivos, a saber:

- *Cool_patterns.ipynb* <br>
- *DLA_2D.py*<br>
- *DLA_teste.py*<br>
- *Square patterns DLA.ipynb*<br>
- *Processamento DLA e DLA_circle.ipynb*<br>
- *Processamento DLA_teste.ipynb*<br>

Os quais consistem na implementação de um algoritmo de Diffusion-Limited Aggregation<br>

Sobre o script *Cool_patterns.ipynb*, ele é o código com o qual eu consegui os melhores resultados para o DLA.


Sobre o script *DLA_teste.py*: ele implementa o DLA em 3D, e não gera designs nem grandes nem relevantes. Ele foi escrito de modo que:

1. A princípio se determinava um número arbitrário de interações que o algoritmo deveria rodar para obter a estrutura 3D finalizada,
agora itera-se até que o vetor de bolinhas fixas contenha 10 elementos.<br>
2. Foram criadas funções, que não são utilizadas, com diferentes formas(cubos, e torus) como blocos de construção da estrutura 3D ao invés de esferas <br>

Observações:<br>
- Código bom para pingentes e brincos.<br>
- Não consigo criar uma árvore com tamanho maior que 10<br>
- Posso usar mais caminhos aleatórios que estou usado<br>
- Não consigo aumentar muito o número de iterações, mas o código já foi rodado com 100 iterações<br>

O *DLA_2D.py* é a mesma implementação do *DLA_teste.py* só que imprimindo as coordenadas no 2D em forma de circulos. Ele foi um dos primeiros códigos do DLA a ser dsenvolvidos, e por isso não gera resultados relevantes.

O script *Square patterns DLA.ipynb*, é o código com os parâmetros que me permitem gerar designs quadradinhos e ramificados do DLA. 

*Processamento DLA e DLA_circle.ipynb* apresenta o código do *Cool_patterns.ipynb* mais algumas funções adicionais para rodar o DLA com um circulo de pontos fixos. Neste caso, ao invés das bolinhas serem geradas aleatoriamente em diferentes posições, todas são geradas no centro e então caminham aleatóriamente até colidir em alguma das bolinhas do circulo. Neste código foram adiconadas algumas funções que permitem visualizar o design através do matplotlib.

*Processamento DLA_teste.ipynb* é o código do *DLA_teste.py* com alguns parâmetros diferentes. Ele feito com a intenção de rodar fora do Blender.

**Sugestão de Modificações**
- [x] Criar formas em duas dimensões ao invés de três. Cool_patterns e square patterns fazem isso. Posso usa os outputs gerados com 3 dimensões e ignorar os valores de z, por exemplo.<br>
- [ ] Construir de baixo pra cima, de cima para baixo, dentro de outras formas, contornando formas, etc.<br>
- [x] DLA com um círculo de pontos fixos. Vide arquivo:Processamento DLA e DLA_circle.ipynb<br>
- [ ] Mudar o tamanho das esferas a medida que são acopladas<br>
- [x] Rodar o algoritmo em outro software que aguente mais processamento que o Blender, salvar em um arquivo os dados, e só printar o resultado no Blender<br>
- [ ] ~~Testar outros softwares como o Processing.~~ Desnecessário. <br>
- [ ] Remover a lógica de grid e funcionar num plano contínuo.<br> 


**Observações:**<br>
- Código bom para pingentes, brincos, aneis, etc. Permite a co-criação entre sistema e designer
o sistema funciona como gerador do design e o usuário pode interagir com a forma apresentada dando outros formatos, deformações, ajutes, rotações, operações de simetria, etc.<br>

## Pasta Jogo_da_vida_Code

Nesta pasta encontram-se os programas que implementam o Jogo da vida de Conway, um tipo de autômato celular.

Ela é composta pelos seguintes arquivos:

- *automato_celular.py* que implementa o jogo da vida tradicional. Imprimindo na tela as células vivas.Apresenta funções para imprimir as entradas e saidas. Apresenta função para adicionar o material de forma procedural.<br>
- *automato_celular_print_zeros.py* é o mesmo código do *automato_celular.py* com a diferença que imprime as células mortas e não as vivas. Além disso, ele apresenta uma função imprime_tabuleiro_altura que imprime a configuração do jogo da vida com aleatorização na altura dos cubinhos. Apresenta funções para imprimir as entradas e saídas.Apresenta função para adicionar o material de forma procedural.<br>
- *JVCfixa.py* é o código através do qual testou-se implementar a mistura do Jogo da Vida de Conway com o DLA. No qual as celulas caminham segundo a lógica do jogo da vida e ficam presas umas as outras como no DLA. Os resultadaos não foram relevantes.<br>
- *Processa_JVC.ipynb* código similar ao *JVCfixa.py* para rodar fora do Blender.<br>
- *Processa_JVC-Metatabuleiro.ipynb* código similar ao *Processa_JVC.ipynb*. A lógica de prender as células é distinta do código *Processa_JVC.ipynb*, o jogo da vida acontece em um tabuleiro, como se não tivesse o recurso de fixar células, enquanto em outro tabuleiro (o metatabuleiro), ele faz as operações de fixar células, sem interferir no tabuleiro original.<br>

**Sugestão de Modificações**
- [x] Rodar o algoritmo em outro software que aguente mais processamento que o Blender, salvar em um arquivo os dados, e só printar o resultado no Blender<br>
- [x] Limpar os arquivos do jogo da vida de Conway, alguns são meio ruins ou redundantes<br>
- [x] Adicionar o material de forma procedural<br>

**Observações:**<br>
- Código bom para anéis, brincos, pingentes, abortuaduras, entre outros<br>
- Co-criação é possível mas menos evidente que no DLA<br>

## print_from_file.py

Script que imprime arquivos .txt no Blender

**Sugestão de Modificações**
- [x] Adicionar textura de metal. Agora eu faço isso de maneira procedural.<br>
- [ ] Adicionar acabamento de forma automática: torus para um anel, por exemplo<br>

- [ ] Mudar o material de acordo com o tamanho e a medida que novas bolinhas são acopladas<br>


## Coisas a se testar geral:<br>
- [x] Salvar entradas e saidas<br>
- [x] Adicionar o material de forma procedural<br>
- [x] Tolerar variações dos parametros(2D,3D, etc...)<br>
- [ ] ~~Checar a correturde do programa~~<br>

## Execução

Para rodá-los abrir o Blender:
1. Clicar em script.<br>
2. Entrar com o código-fonte desejado, na área de texto.<br>
3. Então ou clicar no play no canto superior direitou ou ir no terminal no canto inferior esquerdo e digitar:<br>

```
filename = r"Path_of_file"
exec(compile(open(filename).read(), filename, 'exec'))
```

Referência: [How to run python script in Blender](https://learnsharewithdp.wordpress.com/2018/08/27/how-to-run-a-python-script-in-blender/)

## Dicas
- Limpar a tela com limpa_tela() no terminal<br>
- desenha_tabuleiro(tabuleiro) para ver o desenho final do jogo da vida<br> 
