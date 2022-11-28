forca = """
_____  
    |  
    |
    -"""

vazio = """


"""
cabeça = """
    0
"""

tronco =  """
    0
    |
"""

braço_esquerdo = """
    0
   /|
"""

braço_direito = """
    0
   /|\\

"""

perna_esquerda = """
    0
   /|\\
   /
"""

perna_direita = """
    0
   /|\\
   / \\
""" 

chances_do_boneco = [
vazio, 
cabeça, 
tronco,
braço_esquerdo,
braço_direito,
perna_esquerda,
perna_direita,
]

palavra =  'banana'.upper()

acertos = 0
erros = 0
letras_acertadas = ''
letras_erradas = ''

while acertos != len(palavra) or erros != 7:
    mensagem = ''
    for letra in palavra:
       if letra in letras_acertadas:
           mensagem += f'{letra}'

       else:
           mensagem += '-'
    print(forca+chances_do_boneco[erros])
    print(mensagem)
    
    letra = input('Digite a letra: ').upper()
    if letra in letras_acertadas+letras_erradas:
        print('você já tentou essa letra')
        continue
    
    if letra in palavra:
        print('voce acertou a letra')
        letras_acertadas += letra
        acertos += palavra.count(letra)
        
    else:
       print('você  errou a letra')
       letras_erradas += letra
       erros += 1 


    

    
       

        
         
