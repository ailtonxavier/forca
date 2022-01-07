from random import randrange

def jogar():
  imprime_mensagem_de_abertura()
  palavra_secreta = carregando_palavra_secreta()
  letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
  print(letras_acertadas)

  enforcou = False
  acertou = False
  tentativas = 0

  # enquanto não enforcou e não acertou
  while not enforcou and not acertou:
    
    chute = pede_chute()
    
    if chute in palavra_secreta:
      marca_chute_correto(chute, letras_acertadas, palavra_secreta)
    else:
      tentativas += 1
      desenha_forca(tentativas)
    enforcou = tentativas == 7
    acertou = "_" not in letras_acertadas
    print(letras_acertadas)
  
  if acertou:
    imprime_mensagem_vencedor()
  else:
    imprime_mensagem_perdedor(palavra_secreta.lower())
    

def imprime_mensagem_de_abertura():
  return print("###################################\n### Bem vindo ao jogo da forca! ###\n###################################")

def carregando_palavra_secreta():
  arquivo = open("palavras.txt", "r", encoding="utf-8")
  palavras = []
  
  for linha in arquivo:
    linha = linha.strip()
    palavras.append(linha)

  arquivo.close()

  numero = randrange(0,len(palavras))
  palavra_secreta = palavras[numero].upper()
  return palavra_secreta

def inicializa_letras_acertadas(palavra):
  return ["_" for letras in palavra]

def pede_chute():
  return input("Qual letra? ").strip().upper()

def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
  index = 0
  for letra in palavra_secreta:
    if chute.upper() == letra.upper():
      letras_acertadas[index] = letra
    index += 1

def desenha_forca(tentativas):
  print("  _______     ")
  print(" |/      |    ")

  if(tentativas == 1):
    print(" |      (_)   ")
    print(" |            ")
    print(" |            ")
    print(" |            ")

  if(tentativas == 2):
    print(" |      (_)   ")
    print(" |      \     ")
    print(" |            ")
    print(" |            ")

  if(tentativas == 3):
    print(" |      (_)   ")
    print(" |      \|    ")
    print(" |            ")
    print(" |            ")

  if(tentativas == 4):
    print(" |      (_)   ")
    print(" |      \|/   ")
    print(" |            ")
    print(" |            ")

  if(tentativas == 5):
    print(" |      (_)   ")
    print(" |      \|/   ")
    print(" |       |    ")
    print(" |            ")

  if(tentativas == 6):
    print(" |      (_)   ")
    print(" |      \|/   ")
    print(" |       |    ")
    print(" |      /     ")

  if (tentativas == 7):
    print(" |      (_)   ")
    print(" |      \|/   ")
    print(" |       |    ")
    print(" |      / \   ")

  print(" |            ")
  print("_|___         ")

def imprime_mensagem_vencedor():
  print("\nParabéns, você ganhou!")
  print("       ___________      ")
  print("      '._==_==_=_.'     ")
  print("      .-\\:      /-.    ")
  print("     | (|:.     |) |    ")
  print("      '-|:.     |-'     ")
  print("        \\::.    /      ")
  print("         '::. .'        ")
  print("           ) (          ")
  print("         _.' '._        ")
  print("        '-------'       ")

def imprime_mensagem_perdedor(palavra_secreta):
  print("\n███████████████████████████")
  print("███████▀▀▀░░░░░░░▀▀▀███████")
  print("████▀░░░░░░░░░░░░░░░░░▀████")
  print("███│░░░░░░░░░░░░░░░░░░░│███")
  print("██▌│░░░░░░░░░░░░░░░░░░░│▐██")
  print("██░└┐░░░░░░░░░░░░░░░░░┌┘░██")
  print("██░░└┐░░░░░░░░░░░░░░░┌┘░░██")
  print("██░░┌┘▄▄▄▄▄░░░░░▄▄▄▄▄└┐░░██")
  print("██▌░│██████▌░░░▐██████│░▐██")
  print("███░│▐███▀▀░░▄░░▀▀███▌│░███")
  print("██▀─┘░░░░░░░▐█▌░░░░░░░└─▀██")
  print("██▄░░░▄▄▄▓░░▀█▀░░▓▄▄▄░░░▄██")
  print("████▄─┘██▌░░░░░░░▐██└─▄████")
  print("█████░░▐█─┬┬┬┬┬┬┬─█▌░░█████")
  print("████▌░░░▀┬┼┼┼┼┼┼┼┬▀░░░▐████")
  print("█████▄░░░└┴┴┴┴┴┴┴┘░░░▄█████")
  print("███████▄░░░░░░░░░░░▄███████")
  print("██████████▄▄▄▄▄▄▄██████████")
  print("███████████████████████████")
  print(f"Você foi inforcado, a palavra secreta era {palavra_secreta}.")

if (__name__ == "__main__"):
  jogar()