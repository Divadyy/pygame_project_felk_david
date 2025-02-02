import pygame
import sys
from data.button import Button
from data.functions2 import *
from config import LEVEL_FILE

pygame.init()

size = width, height = 1280, 720
FPS = 60

tiles_images = TILES_IMAGES
tile_width = TILE_WIDTH
tile_height = TILE_HEIGHT

screen = pygame.display.set_mode(size)
pygame.display.set_caption('Main Menu')

main_background = pygame.image.load('menu_imgs/menu.png')
settings_background = pygame.image.load('menu_imgs/settings.png')
clock = pygame.time.Clock()

cursor = pygame.image.load('menu_imgs/cursor.png').convert_alpha()
pygame.mouse.set_visible(False)


def main_menu():
    pygame.mixer.music.load('sounds/surface.ogg')
    pygame.mixer.music.play(-1)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Main Menu')

    new_game_start_button = Button(width / 2 - (498 / 2), 175, 498, 107,
                                   'Начать новую игру',
                                   'menu_imgs/main_btn.png', 'menu_imgs/main_btn_hvr.png',
                                   'sounds/btn.mp3')
    settings_button = Button(width / 2 - (498 / 2), 325, 498, 107,
                             'Настройки',
                             'menu_imgs/main_btn.png', 'menu_imgs/main_btn_hvr.png',
                             'sounds/btn.mp3')
    exit_button = Button(width / 2 - (498 / 2), 475, 498, 107,
                         'Выйти',
                         'menu_imgs/main_btn.png', 'menu_imgs/main_btn_hvr.png',
                         'sounds/btn.mp3')

    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(main_background, (0, 0))

        font = pygame.font.Font(None, 72)
        text_surface = font.render('Shattered Dungeon', True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(width / 2, 75))
        screen.blit(text_surface, text_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.USEREVENT and event.button == new_game_start_button:
                fade()
                running = False
                new_game()

            if event.type == pygame.USEREVENT and event.button == settings_button:
                fade()
                settings_menu()

            if event.type == pygame.USEREVENT and event.button == exit_button:
                running = False
                pygame.quit()
                sys.exit()

            for btn in [new_game_start_button, settings_button, exit_button]:
                btn.handle_event(event)

        for btn in [new_game_start_button, settings_button, exit_button]:
            btn.check_hover(pygame.mouse.get_pos())
            btn.draw(screen)
        if pygame.mouse.get_focused():
            x, y = pygame.mouse.get_pos()
            screen.blit(cursor, (x - 4, y))

        pygame.display.flip()


def save_settings(tiles_images, tile_width, tile_height):
    return tiles_images, tile_width, tile_height


def new_game():
    game_cycle(LEVEL_FILE[0], tiles_images, tile_width, tile_height)


def settings_menu():
    audio_button = Button(width / 2 - (498 / 2), 125, 498, 107,
                          'Настройки аудио',
                          'menu_imgs/main_btn.png', 'menu_imgs/main_btn_hvr.png',
                          'sounds/btn.mp3')
    video_button = Button(width / 2 - (498 / 2), 250, 498, 107,
                          'Настройки видео',
                          'menu_imgs/main_btn.png', 'menu_imgs/main_btn_hvr.png',
                          'sounds/btn.mp3')
    back_button = Button(width / 2 - (498 / 2), 375, 498, 107,
                         'Назад',
                         'menu_imgs/main_btn.png', 'menu_imgs/main_btn_hvr.png',
                         'sounds/btn.mp3')

    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(settings_background, (0, 0))

        font = pygame.font.Font(None, 72)
        text_surface = font.render('Настройки', True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(width / 2, 75))
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

            if event.type == pygame.USEREVENT and event.button == audio_button:
                fade()
                audio_settings()

            if event.type == pygame.USEREVENT and event.button == video_button:
                fade()
                video_settings()

            for btn in [audio_button, video_button, back_button]:
                btn.handle_event(event)

        for btn in [audio_button, video_button, back_button]:
            btn.check_hover(pygame.mouse.get_pos())
            btn.draw(screen)

        x, y = pygame.mouse.get_pos()
        screen.blit(cursor, (x, y))

        pygame.display.flip()


def audio_settings():
    percent_10_button = Button(width / 2 - (498 / 2), 6, 498, 107,
                               '10%',
                               'menu_imgs/main_btn.png', 'menu_imgs/main_btn_hvr.png',
                               'sounds/btn.mp3')
    percent_25_button = Button(width / 2 - (498 / 2), 126, 498, 107,
                               '25%',
                               'menu_imgs/main_btn.png', 'menu_imgs/main_btn_hvr.png',
                               'sounds/btn.mp3')
    percent_50_button = Button(width / 2 - (498 / 2), 246, 498, 107,
                               '50%',
                               'menu_imgs/main_btn.png', 'menu_imgs/main_btn_hvr.png',
                               'sounds/btn.mp3')
    percent_75_button = Button(width / 2 - (498 / 2), 366, 498, 107,
                               '75%',
                               'menu_imgs/main_btn.png', 'menu_imgs/main_btn_hvr.png',
                               'sounds/btn.mp3')
    percent_100_button = Button(width / 2 - (498 / 2), 486, 498, 107,
                                '100% (по умолчанию)',
                                'menu_imgs/main_btn.png', 'menu_imgs/main_btn_hvr.png',
                                'sounds/btn.mp3')
    back_button = Button(width / 2 - (498 / 2), 606, 498, 107,
                         'Назад',
                         'menu_imgs/main_btn.png', 'menu_imgs/main_btn_hvr.png',
                         'sounds/btn.mp3')
    music_off_button = Button(width - 200, 606, 100, 100,
                              '',
                              'menu_imgs/music_off.png', 'menu_imgs/music_off_hvr.png',
                              'sounds/btn.mp3')

    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(settings_background, (0, 0))

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

            if event.type == pygame.USEREVENT and event.button == percent_10_button:
                VOLUME = 0.1
                pygame.mixer.music.set_volume(VOLUME)

            if event.type == pygame.USEREVENT and event.button == percent_25_button:
                VOLUME = 0.25
                pygame.mixer.music.set_volume(VOLUME)

            if event.type == pygame.USEREVENT and event.button == percent_50_button:
                VOLUME = 0.5
                pygame.mixer.music.set_volume(VOLUME)

            if event.type == pygame.USEREVENT and event.button == percent_75_button:
                VOLUME = 0.75
                pygame.mixer.music.set_volume(VOLUME)

            if event.type == pygame.USEREVENT and event.button == percent_100_button:
                VOLUME = 1
                pygame.mixer.music.set_volume(VOLUME)

            if event.type == pygame.USEREVENT and event.button == music_off_button:
                VOLUME = 0
                pygame.mixer.music.set_volume(VOLUME)

            for btn in [percent_10_button, percent_25_button, percent_50_button,
                        percent_75_button, percent_100_button, back_button, music_off_button]:
                btn.handle_event(event)

        for btn in [percent_10_button, percent_25_button, percent_50_button,
                    percent_75_button, percent_100_button, back_button, music_off_button]:
            btn.check_hover(pygame.mouse.get_pos())
            btn.draw(screen)

        x, y = pygame.mouse.get_pos()
        screen.blit(cursor, (x, y))

        pygame.display.flip()


def video_settings():
    textures16x16 = Button(width / 2 - (498 / 2), 100, 498, 107,
                           'Текстуры 16x16',
                           'menu_imgs/main_btn.png', 'menu_imgs/main_btn_hvr.png',
                           'sounds/btn.mp3')
    textures32x32 = Button(width / 2 - (498 / 2), 225, 498, 107,
                           'Текстуры 32x32',
                           'menu_imgs/main_btn.png', 'menu_imgs/main_btn_hvr.png',
                           'sounds/btn.mp3')
    textures64x64 = Button(width / 2 - (498 / 2), 350, 498, 107,
                           'Текстуры 64x64 (по умолчанию)',
                           'menu_imgs/main_btn.png', 'menu_imgs/main_btn_hvr.png',
                           'sounds/btn.mp3')
    back_button = Button(width / 2 - (498 / 2), 475, 498, 107,
                         'Назад',
                         'menu_imgs/main_btn.png', 'menu_imgs/main_btn_hvr.png',
                         'sounds/btn.mp3')

    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(settings_background, (0, 0))

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

            if event.type == pygame.USEREVENT and event.button == textures16x16:
                global tiles_images
                global tile_width
                global tile_height
                tiles_images = {'w': pygame.image.load('textures/wall16x16.png'),
                                'f': pygame.image.load('textures/floor16x16.png'),
                                'g': pygame.image.load('textures/entrance16x16.png'),
                                'x': pygame.image.load('textures/exit16x16.png'),
                                'p': pygame.image.load('textures/player16x16.png'),
                                'h': pygame.image.load('textures/health16x16.png'),
                                's': pygame.image.load('textures/attack16x16.png'),
                                'a': pygame.image.load('textures/defense16x16.png'),
                                'e': pygame.image.load('textures/skeleton16x16.png')}
                tile_width = 16
                tile_height = 16
            if event.type == pygame.USEREVENT and event.button == textures32x32:
                tiles_images = {'w': pygame.image.load('textures/wall32x32.png'),
                                'f': pygame.image.load('textures/floor32x32.png'),
                                'g': pygame.image.load('textures/entrance32x32.png'),
                                'x': pygame.image.load('textures/exit32x32.png'),
                                'p': pygame.image.load('textures/player32x32.png'),
                                'h': pygame.image.load('textures/health32x32.png'),
                                's': pygame.image.load('textures/attack32x32.png'),
                                'a': pygame.image.load('textures/defense32x32.png'),
                                'e': pygame.image.load('textures/skeleton32x32.png')}
                tile_width = 32
                tile_height = 32

            if event.type == pygame.USEREVENT and event.button == textures64x64:
                tiles_images = {'w': pygame.image.load('textures/wall64x64.png'),
                                'f': pygame.image.load('textures/floor64x64.png'),
                                'g': pygame.image.load('textures/entrance64x64.png'),
                                'x': pygame.image.load('textures/exit64x64.png'),
                                'p': pygame.image.load('textures/player64x64.png'),
                                'h': pygame.image.load('textures/health64x64.png'),
                                's': pygame.image.load('textures/attack64x64.png'),
                                'a': pygame.image.load('textures/defense64x64.png'),
                                'e': pygame.image.load('textures/skeleton64x64.png')}
                tile_width = 64
                tile_height = 643

            for btn in [textures16x16, textures32x32, textures64x64, back_button]:
                btn.handle_event(event)

        for btn in [textures16x16, textures32x32, textures64x64, back_button]:
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

        fade_surface = pygame.Surface(size)
        fade_surface.fill((0, 0, 0))
        fade_surface.set_alpha(fade_alpha)
        screen.blit(fade_surface, (0, 0))

        fade_alpha += 5
        if fade_alpha >= 105:
            fade_alpha = 255
            running = False

        pygame.display.flip()
        clock.tick(FPS)
