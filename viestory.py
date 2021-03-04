def intro(): 
    print("Voce esta desacordada apos inalar algum gas misterioso, sente o frio daquele ambiente invadir o seu corpo \n\
        voce so consegue lembrar de uma discussao sobre soltar um gas radioatipo em um local proximo de um vilarejo\n\
mas a pergunta é? aonde voce esta? o que aconteceu? o que fazer? \n\
Acorde, moça\n")

     

def personagem():
    personagem = input("Escolha o personagem para a jornada \n\
    Clara é uma adolecente solitaria que nunca teve muitos amigos ou inclusão em um bom grupo social. \n\
    Sara é uma mulher extrovertida que ama fazer novas amizades \n\
    Carla é uma cientista de renome \n")
    while True: 
        if personagem.title() == "Clara" or personagem.title() == "Sara" or personagem.title() == "Carla":
            break
        else:
            personagem = input("Escolha inválida.  \n\
        Clara é uma adolecente solitaria que nunca teve muitos amigos ou inclusão em um bom grupo social. \n\
    Sara é uma mulher extrovertida que ama fazer novas amizades \n\
    Carla é uma cientista de renome \n")
    print(f"Olá, {personagem.title()}! ")
    primeira_escolha()

def primeira_escolha():
    primeira_escolha = int(input("\n\
ir tomar um banho para acordar ou sair do galpão, por favor \n\
 \n\
    \n\
    1. tomar banho \n\
    2. sair do galpão \n"))

    if (primeira_escolha == 1):
        print("a agua tinha muita radiação, voce morreu")
        perdeu()
    else:
        segunda_escolha

    return primeira_escolha


def programa_principal():
    local = input(f"Digite 1 para iniciar  \n")

    if local.title() == 'banheiro' or local.title() == '1': 
        pri_e = primeira_escolha() 
        if pri_e == 1:
            perdeu()
        elif pri_e == 2:
            seg_e = segunda_escolha()

            if seg_e == 1:
                perdeu()
            elif seg_e == 2:
                seg_e = segunda_escolha()

                if ter_e == 1:
                    vence_jogo()
                elif ter_e == 2:
                    terceira_escolha = int(input("\n\ \n"))
    
def segunda_escolha():
    segunda_escolha = int(input("\n\
voce sai do galpão ainda com o corpo mole, seus olhos ardem com a claridade então o que quer fazer? \n\
 \n\
    \n\
    1. invadir uma casa \n\
    2. continuar andando \n"))

    if (segunda_escolha == 2):
        perdeu()
    else:
        terceira_escolha()
      
    return segunda_escolha

def terceira_escolha():
    terceira_escolha = int(input("\n\
voce da a volta na casa, quebra a janela da porta e abre a porta com facilidade, entrando na cozinha voce deve decidir \n\
 \n\
    \n\
    1. pegar água lacrada, vinagre e sal para descontaminação \n\
    2. buscar mantimentos\n"))

    if(terceira_escolha == 1):
        print("voce esta descontaminado")
        return quarta_escolha()
    else:
        print("O dono da casa chega e ve que a casa esta sendo invadida e antes de pergguntar qualquer coisa, saca o revolve e arira")
        perdeu()
      
    return terceira_escolha

def quarta_escolha():
    quarta_escolha = int(input("\n\
Agora que voce fez uma desinfecção simples da radição DO SEU CORPO, voce deseja permanecer na casa ou sair por ai? \n\
 \n\
    \n\
    1. permanecer na casa\n\
    2. sair da casa \n"))

    if (quarta_escolha == 1):
        print("quem diria que o dono desta casa ainda está vivo, ele entra na casa e ve uma invasorá antes mesmo de conversar ele atira em voce")
        perdeu()
    else:
        quinta_escolha()
      
    return quarta_escolha

