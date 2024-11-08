import os
import platform
# "def limpar tela", tem como função limpar o terminal  a cada opção do usuário. Para utilizar esse comando precisei importar a biblioteca "os".
def limpar_tela():
    so = platform.system()
    if so == "Windows":
        os.system("cls")
    else:
        os.system("clear")
# utilizei o método "def menu_principal" para o usuário poder voltar ao menu, quando ele termina a execução da funcionalidade.
def menu_principal():
    limpar_tela()
    print("Bem-Vindo ao MetrôBot \n")
    print("1. Cadastrar usuário")
    print("2. Tirar dúvidas")
    print("3. Mapa da estação")
    print("4. Encerrar\n")

    escolha_usuário = input("Qual das opções, você precisa ? ")
    
    if escolha_usuário == "1":
        cadastrar_usuario()
    elif escolha_usuário == "2":
        tirar_duvidas()
    elif escolha_usuário == "3":
        mapa_estacao()
    elif escolha_usuário == "4":
        print("Encerrando o programa.")
    else:
        print("Opção inválida!")
        menu_principal()
    
    
def cadastrar_usuario():
    limpar_tela()
    tentativas = 0
    max_tentativas = 3
    #enquanto a tentativa do usuário for menor que 3,o sistema ira permitir ele tentar escrever o email novamente ,caso erre 
    while tentativas < max_tentativas:
        email_usuário = input("Insira o email:")
        email_correto = input(f"O email está correto {email_usuário} ? (S/N) ").lower()
        #o .lower ira registar a resposta do usuário em minusculo , desse modo n necessito colocar email_correto == s or email_correto == S
        if email_correto == "s":
            print("Email cadastrado com sucesso.")
            break
        else:
            tentativas += 1 
            print("Tente novamente, por gentileza.")
    if tentativas == max_tentativas:
            print("Número máximo de tentativas para o email atingido. Retornando ao Menu principal.")
            input("Pressione Enter para retornar ao menu.")
            menu_principal()
            
        
    tentativas = 0 
    while tentativas < max_tentativas:         
        senha_usuário = input("Insira a senha: ")
        senha_correto = input(f"A senha está correto {senha_usuário} ? (S/N)").lower()
        #Coloquei o "lower" para que o sistema consiga ler "S" maiusuculo e o "s" minusculo ,sem a necessidade de fazer o "or".
        if senha_correto == "s":
            print("Senha cadastrado com sucesso.") 
            input("Pressione Enter para retornar ao menu.")
            menu_principal()
            break
        else:
            tentativas += 1 
            print("Tente novamente, por gentileza.")
            
    if tentativas == max_tentativas:
        print("Número máximo de tentativas para a senha atingido.")
        input("Pressione Enter para retornar ao menu.")
        menu_principal()
        
def tirar_duvidas():
    while True:
        limpar_tela()
        print("Qual seria a sua dúvida:\n\n1. Tarifa\n2. Bicicleta\n3. Contatos\n4. Outra dúvida\n")
        duvida_usuario = input("Qual das opções acima voce gostaria ? ")
        
        if duvida_usuario == "1":#caso o usuario escolha duvida sobre a tarifa
            limpar_tela()
            print("A política tarifária de todo o sistema metroferroviário é definida pelo Governo do Estado de São Paulo.\nO valor do bilhete unitário é R$ 5,00.\n")
            input("Pressione Enter para retornar ao menu.")
            menu_principal()
            #outra_duvida = input("Teria outra dúvida ? (S/N)").lower()
            #if outra_duvida == "s":
              #  print()
        elif duvida_usuario == "2":# caso o usuario escolha o opcao de duvidas sobre a bicicleta
            limpar_tela()
            duvida2= """
            O embarque de bicicletas é permitido de segunda a sexta-feira, das 10h às 16h e das 21h à meia-noite, e o dia todo aos finais de semana e feriados. 
            O ciclista pode transportar uma bicicleta convencional ou elétrica, desde que esteja limpa (sem barro, lama ou graxa).

            Nas escadas rolantes, as bicicletas só podem ser transportadas subindo. Nas escadas fixas, devem ser carregadas. 
            Elevadores e esteiras rolantes não podem ser usados para transporte de bicicletas. 
            Dentro das estações, a bicicleta deve ser empurrada e mantida ao lado do ciclista, sem ser largada no chão ou sobre os bancos.

            Menores de 12 anos devem ser acompanhados por um responsável. 
            Até 4 bicicletas são permitidas por viagem, e o embarque deve ser feito no último carro do trem. 
            Dentro do trem, o ciclista deve evitar obstruir portas e manter distância para não impedir a circulação de passageiros.

            Em casos de grande fluxo ou problemas no sistema, os ciclistas podem ser orientados a não embarcar com suas bicicletas.
            """
         
            print(duvida2)
            input("Pressione Enter para retornar ao menu.")
            menu_principal()
        
        elif duvida_usuario == "3": #caso o usuario escolha a opcao de contatos
            limpar_tela()
            print("Central de Atendimento funciona:\nSegunda a Sexta, das 6h30 às 22h00\nSábado e Domingo, das 8h00 às 18h00")
            print("====================")
            print("via WhatsApp:\n(11)91277-6323")
            print("====================")
            print("via telefone:\n0800.770.7106\n")
            input("Pressione Enter para retornar ao menu.")
            menu_principal()
            
        elif duvida_usuario == "4": #caso o usuario escolha outra duvida
            limpar_tela()
            duvida_usuario = input("Qual seria sua dúvida ? ")
            print("Dúvida resgistrada.")
            input("Pressione Enter para retornar ao menu.")
            menu_principal()
    
