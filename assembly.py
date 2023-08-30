# Mapeamento dos registradores em binário
reg = {
    "$zero": "00000",
    "$at": "00001",
    "$v0": "00010",
    "$v1": "00011",
    "$a0": "00100",
    "$a1": "00101",
    "$a2": "00110",
    "$a3": "00111",
    "$t0": "01000",
    "$t1": "01001",
    "$t2": "01010",
    "$t3": "01011",
    "$t4": "01100",
    "$t5": "01101",
    "$t6": "01110",
    "$t7": "01111",
    "$s0": "10000",
    "$s1": "10001",
    "$s2": "10010",
    "$s3": "10011",
    "$s4": "10100",
    "$s5": "10101",
    "$s6": "10110",
    "$s7": "10111",
    "$t8": "11000",
    "$t9": "11001",
    "$k0": "11010",
    "$k1": "11011",
    "$gp": "11100",
    "$sp": "11101",
    "$fp": "11110",
    "$ra": "11111",
}

# Mapeamento de opcode tipo R para códigos binários
opcodeR = {
    "sll": "000000",
    "srl": "000000",
    "jr": "000000",
    "mfhi": "000000",
    "mflo": "000000",
    "mult": "000000",
    "multu": "000000",
    "div": "000000",
    "divu": "000000",
    "add": "000000",
    "addu": "000000",
    "sub": "000000",
    "subu": "000000",
    "and": "000000",
    "or": "000000",
    "slt": "000000",
    "sltu": "000000",
    "mul": "011100",
}

# Mapeamento de functions tipo R para códigos binários
functionsR = {
    "sll": "000000",
    "srl": "000010",
    "jr": "001000",
    "mfhi": "010000",
    "mflo": "010010",
    "mult": "011000",
    "multu": "011001",
    "div": "011010",
    "divu": "011011",
    "add": "100000",
    "addu": "100001",
    "sub": "100010",
    "subu": "100011",
    "and": "100100",
    "or": "100101",
    "slt": "101010",
    "sltu": "101011",
    "mul": "000010",
}

with open("C:/Users/Trojan/Documents/Codificadores/Arquitetura/binario.txt", "w") as file:
        file.write("")

with open("C:/Users/Trojan/Documents/Codificadores/Arquitetura/numero.txt", "r") as file:
    content = file.read()  # Lê todo o conteúdo do arquivo
    words = content.split()  # Divide o conteúdo em palavras

for word in words:

    valorlido = word

    binario = reg.get(valorlido, "Valor não encontrado")

    if(valorlido == ("sll" or "srl" or "jr" or "mfhi" or "mflo" or "mult" or "multu" or "div" or "divu" or "add" or "addu" or "sub" or "subu" or "and" or "or" or "slt" or "sltu" or "mul")):
            
            with open("C:/Users/Trojan/Documents/Codificadores/Arquitetura/binario.txt", "w") as file:
                    file.write("")

            with open("C:/Users/Trojan/Documents/Codificadores/Arquitetura/numero.txt", "r") as file:
                content = file.readlines()  # Lê todo o conteúdo do arquivo
                
            binarioop = opcodeR.get(valorlido,"")
            with open("C:/Users/Trojan/Documents/Codificadores/Arquitetura/binario.txt", "a") as file:
                    file.write(binarioop)

            for word in words:
                words = word.split()  # Divide o conteúdo em palavras
                valorlido = word

                binario = reg.get(valorlido,"")

                with open("C:/Users/Trojan/Documents/Codificadores/Arquitetura/binario.txt", "a") as file:
                    file.write(binario)
                
                        



