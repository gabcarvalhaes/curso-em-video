algoritmo "semnome"

var
   nota, maior: real
   qntd_alunos, contador: inteiro
   nome, melhor: caractere
inicio
      escreval("------------------------------")
      escreval("   Escola Santa Paciência")
      escreval("------------------------------")
      escreva("Quantos alunos essa turma tem? ")
      leia(qntd_alunos)
      escreval("------------------------------")
      contador <- 1
      enquanto (qntd_alunos >= contador  ) faca
               escrevaL("ALUNO", contador )
               escreval("---------------")
               escreva("Nome do aluno: ")
               leia(nome)
               escreva("Nota de ", nome, ": ")
               leia(nota)
               escreval("---------------")
               Se (nota > maior) entao
                  maior <- nota
                  melhor <- nome
               FimSe
               contador <- contador + 1
      FimEnquanto
               escreva("O melhor aproveitamente foi de ", melhor, " com a nota ", maior)

      
fimalgoritmo
