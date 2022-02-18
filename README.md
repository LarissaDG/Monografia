# Monografia

## Introdução
O presente trabalho trata sobre como algoritmos generativos que são usados para a produção de artes plásticas e podem ser usados de maneira análoga para a criação de designs de joias. Portanto,  finalidade dos códigos aqui apresentados é implementar os algoritmos generativos responsáveis por criar o design das peças. Demonstranto, assim, o potencial que o uso destes algoritmo têm na criação de produtos exclusivos e inovadores.<br>

## Código
Os códigos se encontram escritos em Python. A princípio se desenvolveu os códigos dentro do próprio Blender, mas ao notar que alguns algoritmos eram muito pesados para o Blender optou-se por desenvolver os códigos e os processamentos fora dele. E, assim, usar um script apenas para ler e printar os resultados do processamento no Blender.<br>

--------------------
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
	[x]Rodar o algoritmo em outro software que aguente mais processamento que o Blender, salvar em um arquivo os dados, e só printar o resultado no Blender<br>
	[ ]Testar outros softwares como o Processing <br>

Observações:<br>
	-Código bom para pingentes e brincos<br>
	-Não consigo criar uma árvore com tamanho maior que 10<br>
	-Posso usar mais caminhos aleatórios que estou usado<br>
	-Não consigo aumentar muito o número de iterações, mas o código já foi rodado com 100 iterações<br>

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

<h2>Execução</h2>

Para roda-los abrir o Blender, clicar em script. No terminal digitar:<br>

```
filename = r"Path
exec(compile(open(filename).read(), filename, 'exec'))
```

Comentários sobre os códigos do jogo da vida de Conway <br>
Ele vai gerar uma imagem correspondente ao tabuleiro original<br>
Printar as iterações do algoritmo<br>
Limpar a tela com limpa_tela() no terminal<br>
desenha_tabuleiro(tabuleiro) para ver o desenho final do jogo da vida<br> 


Organização em pastas. Agora processo primeiro e só imprimo os resultados. Checar a corretude do programa. Gride maior melhor resultado. Diminuir bolinhas. Começar de baixo pra cima e de cima pra baixo. Animar, fazer um GIF. Talvez testar no processing

Testar de fazer verificações topograficas no Jogo da vida de Conway

