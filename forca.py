def jogar():
  print("***********************************")
  print("*** Bem vindo ao jogo da forca! ***")
  print("***********************************")

  palavra_secreta = "banana"

  enforcou = False
  acertou = False

  # enquanto não enforcou e não acertou
  while not enforcou and not acertou:
    
    chute = input("Qual letra? ").strip()
    
    index = 0
    letra = ""
    for letra in palavra_secreta:
      if chute.upper() == letra.upper():
        print(f"Encontrei a letra {letra} na posição {index}")
      index = index + 1

    print("jogando...")
  print("Fim do jogo")

if __name__ == "__main__":
  jogar()