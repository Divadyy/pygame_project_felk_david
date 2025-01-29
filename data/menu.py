import pygame
import sys
from data.button import Button
from data.functions2 import game_cycle

pygame.init()

SIZE = WIDTH, HEIGHT = 1280, 720
FPS = 60

screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption('Main Menu')
main_background = pygame.image.load('menu_imgs/menu.png')
settings_background = pygame.image.load('menu_imgs/settings.png')
clock = pygame.time.Clock()

cursor = pygame.image.load('menu_imgs/cursor.png').convert_alpha()
pygame.mouse.set_visible(False)


def main_menu():
    game_load_button = Button(WIDTH / 2 - (498 / 2), 125, 498, 107,
                              'Загрузить игру',
                              'menu_imgs/main_btn.png', 'menu_imgs/main_btn_hvr.png',
                              'sounds/btn.mp3')
    new_game_start_button = Button(WIDTH / 2 - (498 / 2), 250, 498, 107,
                                   'Начать новую игру',
                                   'menu_imgs/main_btn.png', 'menu_imgs/main_btn_hvr.png',
                                   'sounds/btn.mp3')
    settings_button = Button(WIDTH / 2 - (498 / 2), 375, 498, 107,
                             'Настройки',
                             'menu_imgs/main_btn.png', 'menu_imgs/main_btn_hvr.png',
                             'sounds/btn.mp3')
    exit_button = Button(WIDTH / 2 - (498 / 2), 500, 498, 107,
                         'Выйти',
                         'menu_imgs/main_btn.png', 'menu_imgs/main_btn_hvr.png',
                         'sounds/btn.mp3')

    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(main_background, (0, 0))

        font = pygame.font.Font(None, 72)
        text_surface = font.render('Shattered Dungeon', True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(WIDTH / 2, 75))
        screen.blit(text_surface, text_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.USEREVENT and event.button == game_load_button:
                fade()
                load_game()

            if event.type == pygame.USEREVENT and event.button == new_game_start_button:
                fade()
                new_game()

            if event.type == pygame.USEREVENT and event.button == settings_button:
                fade()
                settings_menu()

            if event.type == pygame.USEREVENT and event.button == exit_button:
                running = False
                pygame.quit()
                sys.exit()

            for btn in [game_load_button, new_game_start_button, settings_button, exit_button]:
                btn.handle_event(event)

        for btn in [game_load_button, new_game_start_button, settings_button, exit_button]:
            btn.check_hover(pygame.mouse.get_pos())
            btn.draw(screen)
        if pygame.mouse.get_focused():
            x, y = pygame.mouse.get_pos()
            screen.blit(cursor, (x - 4, y))

        pygame.display.flip()


def load_game():
    pass


def new_game():
    pygame.quit()
    game_cycle(0)


def settings_menu():
    audio_button = Button(WIDTH / 2 - (498 / 2), 125, 498, 107,
                          'Настройки аудио',
                          'menu_imgs/main_btn.png', 'menu_imgs/main_btn_hvr.png',
                          'sounds/btn.mp3')
    video_button = Button(WIDTH / 2 - (498 / 2), 250, 498, 107,
                          'Настройки видео',
                          'menu_imgs/main_btn.png', 'menu_imgs/main_btn_hvr.png',
                          'sounds/btn.mp3')
    back_button = Button(WIDTH / 2 - (498 / 2), 375, 498, 107,
                         'Назад',
                         'menu_imgs/main_btn.png', 'menu_imgs/main_btn_hvr.png',
                         'sounds/btn.mp3')

    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(settings_background, (0, 0))

        font = pygame.font.Font(None, 72)
        text_surface = font.render('Настройки', True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(WIDTH / 2, 75))
        screen.blit(text_surface, text_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    fade()
                    running = False

            if event.type == pygame.USEREVENT and event.button == back_button:
                fade()
                running = False

            for btn in [audio_button, video_button, back_button]:
                btn.handle_event(event)

        for btn in [audio_button, video_button, back_button]:
            btn.check_hover(pygame.mouse.get_pos())
            btn.draw(screen)

        x, y = pygame.mouse.get_pos()
        screen.blit(cursor, (x, y))

        pygame.display.flip()


def fade():
    fade_alpha = 0
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        fade_surface = pygame.Surface(SIZE)
        fade_surface.fill((0, 0, 0))
        fade_surface.set_alpha(fade_alpha)
        screen.blit(fade_surface, (0, 0))

        fade_alpha += 5
        if fade_alpha >= 105:
            fade_alpha = 255
            running = False

        pygame.display.flip()
        clock.tick(FPS)
