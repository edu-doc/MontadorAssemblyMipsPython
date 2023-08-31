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

vetorR = ["sll", "srl", "jr", "mfhi", "mflo", "mult", "multu", "div", "divu", "add", "addu", "sub", "subu", "and", "or", "slt", "sltu", "mul"];
vetorL = ["beq", "bne", "addi", "addiu", "slti", "sltiu", "andi", "ori", "lui", "lw", "sw"]
vetorJ = ["j", "jal"]

vetR = ["sll", "srl"];
vetM = ["mfhi", "mflo"];
vetJR = ["jr"];

vetor = [""];

with open("C:/Users/Trojan/Documents/Codificadores/Arquitetura/binario.txt", "w") as file:
          file.write("")

with open("C:/Users/Trojan/Documents/Codificadores/Arquitetura/numero.txt", "r") as file:
    content = file.readlines()  # Lê todo o conteúdo do arquivo

for linha in content:
  
  palavras = linha.split()  # Divide o conteúdo em palavras

  for palavra in palavras:

    nome = palavras[0]
    nome1 = nome[0]
    
    vetor.clear()

    #COMEÇA AS BUSCAS DAS INSTRUÇÕES DO TIPO R ===============================================================================
    
    if palavras[0] in vetorR or palavras[1] in vetorR:
      
        for palavra in palavras:
          valorlido = palavra
          binarioop = opcodeR.get(valorlido,"")
          with open("C:/Users/Trojan/Documents/Codificadores/Arquitetura/binario.txt", "a") as file:
            file.write(binarioop)
        
        
        if palavras[0] in vetR or palavras[1] in vetR:
          
          for palavra in palavras: 
            valorlido = palavra
            binario = reg.get(valorlido,"")
            vetor.append(binario)
          
          if nome1 == "L":
            
            for palavra in palavras: 
              valorlido = palavras
            
            num = int(valorlido[4])
            num1 = bin(num)[2:]
            representa = num1.zfill(5)

            with open("C:/Users/Trojan/Documents/Codificadores/Arquitetura/binario.txt", "a") as file:
              file.write(vetor[3])
              file.write("00000")
              file.write(vetor[2])
              file.write(representa)
              vetor.clear()

            for palavra in palavras:
              valorlido = palavra
              binario = functionsR.get(valorlido,"")
              with open("C:/Users/Trojan/Documents/Codificadores/Arquitetura/binario.txt", "a") as file:
                file.write(binario)

            with open("C:/Users/Trojan/Documents/Codificadores/Arquitetura/binario.txt", "a") as file:
              file.write("\n")

            break

          else:

            for palavra in palavras: 
              valorlido = palavra
              binario = reg.get(valorlido,"")
              vetor.append(binario)

            for palavra in palavras: 
              valorlido = palavras

            num = int(valorlido[3])
            num1 = bin(num)[2:]
            representa = num1.zfill(5)

            with open("C:/Users/Trojan/Documents/Codificadores/Arquitetura/binario.txt", "a") as file:
              file.write(vetor[2])
              file.write("00000")
              file.write(vetor[1])
              file.write(representa)
              vetor.clear()
            
            for palavra in palavras:
              valorlido = palavra
              binario = functionsR.get(valorlido,"")
              with open("C:/Users/Trojan/Documents/Codificadores/Arquitetura/binario.txt", "a") as file:
                file.write(binario)

            with open("C:/Users/Trojan/Documents/Codificadores/Arquitetura/binario.txt", "a") as file:
              file.write("\n")

            break

        # PROCURANDO CASO ESPECIFICO MF ================================================================================

        if palavras[0] in vetM or palavras[1] in vetM:
          
          for palavra in palavras:
            valorlido = palavra
            binario = reg.get(valorlido,"")
            vetor.append(binario)

          if nome1 == "L":
            
            with open("C:/Users/Trojan/Documents/Codificadores/Arquitetura/binario.txt", "a") as file:
              file.write("00000")
              file.write("00000")
              file.write(vetor[2])
              file.write("00000")
              vetor.clear()

            for palavra in palavras:
              valorlido = palavra
              binario = functionsR.get(valorlido,"")
              with open("C:/Users/Trojan/Documents/Codificadores/Arquitetura/binario.txt", "a") as file:
                file.write(binario)
              
            with open("C:/Users/Trojan/Documents/Codificadores/Arquitetura/binario.txt", "a") as file:
              file.write("\n")

            break

          else:

            for palavra in palavras: 
              valorlido = palavra
              binario = reg.get(valorlido,"")
              vetor.append(binario)

            with open("C:/Users/Trojan/Documents/Codificadores/Arquitetura/binario.txt", "a") as file:
              file.write("00000")
              file.write("00000")
              file.write(vetor[1])
              file.write("00000")
              vetor.clear()
            
            for palavra in palavras:
              valorlido = palavra
              binario = functionsR.get(valorlido,"")
              with open("C:/Users/Trojan/Documents/Codificadores/Arquitetura/binario.txt", "a") as file:
                file.write(binario)
            
            with open("C:/Users/Trojan/Documents/Codificadores/Arquitetura/binario.txt", "a") as file:
              file.write("\n")

            break

          # PROCURANDO CASO ESPECIFICO JR ================================================================================
          
        if palavras[0] in vetJR or palavras[1] in vetJR:
          
          for palavra in palavras:
            valorlido = palavra
            binario = reg.get(valorlido,"")
            vetor.append(binario)

          if nome1 == "L":
            
            with open("C:/Users/Trojan/Documents/Codificadores/Arquitetura/binario.txt", "a") as file:
              file.write(vetor[2])
              file.write("00000")
              file.write("00000")
              file.write("00000")
              vetor.clear()

            for palavra in palavras:
              valorlido = palavra
              binario = functionsR.get(valorlido,"")
              with open("C:/Users/Trojan/Documents/Codificadores/Arquitetura/binario.txt", "a") as file:
                file.write(binario)
              
            with open("C:/Users/Trojan/Documents/Codificadores/Arquitetura/binario.txt", "a") as file:
              file.write("\n")

            break

          else:

            for palavra in palavras: 
              valorlido = palavra
              binario = reg.get(valorlido,"")
              vetor.append(binario)

            with open("C:/Users/Trojan/Documents/Codificadores/Arquitetura/binario.txt", "a") as file:
              file.write(vetor[1])
              file.write("00000")
              file.write("00000")
              file.write("00000")
              vetor.clear()
            
            for palavra in palavras:
              valorlido = palavra
              binario = functionsR.get(valorlido,"")
              with open("C:/Users/Trojan/Documents/Codificadores/Arquitetura/binario.txt", "a") as file:
                file.write(binario)
            
            with open("C:/Users/Trojan/Documents/Codificadores/Arquitetura/binario.txt", "a") as file:
              file.write("\n")

            break

        else:
          
          for palavra in palavras:
            valorlido = palavra
            binario = reg.get(valorlido,"")
            vetor.append(binario)

          if nome1 == "L":
            
            with open("C:/Users/Trojan/Documents/Codificadores/Arquitetura/binario.txt", "a") as file:
              file.write(vetor[3])
              file.write(vetor[4])
              file.write(vetor[2])
              file.write("00000")
              vetor.clear()

            for palavra in palavras:
              valorlido = palavra
              binario = functionsR.get(valorlido,"")
              with open("C:/Users/Trojan/Documents/Codificadores/Arquitetura/binario.txt", "a") as file:
                file.write(binario)
              
            with open("C:/Users/Trojan/Documents/Codificadores/Arquitetura/binario.txt", "a") as file:
              file.write("\n")

            break

          else:

            for palavra in palavras: 
              valorlido = palavra
              binario = reg.get(valorlido,"")
              vetor.append(binario)

            with open("C:/Users/Trojan/Documents/Codificadores/Arquitetura/binario.txt", "a") as file:
              file.write(vetor[2])
              file.write(vetor[3])
              file.write(vetor[1])
              file.write("00000")
              vetor.clear()
            
            for palavra in palavras:
              valorlido = palavra
              binario = functionsR.get(valorlido,"")
              with open("C:/Users/Trojan/Documents/Codificadores/Arquitetura/binario.txt", "a") as file:
                file.write(binario)
            
            with open("C:/Users/Trojan/Documents/Codificadores/Arquitetura/binario.txt", "a") as file:
              file.write("\n")

            break
          #COMEÇA A BUSCA DAS INSTRUÇÕES DO TIPO L ==================================================================================
    
    elif palavras[0] in vetorL or palavras[1] in vetorL: 
        print('dudis')
      
    
    
    

    
        

    
  