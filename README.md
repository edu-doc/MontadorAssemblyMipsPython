# MONTADOR ASSEMBLY

# Sobre o projeto

O Projeto é um trabalho da disciplina de Arquitetura de Computadores, onde devemos montar um montador (assembler) simples para o MIPS.

De modo que a aplicação deve receber como entrada um arquivo de texto com código de montagem (assembly) do MIPS sem erros de sintaxe 
e devolver como saída um arquivo de texto com programa equivalente em linguagem de montagem.

O montador deve gerar código de máquina apenas das instruções, não sendo necessário usar 
as diretivas de montador (.data, .text, etc). Seu montador deve inicialmente passar por todo o 
código procurando rótulos (labels), os quais são identificados por um nome seguido de doispontos e guardar a informação da linha onde foram encontrados (isso é sua tabela de 
símbolos). Em seguida, percorrendo todo o código novamente, e traduzir cada instrução para 
código de máquina. Nas instruções que fazem referência aos labels, os mesmos devem ser
substituídos pelos respectivos valores relativos (instruções condicionais fazem referência ao 
valor de PC e incondicionais são pseudodiretas). Seu assembler ainda deve considerar que o 
endereço de memória inicial do programa é sempre 0x00400000. A saída gerada pode ser em 
em hexadecimal (ou seja, cada 4 bits equivalente a 1 caracter hexa).

## Fotos do Arquivo Trabalho
![Web 1](https://github.com/edu-doc/MontadorAssemblyMipsPython/blob/main/fotos/pg1.png)
![Web 1](https://github.com/edu-doc/MontadorAssemblyMipsPython/blob/main/fotos/pg2.png)
![Web 1](https://github.com/edu-doc/MontadorAssemblyMipsPython/blob/main/fotos/pg3.png)

# Tecnologias utilizadas
## Back end
- Python
- MARS MIPS

# Como executar o projeto

## Back end
Pré-requisitos: Python,
                MARS MIPS simulator

```bash
# clonar repositório
  git clone https://github.com/edu-doc/MontadorAssemblyMipsPython

# acessar o arquivo numero.txt
  colocar as instruções em MIPS que você quer montar

# executar o projeto
  assemblyUpgrade

# acessar o arquivo binario.txt
  resposta será encontrada em binario.

# acessar o arquivo hexadecimal.txt
  resposta será encontrada em hexadecimal.
```

# Grupo

Antonio Eduardo de Oliveira Carmo

Eduardo Paz Vieira

