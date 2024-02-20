crct_1 = input("Digite a primeira caracteristica do animal")
crct_2 = input("Digite a segunda caracteristica do animal")
crct_3 = input("Digite a terceira caracteristica do animal")

if crct_1 == "vertebrado":
    if crct_2 == "ave":
        if crct_3 == "carvivoro":
            print("aguia")
        else:
            print("pomba")
    else:
        if crct_3 == "onvivoro":
            print("homem")
        else:
            print("vaca")
else:
    if crct_2 == "inseto":
        if crct_3 == "hematofago":
            print("pulga")
        else:
            print("largat")
    else:
        if crct_3 == "hematofago":
            print("sanguessuga")
        else:
            print("minhoca")
            


