# Monografia

Os códigos se encontram escritos em Python e foram desenvolvidos dentro do Blender, ambiente no qual devem ser executados.<br>

A finalidade dos códigos aqui apresentados é demonstrar o potencial de arte generativa na criação de produtos exclusivos e inovadores,
mais especificamente no design de joias.<br>

O script DLA_teste.py consiste na implementação de um algoritmo de Diffusion-Limited Aggregation<br>
Ele foi escrito de modo que:<br>
	1) A princípio se determinava um número arbitrário de interações que o algoritmo deveria rodar para obter a estrutura 3D finalizada,
	agora itera-se até que o vetor de bolinhas fixas contenha 10 elementos.<br>
	2)Foram criadas funções, que não são utilizadas, com diferentes formas(cubos, e torus) como blocos de construção da estrutura 3D ao invés de esferas <br>

Coisas a se testar:<br>
	[ ]Criar formas em duas dimensões ao invés de três<br>
	[ ]Construir de baixo pra cima, de cima para baixo, dentro de outras formas, contornando formas, etc<br>
	[ ]Mudar o tamanho das esferas a medida que são acopladas<br>
	[ ]Adicionar textura de metal<br>
	[ ]Adicionar acabamento de forma automática: torus para um anel, por exemplo<br>
	[ ]Mudar o material de acordo com o tamanho e a medida que novas bolinhas são acopladas<br>

Observações:
	-Código bom para pingentes e brincos

Os demais códigos se referem a um algoritmo distinto. Neles são implementados automatos celulares, mais especificamente o jogo da vida de Conway<br>

Observações:
	-Código bom para anéis e brincos


<h2>Execução</h2>

Para roda-los abrir o Blender, clicar em script. No terminal digitar:

```
filename = r"Path
exec(compile(open(filename).read(), filename, 'exec'))
```

Comentários sobre os códigos do jogo da vida de Conway <br>
Ele vai gerar uma imagem correspondente ao tabuleiro original<br>
Printar as iterações do algoritmo<br>
Limpar a tela com limpa_tela() no terminal<br>
desenha_tabuleiro(tabuleiro) para ver o desenho final do jogo da vida<br> 