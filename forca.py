def jogar():
  print("###################################")
  print("### Bem vindo ao jogo da forca! ###")
  print("###################################")

  palavra_secreta = "banana"
  letras_acertadas = ["_", "_", "_", "_", "_", "_"]

  print(letras_acertadas)

  enforcou = False
  acertou = False

  # enquanto não enforcou e não acertou
  while not enforcou and not acertou:
    
    chute = input("Qual letra? ").strip()
    
    index = 0
    
    # para letra em palavra_secre: faça!
    for letra in palavra_secreta:
      
      if chute.upper() == letra.upper():
        letras_acertadas[index] = letra
        print(f"Encontrei a letra {letra} na posição {index}")
      
      index = index + 1

    print(letras_acertadas)
  print("Fim do jogo")

if __name__ == "__main__":
  jogar()