import cv2
import numpy as np
import matplotlib.pyplot as plt

def aplicar_tonalidade(img, tonalidade):
    h, w, c = img.shape
    img = img / 255.0 
    resultado = np.zeros_like(img)
    
    for i in range(h):
        for j in range(w):
            r, g, b = img[i, j]
            soma = r + g + b
            if tonalidade == 'vermelho':
                x1, x2, x3 = soma * 0.8, soma * 0.2, soma * 0.1
            elif tonalidade == 'verde':
                x1, x2, x3 = soma * 0.2, soma * 0.8, soma * 0.2
            elif tonalidade == 'azul':
                x1, x2, x3 = soma * 0.1, soma * 0.2, soma * 0.8
            elif tonalidade == 'amarelo':
                x1, x2, x3 = soma * 0.9, soma * 0.9, soma * 0.1
            elif tonalidade == 'laranja':
                x1, x2, x3 = soma * 0.9, soma * 0.6, soma * 0.2
            else:
                x1, x2, x3 = r, g, b 
            
            resultado[i, j] = [x1, x2, x3]
    
    return np.clip(resultado, 0, 1)  

tonalidades = ['vermelho', 'verde', 'azul', 'amarelo', 'laranja']
img_path = 'montanha.jpeg'  
img = cv2.imread(img_path)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

print("Escolha uma tonalidade: ")
print("1 - Vermelho\n2 - Verde\n3 - Azul\n4 - Amarelo\n5 - Laranja")
opcao = int(input("Digite o número correspondente: "))

tonalidade_escolhida = tonalidades[opcao - 1]
img_transformada = aplicar_tonalidade(img, tonalidade_escolhida)

fig, axs = plt.subplots(1, 2, figsize=(10, 5))
axs[0].imshow(img)
axs[0].set_title("Imagem Original")
axs[0].axis("off")

axs[1].imshow(img_transformada)
axs[1].set_title(f"Imagem - {tonalidade_escolhida.capitalize()}")
axs[1].axis("off")

plt.show()

cv2.imwrite(f"imagem_{tonalidade_escolhida}.jpg", (img_transformada * 255).astype(np.uint8))