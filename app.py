import colorama
situacoes = ["Muito baixo (crítico)","Baixo","Médio","Alto","Muito alto (alerta)"]
def mensagem_situacao(indice):
    if indice == 0:
        print(colorama.Fore.RED + situacoes[0])
    elif indice == 1:
        print(colorama.Fore.YELLOW + situacoes[1])
    elif indice == 2:
        print(colorama.Fore.GREEN + situacoes[2])
    elif indice == 3:
        print(colorama.Fore.CYAN + situacoes[3])
    elif indice == 4:
        print(colorama.Fore.BLUE + situacoes[4])
    else:
        print("Índice não reconhecido")
mensagem_situacao(4)    
print(colorama.Style.RESET_ALL)