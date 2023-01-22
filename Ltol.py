def converter():
    exit = False
    while not exit:

        print('Seja Bem vindo ao nosso conversor de maísculo e minúsculo')
        print('1. Minúsculo para maiúsculo')
        print('2. Maiúsculo para minúsculo')
        print('3. Transformar as primeiras letras em maiúsculo')
        print('4. Sair')

        choice = int(input('Escolha uma das opções: '))

        if choice == 1:
            sentence = input('Digite a frase: ')
            print(sentence.upper())
        elif choice == 2:
            sentence = input('Digite a frase: ')
            print(sentence.lower())
        elif choice == 3:
            sentence = input('Digite a frase: ')
            print(sentence.title())
        elif choice == 4:
            print('Até a próxima!')
            exit = True
        else:
            print('Opção inválida, tente novamente')


converter()
