import os

# obter o nome do arquivo de entrada
filename = input("Digite o caminho do arquivo de entrada: ")

# definir o nome do arquivo de saída
output_filename = os.path.splitext(filename)[0] + "Processado.txt"

# abrir o arquivo de entrada para leitura e o arquivo de saída para escrita
with open(filename, "r") as f_in, open(output_filename, "w") as f_out:
    # ler as linhas do arquivo de entrada
    lines = f_in.readlines()
    
    # escrever o cabeçalho do arquivo de saída
    f_out.write("image\trgb\tr\tg\tb\th\ts\tv\n")
    
    # iterar pelas linhas a partir da segunda linha
    for line in lines[1:]:
        # remover espaços em branco no início e fim da linha
        line = line.strip()
        
        # verificar se a primeira coluna contém apenas números
        if line.split(",")[0].split(".")[0].isdigit():
            # verificar se a linha possui 8 valores separados por vírgula
            if line.count(",") == 7:
                # extrair os valores da linha
                image, rgb, r, g, b, h, s, v = line.split(",")
                
                # escrever a linha no arquivo de saída, substituindo ',' por '\t'
                f_out.write(f"{image}\t{rgb}\t{r}\t{g}\t{b}\t{h}\t{s}\t{v}\n")
            else:
                print(f"Inconsistência encontrada na linha: {line}")
        else:
            print(f"Inconsistência encontrada na linha: {line}")
            
print("============================================")
print("Processamento concluído!")
input("Pressione Enter para sair...")
