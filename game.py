import pygame
import random
import sys

# Inicializa o pygame
pygame.init()

# Configurações da tela
LARGURA, ALTURA = 800, 600
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Circulo Game - Círculos Explosivos")

#cores
PRETO = (0,0,0)
VERMELHO = (255,0,0)
BRANCO = (255,255,255)

fonte = pygame.font.SysFont("Arial",36)

raio = 30

circulos = []
for _ in range(5):
     x = random.randint(raio, LARGURA - raio)
     y = random.randint(raio, ALTURA - raio)
     dx = random.choice([-3,3])
     dy = random.choice([-3,3])
     circulos.append([x,y,dx,dy])
     
     
pontos = 0

clock = pygame.time.Clock()
rodando = True
while rodando:
    tela.fill(PRETO)
    
    
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button ==1:
            mx , my = pygame.mouse.get_pos()
            for c in circulos[:]:
                cx,cy, dx, dy =c
                distancia = ((mx - cx) **2 + (my -cy) **2 ) ** 0.5
                if distancia<= raio:
                     circulos.remove(c)
                     pontos +=5
                    
                    
    for c in circulos[:]:
        c[0] += c[2]
        c[1] += c[3]
        
        if c[0] < -raio or c[0] > LARGURA + raio or c[1] < -raio or c[1] > ALTURA + raio:
            circulos.remove(c)

        else:
            pygame.draw.circle(tela,VERMELHO,(c[0],c[1]),raio)
            
            
    if len(circulos) <5:
        x = random.randint(raio,LARGURA -raio)     
        y = random.randint(raio,ALTURA -raio)    
        dx = random.choice([-3,3])
        dy = random.choice([-3,3])
        circulos.append([x,y,dx,dy])
        
        
    texto = fonte.render(f"Pontos: {pontos}",True,BRANCO)
    tela.blit(texto,(20, 20))
    
    
    
    if pontos >= 30:
       vitoria = fonte.render("Você venceu",True,BRANCO)
       tela.blit(vitoria,(LARGURA//2 - 120, ALTURA//2))
       pygame.display.flip()
       pygame.time.delay(3000)
       rodando = False

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()