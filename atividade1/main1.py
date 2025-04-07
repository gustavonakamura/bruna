import cv2
import numpy as np
import os

def transformar_para_cinza(imagem_path, imagem_saida, mostrar_imagens=True):
    if not os.path.isfile(imagem_path):
        print(f"Erro: A imagem '{imagem_path}' não foi encontrada.")
        return False
    
    imagem = cv2.imread(imagem_path)
    
    if imagem is None:
        print(f"Erro: Não foi possível carregar a imagem '{imagem_path}'.")
        return False
    
    imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    
    cv2.imwrite(imagem_saida, imagem_cinza)
    print(f"Imagem em tons de cinza salva em: {imagem_saida}")
    
    if mostrar_imagens:
        cv2.imshow('Original', imagem)
        cv2.imshow('Transformada', imagem_cinza)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    
    return True

def main():
    imagem_entrada = 'montanha.jpeg'
    imagem_saida = 'imagem_transformada.jpg'
    
    transformar_para_cinza(imagem_entrada, imagem_saida)

if __name__ == "__main__":
    main()