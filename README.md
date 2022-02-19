# Monografia

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
- [ ] ~~Testar outros softwares como o Processing.~~ Desnecessário <br>


**Observações:**<br>
- Código bom para pingentes, brincos, aneis, etc. Permite a co-criação entre sistema e designer
o sistema funciona como gerador do design e o usuário pode interagir com a forma apresentada dando outros formatos, deformações, ajutes, rotações, operações de simetria, etc.<br>

## Pasta Jogo_da_vida_Code

**Sugestão de Modificações**
- [x] Rodar o algoritmo em outro software que aguente mais processamento que o Blender, salvar em um arquivo os dados, e só printar o resultado no Blender<br>

## print_from_file.py

**Sugestão de Modificações**
- [x] Adicionar textura de metal. Agora eu faço isso de maneira procedural.<br>
- [ ] Adicionar acabamento de forma automática: torus para um anel, por exemplo<br>

- [ ] Mudar o material de acordo com o tamanho e a medida que novas bolinhas são acopladas<br>

--------------------

Os demais códigos se referem a um algoritmo distinto. Neles são implementados automatos celulares, mais especificamente o jogo da vida de Conway<br>

Coisas a se testar:<br>
	[x]Limpar os arquivos do jogo da vida de Conway, alguns são meio ruins ou redundantes<br>
	[x]Adicionar o material de forma procedural<br>

Observações:<br>
	-Código bom para anéis e brincos<br>
	-O arquivo automato_celular code contém o código "orignal" do projeto. Enquanto o arquivo "trabalhar.py" Adiciona o matérial de forma procedural.<br>


Coisas a se testar geral:<br>
	[ ]Salvar entradas e saidas<br>
	[ ]Adicionar o material de forma procedural<br>
	[ ]Tolerar variações dos parametros(2D,3D, etc...)<br>

## Execução

Para rodá-los abrir o Blender, clicar em script. Entrar com o código-fonte desejado, na área de texto. Então ou clicar no play no canto superior direitou ou ir no terminal no canto inferior esquerdo e digitar:<br>

```
filename = r"Path_of_file"
exec(compile(open(filename).read(), filename, 'exec'))
```

Referência: [How to run python script in Blender](https://learnsharewithdp.wordpress.com/2018/08/27/how-to-run-a-python-script-in-blender/)

Comentários sobre os códigos do jogo da vida de Conway <br>
Ele vai gerar uma imagem correspondente ao tabuleiro original<br>
Printar as iterações do algoritmo<br>
Limpar a tela com limpa_tela() no terminal<br>
desenha_tabuleiro(tabuleiro) para ver o desenho final do jogo da vida<br> 


Organização em pastas. Agora processo primeiro e só imprimo os resultados. Checar a corretude do programa. Gride maior melhor resultado. Diminuir bolinhas. Começar de baixo pra cima e de cima pra baixo. Animar, fazer um GIF. Talvez testar no processing

Testar de fazer verificações topograficas no Jogo da vida de Conway

