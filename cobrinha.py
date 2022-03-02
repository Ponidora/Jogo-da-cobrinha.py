import pygame
from pygame.draw import rect
from pygame.locals import *
from sys import exit
from random import randint





pygame.init()





def aumenta_cobra(lista_cobra):
    for XeY in lista_cobra:
        pygame.draw.rect(tela, (0, 255, 100), (XeY[0], XeY[1], 20, 20) )
        
def reiniciar_jogo():
    global pontos, comprimento_inicial, x_cobra,y_cobra, lista_cobra,lista_cabeca, y_cobra, x_fruta, y_fruta, morreu
    pontos = 0
    comprimento_inicial = 5
    x_cobra = (largura/2) -10
    y_cobra = (largura/2) -10
    lista_cobra = []
    lista_cabeca = []
    x_fruta = randint(40, 600)
    y_fruta = randint(40, 430)
    morreu = False


#musica_de_fundo = pygame.mixer.music.load('sons/BoxCat Games - Battle (Normal)')
#pygame.mixer.music.play(-1)

#o parametro (-1) faz a musica entrar em loop
#pygame.mixer.music.play(-1)

#barulho_colisao = pygame.mixer.Sound.load('smw_yoshi_spit.wav')

largura = 640
altura = 480
x_cobra = (largura/2) - 20
y_cobra = (largura/2) -20


velocidade = 10
x_controle = velocidade
y_controle = 0

x_fruta = randint(40, 600)
y_fruta = randint(40, 430)

#Fontes do sistema
#1 escolha a fonte
#2 tamanho da fonte
#3 negrito?
#4 italico?
fonte = pygame.font.SysFont('comics san', 40, True, True)


tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Jogo')


relogio = pygame.time.Clock()
pontos = 0
lista_cobra = []
comprimento_inicial = 5
morreu = False



while True:
    tela.fill((255, 255 ,255))
    relogio.tick(30)
    mensagem = '{} Pontos'.format(pontos)
    aumenta_cobra(lista_cobra)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    #movimentação e mapeamento de teclas

   

    if pygame.key.get_pressed()[K_a]:
       if x_controle == velocidade:
           pass
       else:    
            x_controle = -velocidade
            y_controle = 0
        

    if pygame.key.get_pressed()[K_d]:
       if x_controle == -velocidade:
            pass
       else:
           x_controle = velocidade
           y_controle = 0
    if pygame.key.get_pressed()[K_w]:
        if y_controle == velocidade:
            pass
        else:
           x_controle = 0
           y_controle = -velocidade
    if pygame.key.get_pressed()[K_s]:
        if y_controle == -velocidade:
            pass
        else:
           x_controle = 0
           y_controle = velocidade

    x_cobra = x_cobra + x_controle
    y_cobra = y_cobra + y_controle

     
    #1 parametros: nome da variavel de texto
    #2 antliasing(função True ou False)
    #3 cor
    texto_formatado = fonte.render(mensagem, True, (0, 0, 0))


    #ORDEM DOS REQUISITOS 
    #1 TELA LUGAR ONDE QUERO Q APAREÇA
    #2 COR(DENTRO DE TUPLAS)
    #3 POSIÇÃO EIXO X, EIXO Y, LARGURA E ALTURA (DENTRO DE TUPLAS)
    
    cobra = pygame.draw.rect(tela, (0,255,100), (x_cobra, y_cobra, 20, 20))
    fruta = pygame.draw.rect(tela, (208, 200, 100), (x_fruta, y_fruta, 20, 20))

    lista_cabeca =[]
    lista_cabeca.append(x_cobra)
    lista_cabeca.append(y_cobra)
    lista_cobra.append(lista_cabeca)

    if lista_cobra.count(lista_cabeca) > 1:
        fonte2 = pygame.font.SysFont('arial', 25, True, True )
        mensagem = 'Game over! Pressione R para jogar novamente'
        texto_formatado = fonte2.render(mensagem, True, (0, 0, 0))
        ret_texto = texto_formatado.get_rect()
        morreu = True

        while morreu:
            tela.fill((255, 255, 255))

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        reiniciar_jogo()
            
                ret_texto.center = (largura//2, altura//2)
                tela.blit(texto_formatado, ret_texto)
            pygame.display.update()

    if x_cobra > largura:
        x_cobra = 0
    if x_cobra < 0:
        x_cobra = largura
    if y_cobra > altura:
        y_cobra = 0
    if y_cobra < 0:
        y_cobra = altura





    if len(lista_cobra) > comprimento_inicial:
        del lista_cobra[0] 
    



    if cobra.colliderect(fruta):
       x_fruta = randint(20, 600)
       y_fruta = randint(20, 430)
       pontos = pontos + 1
       comprimento_inicial = comprimento_inicial + 1
       #barulho_colisao.play() 

    tela.blit(texto_formatado, (450, 40))
    pygame.display.update()