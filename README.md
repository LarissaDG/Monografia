# Monografia

Os códigos deseolvidos foram feitos para rodar no Blender.

Eles usam de automatos celulares mais especificamente o jogo da vida de conway

Para roda-los abrir o Blender, clicar em script. No terminal digitar:

filename = r"Path"
exec(compile(open(filename).read(), filename, 'exec'))

Ele vai gerar uma imagem correspondente ao tabuleiro original
Printar as iterações do algoritmo
Limpar a tela com limpa_tela() no terminal
desenha_tabuleiro(tabuleiro) para ver o desenho final do jogo da vida 