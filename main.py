print(50*"-")
print("\tBOT DE MENSAGENS PARA OMLEGLE E BUZZR")
print(50*"-")

try:
    c = int(input("1-Omegle\n2-Buzzr\n3-Todos\nResposta:"))
    if(c == 1):
        from sites.Omegle import Omegle
    elif(c == 2):
        from sites.Buzzr import Buzzr
    elif(c == 3):
        from sites.Omegle import Omegle
        from sites.Buzzr import Buzzr
    else:
        print("OPÇÃO INCORRETA")
except:
    print("O valor digitado nao esta correto")