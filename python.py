# Registro de matricula
rm = int(input("Insira seu RM: "))

# Idade do aluno matriculado
idade = int(input("Insira sua idade: "))

# Se a idade do aluno for iqual ou maior que 18 anos, exibir a mensagem:
# "Sua participação foi autorizada, aluno de RM {RM}!"
# "Mais informações foram enviadas para o e-mail cadastrado!"
if int(idade) >= 18:
    print("Sua participação foi autorizada, aluno de RM {}!".format(rm))
    print("Mais informações foram enviadas para o e-mail cadastrado!")

# Se não, crie a variável <autorizado>, que exibe a mensagem:
# "Você possui autorização dos responsaveis? Insira S para Sim ou N para não: "
else:
    autorizado = input("Você possui autorização dos responsaveis? Insira S para Sim ou N para Não: ")

    # Se a autorização for verdadeira, exibir a mensagem:
    # "Sua participação foi autorizada, aluno de RM {RM}!"
    # "Mais informações serão enviadas para o e-mail dos seus responsáveis!"
    if autorizado == "S":
        print("Sua participação foi autorizada, aluno de RM {}!".format(rm))
        print("Mais informações serão enviadas para o e-mail dos seus responsáveis!")

    # Se não, exibir a mensagem:
    # "Sua participação não foi autorizada por causa da sua idade."
    else:
        print("Sua participação não foi autorizada por causa da sua idade.")