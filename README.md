# Colors-to-ImageJ
Script em Python que converte um arquivo .csv de saída do FORD com os parâmetros image, rgb, r, g, b, h, s, v para .txt para uso no ImagePlot do ImageJ

# Como usar
0. Após analise das cores das imagens no FORD, será gerado um arquivo "Colors.csv"
1. Baixe e execute o arquivo 'ColorsToImageJ.exe' em um ambiente com Python 3.11.2
2. Insira o caminho do arquivo "Colors.csv" *(Ex: C:\Users\NomeUsuario\Desktop\NomedaPasta\Colors.csv)*
3. ou Execute o arquivo 'ColorsToImageJ.exe' na mesma pasta do arquivo "Colors.csv" e digite Colors.csv (ou outro nome caso tenha renomeado o arquivo) 
4. O arquivo de saida será "NomeDoArquivo+Processado.txt" *(Ex: "ColorsProcessado.txt")*

# Como Funciona
1. O Script analisa o arquivo estabelece o cabeçario e procura pelos 8 parâmetros: image, rgb, r, g, b, h, s, v
2. Substitui a separação por virgulas, e separa os valores por tabulação (\t)
3. Caso em uma linha o parâmetro "name" não seja um número *(Ex: 15622.jpeg)*, ela será exluida e a mensagem 'Inconsistência encontrada na linha: (linha)' será exibida no terminal
4. Caso a linha não possua os 8 valores, ela será exluida e a mensagem 'Inconsistência encontrada na linha: (linha)' será exibida no terminal
