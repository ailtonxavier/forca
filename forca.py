from random import randrange

def jogar():
  print("###################################")
  print("### Bem vindo ao jogo da forca! ###")
  print("###################################")

  arquivo = open("palavras.txt", "r", encoding="utf-8")
  palavras = []
  
  for linha in arquivo:
    linha = linha.strip()
    palavras.append(linha)

  arquivo.close()

  numero = randrange(0,len(palavras))
  palavra_secreta = palavras[numero].upper()

  print(palavras)

  letras_acertadas = ["_" for letras in palavra_secreta]

  enforcou = False
  acertou = False
  tentativas = 0

  print(letras_acertadas)

  # enquanto não enforcou e não acertou
  while not enforcou and not acertou:
    
    chute = input("Qual letra? ").strip().upper()
    
    if chute in palavra_secreta:
      index = 0
      for letra in palavra_secreta:
        if chute.upper() == letra.upper():
          letras_acertadas[index] = letra
        index += 1
    else:
      tentativas += 1
    enforcou = tentativas == 6
    acertou = "_" not in letras_acertadas
    print(letras_acertadas)
  
  if acertou:
    print("Parabéns você ganhou!")
  else:
    print("Você perdeu =(")

  print("Fim do jogo")

if __name__ == "__main__":
  jogar()