def quinta_escolha():
    quinta_escolha = int(input("\n\
voce continua andando ate que sente seu corpo pedir um pouco de agua e comida, o que deseja fazer? \n\
 \n\
    \n\
    1. invadir um mercadinho proximo \n\
    2. procurar alguem para pedir ajuda\n"))

    if (quinta_escolha == 1 ):
        print("nossa quanta sorte! a porta ja esta destrancada então voce com facilidade consegue saquear o mercado para satisfazer suas necessidades")
        sexta_escolha()
    else:
        print("os poucos habitantes destes vilarejo estão desconfiados de qualquer rosto estranho depois do ataque, infelizmente a unica ajuda que ele pode lhe dar foi lhe assassinar sem motivo")
        perdeu()

    return quinta_escolha

def sexta_escolha():
    sexta_escolha = int(input("\n\
voce ja esta totalmente satisfeito das suas necessidas quando ouve um barulho de alguem chegando, vejamos é uma criança que pergunta:- quem esta ai?\n\
 \n\
    \n\
    1. tentar uma conversa, para entender o que esta acontecendo \n\
    2. sair na furtiva\n"))

    if (sexta_escolha == 1 ):
        print("a criança lhe explica que o vilarejo aonde voces estão foi algo de um teste de um novo gas radioativo por isto que os moradores estão tão apreensivos a qualquer pessoa nova e que voce deve ir embora")
        setima_escolha()
    else:
        print("voce sai antes que a criança chega mais perto de voce, sem nenhum plano ou entendimento, apos andar algumas quadras é acertedo por algo que não consegue ve a tempo")
        perdeu()

    return sexta_escolha

def setima_escolha():
    setima_escolha = int(input("\n\
voce sai do galpão ainda com o corpo mole, seus olhos ardem com a claridade então o que quer fazer? \n\
 \n\
    \n\
    1. roubar um carro \n\
    2. pedir que a criança deixe mantimentos na rua atras do mercadinho e sair em seguida \n"))

    if (setima_escolha == 1):
        print("roubar o carro parecia uma boa ideia, uma pena que não foi pensado se a gasolina era o suficiente, agora voce esta no meio do nada sem chance de pedir ajuda")
        perdeu()
    else:
        oitava_escolha()
      
    return setima_escolha

def oitava_escolha():
    oitava_escolha = int(input("\n\
quanta sorte voce teve de encontrar esta menina docil, ela realmente deixou tudo que voce precisa para 3 dias inteiros em uma bolsa, mas pra que tanto aonde é a cidade mais proxima? \n\
 \n\
    \n\
    1. seguir a viagem andando \n\
    2. roubar um carro\n"))

    if (oitava_escolha == 2):
        print("quem diria, a gasolina do carro não deu para chegar ate a proxima cidade, mas sem problemas voce tem tudo para continuar a viagem andando")
        vence_jogo()
    else:
        print("parece uma boa ideia sair da vila sem chamar atenção, a viagem é longa mas com a boa administração dos recursos apos 3 dias voce chega na cidade mais proxima")
        vence_jogo()
      
    return oitava_escolha

def vence_jogo():
    print("meus parabens!concluiu o objetivo, apos chegar na cidade proxima voce conseguiu a ajuna necessaria para voltar para casa")
    vence = input("Deseja jogar novamente? Responda sim ou não. \n")
    if vence.title() == "Sim":
        programa_principal()
    else:
        print("Fim de jogo!")
    return vence






def perdeu():
    print("Voce perdeu, moça")
    perdeu = input("Deseja jogar novamente? Responda sim ou não. \n")
    while True:
        if perdeu.title() == "Sim":
            programa_principal()
        else:
            print("Fim de jogo!")
        break
         
def escolha_invalida():
    invalido = input("Escolha invalida. Deseja jogar novamente? sim ou não. \n")
    while True:
        if invalido.title() == "Sim":
            programa_principal()
        else:
            print("Fim de jogo!")
        break
intro()
personagem()