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

opcodeL = {
    "beq": "000100",
    "bne": "000101",
    "addi": "001000",
    "addiu": "001001",
    "slti": "001010",
    "sltiu": "001011",
    "andi": "001100",
    "ori": "001101",
    "lui": "001111",
    "lw": "100011",
    "sw": "101011",
}

opcodeJ = {
    "j": "000010",
    "jal": "000011",
}

adress = {

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

vetS = ["sll", "srl"];
vetM = ["mfhi", "mflo"];
vetJR = ["jr"];
vetMDU =["mult", "multu", "div", "divu"];
vetorLUI = ["lui"];
vetorW = ["sw", "lw"]
vetorB = ["beq", "bne"]

num = [""];

vetor = [""]; #Inicialização de Vetor (NÃO DELETE DE MODO ALGUM!)

with open("C:/Users/Trojan/Documents/Codificadores/Arquitetura/numero.txt", 'r') as file:
        numero_linha = 1
        for linha in file:
            palavras = linha.strip().split()  # Divide a linha em palavras
            for i in range(len(palavras)): #Filtro para retirar as Parenteses
              palavras[i] = palavras[i].replace(':', '')
            if palavras:
                primeira_palavra = palavras[0]  # Pega a primeira palavra
                adress[primeira_palavra] = numero_linha
            numero_linha += 1

with open("C:/Users/Trojan/Documents/Codificadores/Arquitetura/binario.txt", "w") as file: #Limpa o arquivo binario.txt
          file.write("")

with open("C:/Users/Trojan/Documents/Codificadores/Arquitetura/numero.txt", "r") as file: #Lê o arquivo numero.txt
    content = file.readlines()

for i in range(len(content)): #Filtro para retirar as virgulas
    content[i] = content[i].replace(',', '')


for linha in content:
  
  palavras = linha.split()  # Divide o conteúdo em palavras
  nome1 = False
  for palavra in palavras:

    vetor.clear()

    #COMEÇA AS BUSCAS DAS INSTRUÇÕES DO TIPO R ===============================================================================
    
    if palavras[0] in vetorR or palavras[1] in vetorR:
      
        for palavra in palavras:
          valorlido = palavra
          binarioop = opcodeR.get(valorlido,"")
          with open("C:/Users/Trojan/Documents/Codificadores/Arquitetura/binario.txt", "a") as file:
            file.write(binarioop)
        
        if palavras[0] in vetS or palavras[1] in vetS:
          
          for palavra in palavras: 
            valorlido = palavra
            binario = reg.get(valorlido,"")
            vetor.append(binario)
          
          for palavra in palavras:
            nome2 = len(palavra)
            nome2 = nome2 - 1
            if palavra[nome2] == ':':
              nome1 = True
  
          if nome1 == True:
            
            for palavra in palavras: 
              valorlido = palavras
            
            num = int(valorlido[4])
            num1 = bin(num)[2:]
            representa = num1.zfill(5)

            with open("C:/Users/Trojan/Documents/Codificadores/Arquitetura/binario.txt", "a") as file:
              file.write("00000")
              file.write(vetor[3])
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
              file.write("00000")
              file.write(vetor[2])
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

        # PROCURANDO CASO ESPECIFICO MDU ===============================================================================

        if palavras[0] in vetMDU or palavras[1] in vetMDU:
          
          for palavra in palavras: 
            valorlido = palavra
            binario = reg.get(valorlido,"")
            vetor.append(binario)
          
          for palavra in palavras:
            nome2 = len(palavra)
            nome2 = nome2 - 1
            if palavra[nome2] == ':':
              nome1 = True
  
          if nome1 == True:
            
            for palavra in palavras: 
              valorlido = palavras
            
            num = int(valorlido[4])
            num1 = bin(num)[2:]
            representa = num1.zfill(5)

            with open("C:/Users/Trojan/Documents/Codificadores/Arquitetura/binario.txt", "a") as file:
              file.write(vetor[2])
              file.write(vetor[3])
              file.write("00000")
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

            with open("C:/Users/Trojan/Documents/Codificadores/Arquitetura/binario.txt", "a") as file:
              file.write(vetor[1])
              file.write(vetor[2])
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

        # PROCURANDO CASO ESPECIFICO MF ================================================================================

        if palavras[0] in vetM or palavras[1] in vetM:
          
          for palavra in palavras:
            valorlido = palavra
            binario = reg.get(valorlido,"")
            vetor.append(binario)
          
          for palavra in palavras:
            nome2 = len(palavra)
            nome2 = nome2 - 1
            if palavra[nome2] == ':':
              nome1 = True
  
          if nome1 == True:
            
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

          for palavra in palavras:
            nome2 = len(palavra)
            nome2 = nome2 - 1
            if palavra[nome2] == ':':
              nome1 = True
  
          if nome1 == True:
            
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

          for palavra in palavras:
            nome2 = len(palavra)
            nome2 = nome2 - 1
            if palavra[nome2] == ':':
              nome1 = True
  
          if nome1 == True:
            
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
        
        for palavra in palavras:
          valorlido = palavra
          binarioopL = opcodeL.get(valorlido,"")
          with open("C:/Users/Trojan/Documents/Codificadores/Arquitetura/binario.txt", "a") as file:
            file.write(binarioopL)
        
        if palavras[0] in vetorLUI or palavras[1] in vetorLUI:
        
          for palavra in palavras:
              valorlido = palavra
              binarioL = reg.get(valorlido,"")
              vetor.append(binarioL)

          for palavra in palavras:
            nome2 = len(palavra)
            nome2 = nome2 - 1
            if palavra[nome2] == ':':
              nome1 = True
  
          if nome1 == True:

            num = int(valorlido)
            num1 = bin(num)[2:]
            representa = num1.zfill(16)
            
            with open("C:/Users/Trojan/Documents/Codificadores/Arquitetura/binario.txt", "a") as file:
              file.write("00000")
              file.write(vetor[2])
              file.write(representa)
              vetor.clear()
                
            with open("C:/Users/Trojan/Documents/Codificadores/Arquitetura/binario.txt", "a") as file:
              file.write("\n")

            break

          else:
            
            for palavra in palavras: 
              valorlido = palavra
              binarioL = reg.get(valorlido,"")
              vetor.append(binarioL)
            
            num = int(valorlido)
            num1 = bin(num)[2:]
            representa = num1.zfill(16)
            
            with open("C:/Users/Trojan/Documents/Codificadores/Arquitetura/binario.txt", "a") as file:
              file.write("00000")
              file.write(vetor[1])
              file.write(representa)
              vetor.clear()
              
            with open("C:/Users/Trojan/Documents/Codificadores/Arquitetura/binario.txt", "a") as file:
              file.write("\n")

            break
        
        if palavras[0] in vetorB or palavras[1] in vetorB:
        
          for palavra in palavras:
              valorlido = palavra
              binarioL = reg.get(valorlido,"")
              vetor.append(binarioL)

          for palavra in palavras:
            nome2 = len(palavra)
            nome2 = nome2 - 1
            if palavra[nome2] == ':':
              nome1 = True

          if nome1 == True:
          
            if palavras[4] in adress:
              
              for i in range(len(palavras)): #Filtro para retirar as Parenteses
                palavras[i] = palavras[i].replace(':', '')
              for palavra in palavras:
                valorlido = palavra
                binarioL = adress.get(valorlido,"")
                vetor.append(binarioL)
              
              numero = vetor[9]
              numero1 = int(numero)
              numero1 = numero1 - 1
              numero2 = vetor[5]
              numero3 = int(numero2)
              numero5 = numero2 - numero1
              numero4 = bin(numero5)[2:]
              representa = numero4.zfill(16)
              
              complemento = ''.join('1' if bit == '0' else '0' for bit in representa)  # Inversão de bits
              carry = 1
              resultado = ''
    
              for bit in reversed(complemento):
                if carry == 1:
                    if bit == '0':
                        resultado = '1' + resultado
                        carry = 0
                    else:
                        resultado = '0' + resultado
                else:
                    resultado = bit + resultado

                
            with open("C:/Users/Trojan/Documents/Codificadores/Arquitetura/binario.txt", "a") as file:
              file.write(vetor[2])
              file.write(vetor[3])
              file.write(resultado)
              vetor.clear()
                
            with open("C:/Users/Trojan/Documents/Codificadores/Arquitetura/binario.txt", "a") as file:
              file.write("\n")

            break

          else:
            
            if palavras[3] in adress:
              
              for palavra in palavras:
                valorlido = palavra
                binarioL = adress.get(valorlido,"")
                vetor.append(binarioL)

              numero = vetor[7]
              numero1 = int(numero)
              numero1 = numero1 - 1
              numero2 = vetor[4]
              numero3 = int(numero2)
              numero5 = numero3 - numero1
              numero4 = bin(numero5)[2:]
              representa = numero4.zfill(16)
              
              complemento = ''.join('1' if bit == '0' else '0' for bit in representa)  # Inversão de bits
              carry = 1
              resultado = ''
    
              for bit in reversed(complemento):
                if carry == 1:
                    if bit == '0':
                        resultado = '1' + resultado
                        carry = 0
                    else:
                        resultado = '0' + resultado
                else:
                    resultado = bit + resultado
            
            with open("C:/Users/Trojan/Documents/Codificadores/Arquitetura/binario.txt", "a") as file:
              file.write(vetor[1])
              file.write(vetor[2])
              file.write(resultado)
              vetor.clear()
              
            with open("C:/Users/Trojan/Documents/Codificadores/Arquitetura/binario.txt", "a") as file:
              file.write("\n")

            break

        elif palavras[0] in vetorW or palavras[1] in vetorW:
          
          for i in range(len(palavras)): #Filtro para retirar as Parenteses
            palavras[i] = palavras[i].replace('(', '')
            palavras[i] = palavras[i].replace(')', '')

          for palavra in palavras:
              valorlido = palavra
              binarioL = reg.get(valorlido,"")
              vetor.append(binarioL)
    
          for palavra in palavras:
            nome2 = len(palavra)
            nome2 = nome2 - 1
            if palavra[nome2] == ':':
              nome1 = True
  
          if nome1 == True:
            
            partes = palavras[3].split('$')
            
            partes[1] = "$" + partes[1]
            
            for palavra in palavras:
              valorlido = palavra
              binarioL = reg.get(valorlido,"")
              vetor.append(binarioL)
            
            for palavra in partes:
              valorlido = palavra
              binarioL = reg.get(valorlido,"")
              vetor.append(binarioL)

            num = int(partes[0])
            num1 = bin(num)[2:]
            representa = num1.zfill(16)
            
            with open("C:/Users/Trojan/Documents/Codificadores/Arquitetura/binario.txt", "a") as file:
              file.write(vetor[9])
              file.write(vetor[2])
              file.write(representa)
              vetor.clear()
                
            with open("C:/Users/Trojan/Documents/Codificadores/Arquitetura/binario.txt", "a") as file:
              file.write("\n")

            break

          else:
           
            partes = palavras[2].split('$')
            partes[1] = "$" + partes[1]
            
            for palavra in palavras:
              valorlido = palavra
              binarioL = reg.get(valorlido,"")
              vetor.append(binarioL)
            
            for palavra in partes:
              valorlido = palavra
              binarioL = reg.get(valorlido,"")
              vetor.append(binarioL)

            num = int(partes[0])
            num1 = bin(num)[2:]
            representa = num1.zfill(16)
            
            with open("C:/Users/Trojan/Documents/Codificadores/Arquitetura/binario.txt", "a") as file:
              file.write(vetor[7])
              file.write(vetor[1])
              file.write(representa)
              vetor.clear()
                
            with open("C:/Users/Trojan/Documents/Codificadores/Arquitetura/binario.txt", "a") as file:
              file.write("\n")

            break

        else:

          for palavra in palavras:
              valorlido = palavra
              binarioL = reg.get(valorlido,"")
              vetor.append(binarioL)

          for palavra in palavras:
            nome2 = len(palavra)
            nome2 = nome2 - 1
            if palavra[nome2] == ':':
              nome1 = True
  
          if nome1 == True:
            
            num = int(valorlido)
            num1 = bin(num)[2:]
            representa = num1.zfill(16)
          
            with open("C:/Users/Trojan/Documents/Codificadores/Arquitetura/binario.txt", "a") as file:
              file.write(vetor[3])
              file.write(vetor[2])
              file.write(representa)
              vetor.clear()
                
            with open("C:/Users/Trojan/Documents/Codificadores/Arquitetura/binario.txt", "a") as file:
              file.write("\n")

            break

          else:

            for palavra in palavras: 
              valorlido = palavra
              binarioL = reg.get(valorlido,"")
              vetor.append(binarioL)
            
            num = int(valorlido)
            num1 = bin(num)[2:]
            representa = num1.zfill(16)
            
            
            with open("C:/Users/Trojan/Documents/Codificadores/Arquitetura/binario.txt", "a") as file:
              file.write(vetor[2])
              file.write(vetor[1])
              file.write(representa)
              
              vetor.clear()
              
            with open("C:/Users/Trojan/Documents/Codificadores/Arquitetura/binario.txt", "a") as file:
              file.write("\n")

            break

    #COMEÇA A BUSCA DAS INSTRUÇÕES DO TIPO J ==================================================================================

    elif palavras[0] in vetorJ:

        for palavra in palavras:
            
          valorlido = palavra
          binarioopJ = opcodeJ.get(valorlido,"")
          with open("C:/Users/Trojan/Documents/Codificadores/Arquitetura/binario.txt", "a") as file:
            file.write(binarioopJ)
      
        if palavras[1] in adress:
              
            for palavra in palavras:
              valorlido = palavra
              binarioL = adress.get(valorlido,"")
              vetor.append(binarioL)
            
            numero = vetor[1]
            numero1 = int(numero)
            numero1 = numero1 - 1
            numero4 = bin(numero1)[2:]
            representa = numero4.zfill(20)
            representa1 = "1" 
            valorfinal = representa1 + representa
            representa = valorfinal.zfill(26)
         
        with open("C:/Users/Trojan/Documents/Codificadores/Arquitetura/binario.txt", "a") as file:
          file.write(representa)
          vetor.clear()
              
        with open("C:/Users/Trojan/Documents/Codificadores/Arquitetura/binario.txt", "a") as file:
          file.write("\n")

        break
  
    
    

    
        

    
  