def mapa_estacao():
    limpar_tela()
    print("Mapa da estação da CCR.\n\n1-Linha 4(Amarela)\n2-Linha 5(Lilás)\n3-Linha 8(Diamante)\n4-Linha 9(Esmeralda)\n")
    linha_usuario = input("Qual linha você gostaria de acessar ? ")
    
    if linha_usuario == "1": # usuario escolha a opcao 1
        limpar_tela()
        print("Linha Amarela no SENTIDO Luz:\n")
        print("Vila Sônia --> São Paulo-Morumbi --> Butantã --> Pinheiros --> Faria Lima --> Fradique Coutinho --> Oscar Freire --> Paulista-Pernambucanas --> Higienópolis-Mackenzie --> República --> Luz.")
        
        print("=====================================")
        
        print("Linha amarela no SENTIDO Vila Sonia:\n ")
        print("Luz --> República --> Higienópolis-Mackenzie --> Paulista-Pernambucanas --> Oscar Freire --> Fradique Coutinho --> Faria Lima --> Pinheiros --> Butantã --> São Paulo-Morumbi --> Vila Sônia.\n")
        
        ponto_interesse=input("Gostaria de saber os Pontos de interesse ? (S/N) ").lower() #usuario escolha saber os pontos de interesse 
        limpar_tela()
        
        if ponto_interesse == "s":
            limpar_tela()
            estacao_usuario =input("1.Vila Sônia\n2.São Paulo-Morumbi\n3.Butantã\n4.Pinheiros\n5.Faria Lima\n6.Fradique Coutinho\n7.Oscar Freire\n8.Paulista-Pernambucanas\n9.Higienópolis-Mackenzie\n10.República\n11.Luz.\nQual das estações você gostaria de saber ? (inserir o número) ")# usuario escolhe uma estacao , e irá exiber os pontos
            
            if estacao_usuario == "1":
                limpar_tela()
                print("Os Ponto(s) de Interesse:\nPátio Vila Sônia – Sede da concessionária ViaQuatro\nTerminal de Ônibus Vila Sônia\nHorário de funcionamento:\nTodos os dias, das 4:40 à meia-noite.")
                input("Pressione Enter para retornar ao menu.")
                menu_principal()
                
            elif estacao_usuario == "2":
                limpar_tela()
                print("Os Ponto(s) de Interesse:\nEstádio Cícero Pompeu de Toledo - Morumbi\nHorário de funcionamento:\nTodos os dias, das 4:40 à meia-noite.")
                input("Pressione Enter para retornar ao menu.")
                menu_principal()
                
            elif estacao_usuario == "3":
                limpar_tela()
                print("Os Ponto(s) de Interesse:\nInstituto Butantã\nCidade Universitária (USP)\nJockey Club de São Paulo\nHorário de funcionamento:\nTodos os dias, das 4:40 à meia-noite.")
                input("Pressione Enter para retornar ao menu.")
                menu_principal()
                
            elif estacao_usuario == "4":
                limpar_tela()
                print("Os Ponto(s) de Interesse:\nCentro Brasileiro Britânico\nPraça Victor Civita\nSESC Pinheiros\nTeatro Cultura Inglesa\nHorário de funcionamento:\nTodos os dias, das 4:40 à meia-noite.")
                input("Pressione Enter para retornar ao menu.")
                menu_principal()
                
            elif estacao_usuario == "5":
                limpar_tela()
                print("Os Ponto(s) de Interesse:\nSESC Pinheiros\nTeatro Cultura Inglesa\nMercado Municipal de Pinheiros\nInstituto Tomie Ohtake\nHorário de funcionamento:\nTodos os dias, das 4:40 à meia-noite.")
                input("Pressione Enter para retornar ao menu.")
                menu_principal()
                
            elif estacao_usuario == "6":
                limpar_tela()
                print("Os Ponto(s) de Interesse:\nSanpo Bento Deli\nCarrefour Express\nCoffee Lab\nHorário de funcionamento:\nTodos os dias, das 4:40 à meia-noite.")
                input("Pressione Enter para retornar ao menu.")
                menu_principal()
                
            elif estacao_usuario == "7":
                limpar_tela()
                print("Os Ponto(s) de Interesse:\nEscola de Enfermagem da USP\nHorário de funcionamento:\nTodos os dias, das 4:40 à meia-noite.")
                input("Pressione Enter para retornar ao menu.")
                menu_principal()
                
            elif estacao_usuario == "8":
                limpar_tela()
                print("Os Ponto(s) de Interesse:\nEstádio Paulo Machado de Carvalho - Pacaembu\nTeatro Augusta\nHospital das Clínicas\nHorário de funcionamento:\nTodos os dias, das 4:40 à meia-noite.")
                input("Pressione Enter para retornar ao menu.")
                menu_principal()
                
            elif estacao_usuario == "9":
                limpar_tela()
                print("Os Ponto(s) de Interesse:\nSESC Consolação\nPraça Roosevelt\nHorário de funcionamento:\nTodos os dias, das 4:40 à meia-noite.")
                input("Pressione Enter para retornar ao menu.")
                menu_principal()
                
            elif estacao_usuario == "10":
                limpar_tela()
                print("Os Ponto(s) de Interesse:\nBiblioteca Mário de Andrade\nPraça da República\nTeatro Municipal de São Paulo\nGaleria do Rock\nHorário de funcionamento:\nTodos os dias, das 4:40 à meia-noite.")
                input("Pressione Enter para retornar ao menu.")
                menu_principal()
                
            else:
                limpar_tela()
                print("Os Ponto(s) de Interesse:\nMuseu de Arte Sacra\nMuseu da Língua Portuguesa\nPinacoteca do Estado\nSala São Paulo\nMemorial da Resistência de São Paulo\nHorário de funcionamento:\nTodos os dias, das 4:40 à meia-noite.")
                input("Pressione Enter para retornar ao menu.")
                menu_principal()
                
        else:
            print("Obriga por utilziar!")
            input("Pressione Enter para retornar ao menu.")
            menu_principal()
            
    elif linha_usuario == "2":
        limpar_tela()
        print("Linha Lilás no SENTIDO Chácara Klabin:\n")
        print("Capão Redondo --> Campo Limpo --> Vila das Belezas --> Giovanni Gronchi --> Santo Amaro --> Largo Treze --> Adolfo Pinheiro --> Alto da Boa Vista --> Borba Gato--> Brooklin --> Campo Belo --> Eucaliptos --> Moema --> AACD-Servidor --> Hospital São Paulo --> Santa Cruz --> Chácara Klabin. ")
        
        print("===========================================")
        print("Linha lilás no SENTIDO Capao Redondo:\n")
        
        print("Chácara Klabin --> Santa Cruz --> Hospital São Paulo --> AACD-Servidor --> Moema --> Eucaliptos--> Campo Belo --> Brooklin --> Borba Gato --> Alto da Boa Vista --> Adolfo Pinheiro --> Largo Treze --> Santo Amaro --> Giovanni Gronchi --> Vila das Belezas --> Campo Limpo --> Capão Redondo.\n ")
        ponto_interesse=input("Gostaria de saber os Pontos de interesse ? (S/N) ").lower()
        limpar_tela()
        
        if ponto_interesse =="s":
            ponto_interesse = input("1.Chácara klabin\n2.Santa Cruz\n3.Hospital São Paulo\n4.AACD-Servidor\n5.Moema\n6.Eucaliptos\n7.Campo Belo\n8.Brooklin\n9.Borba Gato\n10.Alto da Boa Vista\n11.Adolfo Pinheiro\n12.Largo Treze\n13.Santo Amaro\n14.Giovanni Gronchi\n15.Vila das Belezas\n16.Campo Limpo\n17.Capão Redondo.\nQual das estações você gostaria de saber ? (inserir o número) ")
        
            if ponto_interesse == "1":
                limpar_tela()
                print("O(s) Ponto(s) de Interesse:\nCasa Modernista\nHorário de funcionamento:\nTodos os dias, das 4:40 à meia-noite.")
             
            elif ponto_interesse == "2":
                limpar_tela()
                print("O(s) Ponto(s) de Interesse:\nMuseu Lasar Segall\nIgreja Nossa Senhora da Saúde\nFundação Dorina Nowill\nHorário de funcionamento:\nTodos os dias, das 4:40 à meia-noite.")
                
            elif ponto_interesse == "3":
                limpar_tela()
                print("O(s) Ponto(s) de Interesse:\nHospital São Paulo\nEscola Paulista de Medicina da Universidade Federal de São Paulo\nMaternidade do Amparo Maternal\nAPAE São Paulo\nHorário de funcionamento:\nTodos os dias, das 4:40 à meia-noite.")
                
            elif ponto_interesse == "4":
                limpar_tela()
                print("O(s) Ponto(s) de Interesse:\nHospital do Servidor Público\nAACD\nHorário de funcionamento:\nTodos os dias, das 4:40 à meia-noite.")
                
            elif ponto_interesse == "5":
                limpar_tela()
                print("O(s) Ponto(s) de Interesse:\nParóquia Nossa Senhora Aparecida\nParque das Bicicletas\nHorário de funcionamento:\nTodos os dias, das 4:40 à meia-noite.")
                
            elif ponto_interesse == "6":
                limpar_tela()
                print("O(s) Ponto(s) de Interesse:\nShopping Ibirapuera\nHorário de funcionamento:\nTodos os dias, das 4:40 à meia-noite.")
                
            elif ponto_interesse == "7":
                limpar_tela()
                print("O(s) Ponto(s) de Interesse:\nSão Fernando Golf Club\nVida noturna\nHorário de funcionamento:\nTodos os dias, das 4:40 à meia-noite.")
                
            elif ponto_interesse == "8":
                limpar_tela()
                print("O(s) Ponto(s) de Interesse:\nShopping Morumbi\nHorário de funcionamento:\nTodos os dias, das 4:40 à meia-noite.")
                
            elif ponto_interesse == "9":
                limpar_tela()
                print("O(s) Ponto(s) de Interesse:\nConsulado Geral dos Estados Unidos\nForo Regional de Santo Amaro\nHorário de funcionamento:\nTodos os dias, das 4:40 à meia-noite.")
                
            elif ponto_interesse == "10":
                limpar_tela()
                print("O(s) Ponto(s) de Interesse:\nCatedral Anglicana de São Paulo\nClube Hípico de Santo Amaro\nHorário de funcionamento:\nTodos os dias, das 4:40 à meia-noite.")
                
            elif ponto_interesse == "11":
                limpar_tela()
                print("O(s) Ponto(s) de Interesse:\nHospital Santa Casa de Misericórdia\nTeatro Paulo Eiró\nHospital Regional Sul\nHorário de funcionamento:\nTodos os dias, das 4:40 à meia-noite.")
                
            elif ponto_interesse == "12":
                limpar_tela()
                print("O(s) Ponto(s) de Interesse:\nSesc Santo Amaro\nMercado de Santo Amaro\nPoupatempo\nHorário de funcionamento:\nTodos os dias, das 4:40 à meia-noite.")
                
            elif ponto_interesse == "13":
                limpar_tela()
                print("O(s) Ponto(s) de Interesse:\nTerminal Guido Caloi\nHorário de funcionamento:\nTodos os dias, das 4:40 à meia-noite.")
                
            elif ponto_interesse == "14":
                limpar_tela()
                print("O(s) Ponto(s) de Interesse:\nTerminal João Dias\nHorário de funcionamento:\nTodos os dias, das 4:40 à meia-noite.")
                
            elif ponto_interesse == "15":
                limpar_tela()
                print("O(s) Ponto(s) de Interesse:\nUBS Parque Arariba\nUBS Vila das Belezas\nHorário de funcionamento:\nTodos os dias, das 4:40 à meia-noite.")
                
            elif ponto_interesse == "16":
                limpar_tela()
                print("O(s) Ponto(s) de Interesse:\nSesc Campo Limpo\nPrefeitura Regional do Campo Limpo\nHorário de funcionamento:\nTodos os dias, das 4:40 à meia-noite.")
                
            else:
                limpar_tela()
                print("O(s) Ponto(s) de Interesse:\nParque Santo Dias\nHorário de funcionamento:\nTodos os dias, das 4:40 à meia-noite.")
                
        else:
            print("Obrigado por utilizar!")
            input("Pressione Enter para retornar ao menu.")
            menu_principal()
            
    elif linha_usuario == "3":
        limpar_tela()
        print("Linha Diamante no SENTIDO Amador Bueno:\n ")
        
        print("Júlio Prestes --> Palmeiras-Barra Funda --> Lapa --> Domingos de Moraes --> Imperatriz Leopoldina --> Presidente Altino --> Osasco --> Comandante Sampaio --> Quitaúna --> General Miguel Costa --> Carapicuíba --> Santa Terezinha --> Antonio João --> Barueri --> Jardim Belval --> Jandira --> Sagrado Coração --> Engenheiro Cardoso --> Itapevi --> Santa Rita --> Amador Bueno. ")
        
        print("==================================================================================")
        print("Linha Diamante no SENTIDO Júlio Prestes:\n")
        
        print("Amador Bueno --> Santa Rita --> Itapevi --> Engenheiro Cardoso --> Sagrado Coração --> Jandira --> Jardim Belval --> Barueri --> Antonio João --> Santa Terezinha --> Carapicuíba --> General Miguel Costa --> Quitaúna --> Comandante Sampaio --> Osasco --> Presidente Altino --> Imperatriz Leopoldina --> Domingos de Moraes --> Lapa --> Palmeiras-Barra Funda --> Júlio Prestes.\n ")
        
        ponto_interesse=input("Gostaria de saber os Pontos de interesse ? (S/N) ").lower()
        
        if ponto_interesse == "s":
            limpar_tela()
            ponto_interesse = input("1.Amador Bueno\n2.Santa Rita\n3.Itapevi\n4.Engenheiro Cardoso\n5.Sagrado Coração\n6.Jandira\n7.Jardim Belval\n8.Barueri\n9.Antonio João\n10.Santa Terezinha\n11.Carapicuíba\n12.General Miguel Costa\n13.Quitaúna\n14.Comandante Sampaio\n15.Osasco\n16.Presidente Altino\n17.Imperatriz Leopoldina\n18.Domingos de Moraes\n19.Lapa\n20.Palmeiras-Barra Funda\n21.Júlio Prestes.\nQual das estações você gostaria de saber ? (inserir o número) ")
            
            if ponto_interesse =="1":
                limpar_tela()
                print("O(s) Ponto(s) de Interesse:\nPraça Novo Amador\nClube e Pesqueiro J&I\nPesqueiro Boa Vida\nHorário de funcionamento:\nTodos os dias, das 4:40 à meia-noite.")
                
            elif ponto_interesse ==  "2":
                limpar_tela()
                print("O(s) Ponto(s) de Interesse:\nIgreja Matriz Santa Rita de Cássia\nMuseu Histórico Zequinha de Abreu\nParque Turístico Municipal\nHorário de funcionamento:\nTodos os dias, das 4:40 à meia-noite.")
                
            elif ponto_interesse ==  "3":
                limpar_tela()
                print("O(s) Ponto(s) de Interesse:\nMercado Municipal de Itapevi\nCentro histórico de Itapevi\nHorário de funcionamento:\nTodos os dias, das 4:40 à meia-noite.")
                
            elif ponto_interesse ==  "4":
                limpar_tela()
                print("O(s) Ponto(s) de Interesse:\nParóquia Nossa Senhora Medianeira de Todas as Graças\n Praça Carlos de Castro\nHorário de funcionamento:\nTodos os dias, das 4:40 à meia-noite.")
                
            elif ponto_interesse ==  "5":
                limpar_tela()
                print("O(s) Ponto(s) de Interesse:\nCapela do Sagrado Coração de Jesus\nCentro de Jandira\nHorário de funcionamento:\nTodos os dias, das 4:40 à meia-noite.")
                
            elif ponto_interesse ==  "6":
                limpar_tela()
                print("O(s) Ponto(s) de Interesse:\nTeatro Municipal Luiz Gonzaga\nParque da Cidade de Jandira\nHorário de funcionamento:\nTodos os dias, das 4:40 à meia-noite.")
                
            elif ponto_interesse ==  "7":
                limpar_tela()
                print("O(s) Ponto(s) de Interesse:\nParóquia São Francisco de Assis\nPraça Jardim Belval\nHorário de funcionamento:\nTodos os dias, das 4:40 à meia-noite.")
                
            elif ponto_interesse ==  "8":
                limpar_tela()
                print("O(s) Ponto(s) de Interesse:\nParque Municipal Dom José\nMuseu da Bíblia\nHorário de funcionamento:\nTodos os dias, das 4:40 à meia-noite.")
                
            elif ponto_interesse ==  "9":
                limpar_tela()
                print("O(s) Ponto(s) de Interesse:\nShopping Barueri\nParque Ecológico de Barueri\nHorário de funcionamento:\nTodos os dias, das 4:40 à meia-noite.")
                
            elif ponto_interesse ==  "10":
                limpar_tela()
                print("O(s) Ponto(s) de Interesse:\nIgreja Santa Terezinha\nPraça Santa Terezinha\nHorário de funcionamento:\nTodos os dias, das 4:40 à meia-noite.")
                
            elif ponto_interesse ==  "11":
                limpar_tela()
                print("O(s) Ponto(s) de Interesse:\nMercado Municipal de Carapicuíba\nParque Gabriel Chucre\nHorário de funcionamento:\nTodos os dias, das 4:40 à meia-noite.")
                
            elif ponto_interesse ==  "12":
                limpar_tela()
                print("O(s) Ponto(s) de Interesse:\nAldeia Jesuítica de Carapicuíba\nParque da Aldeia\nHorário de funcionamento:\nTodos os dias, das 4:40 à meia-noite.")
                
            elif ponto_interesse ==  "13":
                limpar_tela()
                print("O(s) Ponto(s) de Interesse:\nMuseu de Osasco\nQuartel do Exército Brasileiro\nHorário de funcionamento:\nTodos os dias, das 4:40 à meia-noite.")
                
            elif ponto_interesse ==  "14":
                limpar_tela()
                print("O(s) Ponto(s) de Interesse:\nCentro de Treinamento do Corinthians\nParóquia Nossa Senhora dos Remédios\nHorário de funcionamento:\nTodos os dias, das 4:40 à meia-noite.")
                
            elif ponto_interesse ==  "15":
                limpar_tela()
                print("O(s) Ponto(s) de Interesse:\nShopping Osasco Plaza\nCalçadão de Osasco\nParque Ecológico Dionísio Alvarez Mateos\nHorário de funcionamento:\nTodos os dias, das 4:40 à meia-noite.")
                
            elif ponto_interesse ==  "16":
                limpar_tela()
                print("O(s) Ponto(s) de Interesse:\nComplexo Presidente Altino (CPTM)\nPraça Dr. Mário Ottoni Rezende\nHorário de funcionamento:\nTodos os dias, das 4:40 à meia-noite.")
                
            elif ponto_interesse ==  "17":
                limpar_tela()
                print("O(s) Ponto(s) de Interesse:\nMercado da Vila Leopoldina\nPraça do Centro Cultural da Vila Leopoldina\nHorário de funcionamento:\nTodos os dias, das 4:40 à meia-noite.")
                
            elif ponto_interesse ==  "18":
                limpar_tela()
                print("O(s) Ponto(s) de Interesse:\nIgreja de São Pedro e São Paulo\nLargo da Vila Anastácio\nHorário de funcionamento:\nTodos os dias, das 4:40 à meia-noite.")
                
            elif ponto_interesse ==  "19":
                limpar_tela()
                print("O(s) Ponto(s) de Interesse:\nMercado da Lapa\nShopping Center Lapa\nHorário de funcionamento:\nTodos os dias, das 4:40 à meia-noite.")
                
            elif ponto_interesse ==  "20":
                limpar_tela()
                print("O(s) Ponto(s) de Interesse:\nMemorial da América Latina\nAllianz Parque\nParque da Água Branca\nHorário de funcionamento:\nTodos os dias, das 4:40 à meia-noite.")
                
            else :
                limpar_tela()
                print("O(s) Ponto(s) de Interesse:\nSala São Paulo\nPinacoteca de São Paulo\nEstação Júlio Prestes\nHorário de funcionamento:\nTodos os dias, das 4:40 à meia-noite.")
            
        else: 
            limpar_tela()
            print("obrigado por utilizar!")
            input("Pressione Enter para retornar ao menu.")
            menu_principal()
        
    else:
        limpar_tela()
        print("Linha Esmeralda no SENTIDO Mendes-Vila Natal:\n")
        print("Osasco --> Presidente Altino --> Ceasa --> Vila Lobos-Jaguaré --> Cidade Universitária --> Pinheiros --> Hebraica-Rebouças --> Cidade Jardim --> Vila Olímpia --> Berrini --> Morumbi --> Granja Julieta --> João Dias --> Santo Amaro --> Socorro --> Jurubatuba --> Autódromo --> Primavera-Interlagos --> Grajaú --> Mendes-Vila Natal.")
        print("================================")
        
        print("Linha Esmeralda no SENTIDO Osasco:\n ")
        
        print("Mendes-Vila Natal --> Grajaú --> Primavera-Interlagos --> Autódromo --> Jurubatuba --> Socorro --> Santo Amaro --> João Dias --> Granja Julieta --> Morumbi --> Berrini --> Vila Olímpia --> Cidade Jardim --> Hebraica-Rebouças --> Pinheiros --> Cidade Universitária --> Vila Lobos-Jaguaré --> Ceasa --> Presidente Altino --> Osasco.\n ")
        
        ponto_interesse=input("Gostaria de saber os Pontos de interesse ? (S/N) ").lower()
        limpar_tela()
        
        if ponto_interesse == "s":
            ponto_interesse = input("1.Osasco\n2.Presidente Altino\n3.Ceasa\n4.Vila Lobos-Jaguaré\n5.Cidade Universitária\n6.Pinheiros\n7.Hebraica-Rebouças\n8.Cidade Jardim\n9.Vila Olímpia\n10.Berrini\n11.Morumbi\n12.Granja Julieta\n13.João Dias\n14.Santo Amaro\n15.Socorro\n16.Jurubatuba\n17.Autódromo\n18.Primavera-Interlagos\n19.Grajaú\n20.Mendes-Vila Natal\nQual das estações você gostaria de saber ? (inserir o número) ")
        
            if ponto_interesse == "1":
                limpar_tela()
                print("O(s) Ponto(s) de Interesse:\nShopping Osasco Plaza\nCalçadão de Osasco\nParque Ecológico Dionísio Alvarez Mateos\nHorário de funcionamento:\nTodos os dias, das 4:40 à meia-noite.")
            
            elif ponto_interesse ==  "2":
                limpar_tela()
                print("O(s) Ponto(s) de Interesse:\nComplexo Presidente Altino (CPTM)\nHorário de funcionamento:\nTodos os dias, das 4:40 à meia-noite.")
            
            elif ponto_interesse ==  "3":
                limpar_tela()
                print("O(s) Ponto(s) de Interesse:\n CEAGESP (Companhia de Entrepostos e Armazéns Gerais de São Paulo)\nMercado de Flores\nHorário de funcionamento:\nTodos os dias, das 4:40 à meia-noite.")
            
            elif ponto_interesse ==  "4":
                limpar_tela()
                print("O(s) Ponto(s) de Interesse:\nParque Villa-Lobos\nShopping Villa-Lobos\nHorário de funcionamento:\nTodos os dias, das 4:40 à meia-noite.")
            
            elif ponto_interesse ==  "5":
                limpar_tela()
                print("O(s) Ponto(s) de Interesse:\nUniversidade de São Paulo (USP)\nMuseu de Zoologia da USP\nInstituto Butantan\nHorário de funcionamento:\nTodos os dias, das 4:40 à meia-noite.")
            
            elif ponto_interesse ==  "6":
                limpar_tela()
                print("O(s) Ponto(s) de Interesse:\nLargo da Batata\nInstituto Tomie Ohtake\nHorário de funcionamento:\nTodos os dias, das 4:40 à meia-noite.")
            
            elif ponto_interesse ==  "7":
                limpar_tela()
                print("O(s) Ponto(s) de Interesse:\nClube Hebraica\nShopping Eldorado\nMuseu da Casa Brasileira\nHorário de funcionamento:\nTodos os dias, das 4:40 à meia-noite.")
            
            elif ponto_interesse ==  "8":
                limpar_tela()
                print("O(s) Ponto(s) de Interesse:\nShopping Cidade Jardim\nHorário de funcionamento:\nTodos os dias, das 4:40 à meia-noite.")
            
            elif ponto_interesse ==  "9":
                limpar_tela()
                print("O(s) Ponto(s) de Interesse:\nShopping Vila Olímpia\nParque do Povo\nHorário de funcionamento:\nTodos os dias, das 4:40 à meia-noite.")
            
            elif ponto_interesse ==  "10":
                limpar_tela()
                print("O(s) Ponto(s) de Interesse:\nAvenida Engenheiro Luís Carlos Berrini (centro financeiro)\nShopping Nações Unidas\nHorário de funcionamento:\nTodos os dias, das 4:40 à meia-noite.")
            
            elif ponto_interesse ==  "11":
                limpar_tela()
                print("O(s) Ponto(s) de Interesse:\nShopping Morumbi\nMarket Place Shopping Center\nHorário de funcionamento:\nTodos os dias, das 4:40 à meia-noite.")
            
            elif ponto_interesse ==  "12":
                limpar_tela()
                print("O(s) Ponto(s) de Interesse:\nParque Severo Gomes\nHorário de funcionamento:\nTodos os dias, das 4:40 à meia-noite.")
            
            elif ponto_interesse ==  "13":
                limpar_tela()
                print("O(s) Ponto(s) de Interesse:\nCentro Empresarial de São Paulo\nParque Burle Marx\nHorário de funcionamento:\nTodos os dias, das 4:40 à meia-noite.")
            
            elif ponto_interesse ==  "14":
                limpar_tela()
                print("O(s) Ponto(s) de Interesse:\n Largo Treze\nPraça Floriano Peixoto\nCentro Cultural Santo Amaro\nHorário de funcionamento:\nTodos os dias, das 4:40 à meia-noite.")
            
            elif ponto_interesse ==  "15":
                limpar_tela()
                print("O(s) Ponto(s) de Interesse:\nParque da Represa de Guarapiranga\nHorário de funcionamento:\nTodos os dias, das 4:40 à meia-noite.")
            
            elif ponto_interesse ==  "16":
                limpar_tela()
                print("O(s) Ponto(s) de Interesse:\nShopping SP Market\nHorário de funcionamento:\nTodos os dias, das 4:40 à meia-noite.")
            
            elif ponto_interesse ==  "17":
                limpar_tela()
                print("O(s) Ponto(s) de Interesse:\nAutódromo de Interlagos\nParque Interlagos\nHorário de funcionamento:\nTodos os dias, das 4:40 à meia-noite.")
            
            elif ponto_interesse ==  "18":
                limpar_tela()
                print("O(s) Ponto(s) de Interesse:\nParque Natural Municipal da Ilha do Bororé\nrepresa Billings\nHorário de funcionamento:\nTodos os dias, das 4:40 à meia-noite.")
            
            elif ponto_interesse ==  "19":
                limpar_tela()
                print("O(s) Ponto(s) de Interesse:\nLargo do Grajaú\nHorário de funcionamento:\nTodos os dias, das 4:40 à meia-noite.")
            
            else: 
                limpar_tela()
                print("O(s) Ponto(s) de Interesse:\nParques e áreas verdes próximas\nHorário de funcionamento:\nTodos os dias, das 4:40 à meia-noite.")
        else: 
            limpar_tela()
            print("obrigado por utilizar!")
            input("Pressione Enter para retornar ao menu.")
            menu_principal()    
                                                                                    
                                                                                        
        
        
        input("Pressione Enter para retornar ao menu.")
        menu_principal()
    
    
   
    
menu_principal()



    

    

