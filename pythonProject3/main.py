import pygame
import sys
import random

# Inicialização do Pygame
pygame.init()

# Configurações da tela
largura, altura = 800, 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Jogo de Tiro")

# Cores
branco = (255, 255, 255)
vermelho = (255, 0, 0)

# Jogador
jogador_img = __import__("jogador.png")
jogador_rect = jogador_img.get_rect()
jogador_rect.centerx = largura // 2
jogador_rect.bottom = altura - 10
jogador_velocidade = 5

# Inimigo
inimigo_img = __import__("inimigo.png")
inimigo_rect = inimigo_img.get_rect()
inimigo_rect.x = random.randint(0, largura - inimigo_rect.width)
inimigo_rect.y = random.randint(50, 150)
inimigo_velocidade = 2

# Pontuação
pontuacao = 0
fonte = pygame.font.Font(None, 36)

# Loop principal do jogo
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Movimento do jogador
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:
        jogador_rect.x -= jogador_velocidade
    if teclas[pygame.K_RIGHT]:
        jogador_rect.x += jogador_velocidade

    # Atualizações
    inimigo_rect.y += inimigo_velocidade

    # Colisão
    if jogador_rect.colliderect(inimigo_rect):
        inimigo_rect.x = random.randint(0, largura - inimigo_rect.width)
        inimigo_rect.y = random.randint(50, 150)
        pontuacao -= 1

    if inimigo_rect.bottom > altura:
        inimigo_rect.x = random.randint(0, largura - inimigo_rect.width)
        inimigo_rect.y = random.randint(50, 150)
        pontuacao += 1

    # Desenho
    tela.fill(branco)
    tela.blit(jogador_img, jogador_rect)
    tela.blit(inimigo_img, inimigo_rect)

    texto_pontuacao = fonte.render(f"Pontuação: {pontuacao}", True, vermelho)
    tela.blit(texto_pontuacao, (10, 10))

    pygame.display.flip()

    # Limita a taxa de quadros
    pygame.time.delay(30)
