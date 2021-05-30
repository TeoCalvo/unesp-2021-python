# loteria da babilonia com loop
import random # biblioteca que gera valores aleatórios - pseudoaleatórios

print("Seja bem vindo à Loteria da Babilonia!\nAposte em suas chances!")

numero_sorte = random.randint(1,15) # valor aleatório entre 1 e 15
tentativa = 3

while tentativa > 0:
    
    print("Você tem", tentativa, "tentativas!")
    numero_jogador = int(input("Entre com seu número: ")) # É o número que o usuário vai chutar
    
    if numero_jogador == numero_sorte:
        print("Você é um ganhador!!")
        break # Sai do loop forçadamente!!!

    elif numero_jogador > numero_sorte:
        print("Você é um perdedor! Tente um número menor!")

    else:
        print("Você é um perdedor! Tente um número maior!")
        
    tentativa -= 1 # Remove uma tentativa do player
    
else: # isso só acontece quando acabarem as tentativas
    print("Acabaram suas tentativas!!")