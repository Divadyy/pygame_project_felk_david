# Импортируем PyGame и все константы
import sys

import pygame

from data.config import *
from button import Button
from data.menu import *
from classes import *

map_static = [[]]
map_dynamic = [[]]


def load_from_file(file):
    game_map = []
    player_pos = [0, 0]
    enemies_pos = []
    with open(file, 'r') as f:
        n = 0
        for line in f:
            game_map.append([])
            m = 0
            for symbol in line.strip():
                character = Character()
                item = Item()
                if symbol == 'e':
                    character.empty = False
                    character.attack = 2
                    character.health = 4
                    character.variation = 1
                    symbol = Tile('f', character, item)
                    enemies_pos.append((n, m))
                    game_map[n].append(symbol)
                elif symbol == 'p':
                    character.empty = False
                    character.attack = 2
                    character.health = 10
                    character.variation = 0
                    symbol = Tile('p', character, item)
                    game_map[n].append(symbol)
                    player_pos[0] = n
                    player_pos[1] = m
                elif symbol == 'w':
                    symbol = Tile('w', character, item)
                    game_map[n].append(symbol)
                elif symbol == 'd':
                    symbol = Tile('d', character, item)
                    game_map[n].append(symbol)
                elif symbol == 'v':
                    symbol = Tile('v', character, item)
                    game_map[n].append(symbol)
                elif symbol == 'h':
                    item.empty = False
                    item.health_gain = 2
                    symbol = Tile('f', character, item)
                    game_map[n].append(symbol)
                elif symbol == 's':
                    item.empty = False
                    item.attack_gain = 1
                    symbol = Tile('f', character, item)
                    game_map[n].append(symbol)
                elif symbol == 'a':
                    item.empty = False
                    item.armor_gain = 1
                    symbol = Tile('f', character, item)
                    game_map[n].append(symbol)
                elif symbol == 'x':
                    symbol = Tile('x', character, item)
                    game_map[n].append(symbol)
                else:
                    symbol = Tile('f', character, item)
                    game_map[n].append(symbol)
                m += 1
            n += 1
    del LEVEL_FILE[0]
    return game_map, player_pos, enemies_pos


def render(game_map, Screen, tiles_images, tile_width, tile_height):
    if tile_width == 16:
        font1 = pygame.font.Font(None, 12)
        font2 = pygame.font.Font(None, 15)
    if tile_width == 32:
        font1 = pygame.font.Font(None, 20)
        font2 = pygame.font.Font(None, 25)
    if tile_width == 64:
        font1 = pygame.font.Font(None, 35)
        font2 = pygame.font.Font(None, 45)
    indentation_x = (WIDTH - len(game_map[0]) * tile_width) / 2
    indentation_y = (HEIGHT - len(game_map) * tile_height) / 2
    for y in range(len(game_map)):
        for x in range(len(game_map[0])):
            match game_map[y][x].structure:
                case 'w':
                    Screen.blit(tiles_images['w'],
                                (x * tile_width + indentation_x, y * tile_height + indentation_y))
                case 'f':
                    Screen.blit(tiles_images['f'],
                                (x * tile_width + indentation_x, y * tile_height + indentation_y))
                case 'v':
                    Screen.blit(tiles_images['v'],
                                (x * tile_width + indentation_x, y * tile_height + indentation_y))
                case 'd':
                    Screen.blit(tiles_images['d'],
                                (x * tile_width + indentation_x, y * tile_height + indentation_y))
                case 'x':
                    Screen.blit(tiles_images['x'],
                                (x * tile_width + indentation_x, y * tile_height + indentation_y))
                case 'p':
                    Screen.blit(tiles_images['g'],
                                (x * tile_width + indentation_x, y * tile_height + indentation_y))
            if not game_map[y][x].item.empty:
                if game_map[y][x].item.attack_gain > 0:
                    Screen.blit(tiles_images['s'],
                                (x * tile_width + indentation_x, y * tile_height + indentation_y))
                elif game_map[y][x].item.armor_gain > 0:
                    Screen.blit(tiles_images['a'],
                                (x * tile_width + indentation_x, y * tile_height + indentation_y))
                elif game_map[y][x].item.health_gain > 0:
                    Screen.blit(tiles_images['h'],
                                (x * tile_width + indentation_x, y * tile_height + indentation_y))
            if not game_map[y][x].character.empty:
                match game_map[y][x].character.variation:
                    case 0:
                        Screen.blit(tiles_images['p'],
                                    (x * tile_width + indentation_x, y * tile_height + indentation_y))
                        text_surface = font2.render(str(game_map[y][x].character.health), False, (0, 255, 0))
                        Screen.blit(text_surface, (x * tile_width + indentation_x, y * tile_height + indentation_y))
                    case 1:
                        Screen.blit(tiles_images['e'],
                                    (x * tile_width + indentation_x, y * tile_height + indentation_y))
                        text_surface = font1.render(str(game_map[y][x].character.health), False, (255, 0, 0))
                        Screen.blit(text_surface, (x * tile_width + indentation_x, y * tile_height + indentation_y))


def process_enemy_moves(game_map, enemies_pos, player_pos):
    wave_path = [[-1] * len(game_map[0]) for _ in range(len(game_map))]
    queue = [(player_pos[0], player_pos[1])]
    wave_path[player_pos[0]][player_pos[1]] = 0
    while queue:
        n, m = queue[0]
        del queue[0]
        path = wave_path[n][m]

        if n != 0 and wave_path[n - 1][m] == -1 and game_map[n - 1][m].structure != 'w':
            queue.append((n - 1, m))
            wave_path[n - 1][m] = path + 1

        if n != len(game_map) - 1 and wave_path[n + 1][m] == -1 and game_map[n + 1][m].structure != 'w':
            queue.append((n + 1, m))
            wave_path[n + 1][m] = path + 1

        if m != 0 and wave_path[n][m - 1] == -1 and game_map[n][m - 1].structure != 'w':
            queue.append((n, m - 1))
            wave_path[n][m - 1] = path + 1

        if m != len(game_map[0]) - 1 and wave_path[n][m + 1] == -1 and game_map[n][m + 1].structure != 'w':
            queue.append((n, m + 1))
            wave_path[n][m + 1] = path + 1

    for i in range(0, len(enemies_pos)):
        n, m = enemies_pos[i]
        if wave_path[n][m] == 1:
            player_armor = game_map[player_pos[0]][player_pos[1]].character.armor
            health_delta = game_map[n][m].character.attack - player_armor
            if health_delta > 0:
                sound = pygame.mixer.Sound('sounds/hit.mp3')
                sound.play()
                game_map[player_pos[0]][player_pos[1]].character.health -= health_delta
        else:
            if n != 0 and wave_path[n - 1][m] == wave_path[n][m] - 1 and game_map[n - 1][m].character.empty:
                game_map[n - 1][m].character.empty = False
                game_map[n - 1][m].character.variation = game_map[n][m].character.variation
                game_map[n - 1][m].character.health = game_map[n][m].character.health
                game_map[n - 1][m].character.attack = game_map[n][m].character.health
                game_map[n - 1][m].character.armor = game_map[n][m].character.armor
                game_map[n][m].character.empty = True
                enemies_pos[i] = (n - 1, m)
                continue
            if n != len(game_map) - 1 and wave_path[n + 1][m] == wave_path[n][m] - 1 and game_map[n + 1][m].character.empty:
                game_map[n + 1][m].character.empty = False
                game_map[n + 1][m].character.variation = game_map[n][m].character.variation
                game_map[n + 1][m].character.health = game_map[n][m].character.health
                game_map[n + 1][m].character.attack = game_map[n][m].character.health
                game_map[n + 1][m].character.armor = game_map[n][m].character.armor
                game_map[n][m].character.empty = True
                enemies_pos[i] = (n + 1, m)
                continue
            if m != 0 and wave_path[n][m - 1] == wave_path[n][m] - 1 and game_map[n][m - 1].character.empty:
                game_map[n][m - 1].character.empty = False
                game_map[n][m - 1].character.variation = game_map[n][m].character.variation
                game_map[n][m - 1].character.health = game_map[n][m].character.health
                game_map[n][m - 1].character.attack = game_map[n][m].character.health
                game_map[n][m - 1].character.armor = game_map[n][m].character.armor
                game_map[n][m].character.empty = True
                enemies_pos[i] = (n, m - 1)
                continue
            if m != len(game_map[0]) - 1 and wave_path[n][m + 1] == wave_path[n][m] - 1 and game_map[n][m + 1].character.empty:
                game_map[n][m + 1].character.empty = False
                game_map[n][m + 1].character.variation = game_map[n][m].character.variation
                game_map[n][m + 1].character.health = game_map[n][m].character.health
                game_map[n][m + 1].character.attack = game_map[n][m].character.health
                game_map[n][m + 1].character.armor = game_map[n][m].character.armor
                game_map[n][m].character.empty = True
                enemies_pos[i] = (n, m + 1)
                continue
    return game_map, enemies_pos


def game_cycle(file, tiles_images, tile_width, tile_height):
    pygame.mixer.music.load('sounds/game.ogg')
    pygame.mixer.music.play()
    Screen = pygame.display.set_mode((1920, 1080))
    game_map, player_pos, enemies_pos = load_from_file(file)

    render(game_map, Screen, tiles_images, tile_width, tile_height)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
            if event.type == pygame.KEYDOWN:
                valid_move = False
                dest_y = player_pos[0]
                dest_x = player_pos[1]
                match event.key:
                    case pygame.K_LEFT:
                        if player_pos[1] != 0 and game_map[player_pos[0]][player_pos[1] - 1].structure != 'w':
                            valid_move = True
                            dest_x = player_pos[1] - 1
                    case pygame.K_RIGHT:
                        if player_pos[1] != len(game_map[0]) - 1 and game_map[player_pos[0]][player_pos[1] + 1].structure != 'w':
                            valid_move = True
                            dest_x = player_pos[1] + 1
                    case pygame.K_UP:
                        if player_pos[0] != 0 and game_map[player_pos[0] - 1][player_pos[1]].structure != 'w':
                            valid_move = True
                            dest_y = player_pos[0] - 1
                    case pygame.K_DOWN:
                        if player_pos[0] != len(game_map) - 1 and game_map[player_pos[0] + 1][player_pos[1]].structure != 'w':
                            valid_move = True
                            dest_y = player_pos[0] + 1
                if valid_move:
                    if not game_map[dest_y][dest_x].character.empty:
                        health_delta = game_map[player_pos[0]][player_pos[1]].character.attack - game_map[dest_y][dest_x].character.armor
                        if health_delta > 0:
                            sound = pygame.mixer.Sound('sounds/hit_crush.mp3')
                            sound.play()
                            game_map[dest_y][dest_x].character.health -= health_delta
                        if game_map[dest_y][dest_x].character.health <= 0:
                            sound = pygame.mixer.Sound('sounds/bones.mp3')
                            sound.play()
                            game_map[dest_y][dest_x].character.empty = True
                            enemies_pos.remove((dest_y, dest_x))
                    else:
                        if not game_map[dest_y][dest_x].item.empty:
                            if game_map[dest_y][dest_x].item.attack_gain > 0:
                                sound = pygame.mixer.Sound('sounds/sword.mp3')
                                sound.play()
                                game_map[player_pos[0]][player_pos[1]].character.attack += game_map[dest_y][
                                    dest_x].item.attack_gain
                            elif game_map[dest_y][dest_x].item.armor_gain > 0:
                                sound = pygame.mixer.Sound('sounds/armor.mp3')
                                sound.play()
                                game_map[player_pos[0]][player_pos[1]].character.armor += game_map[dest_y][
                                    dest_x].item.armor_gain
                            elif game_map[dest_y][dest_x].item.health_gain > 0:
                                sound = pygame.mixer.Sound('sounds/drink.mp3')
                                sound.play()
                                game_map[player_pos[0]][player_pos[1]].character.health += game_map[dest_y][
                                    dest_x].item.health_gain
                            game_map[dest_y][dest_x].item.empty = True
                        if game_map[dest_y][dest_x].structure == 'x':
                            sound = pygame.mixer.Sound('sounds/secret.mp3')
                            sound.play()
                            current_health = game_map[player_pos[0]][player_pos[1]].character.health
                            current_armor = game_map[player_pos[0]][player_pos[1]].character.armor
                            current_attack = game_map[player_pos[0]][player_pos[1]].character.attack

                            if LEVEL_FILE:
                                runningg = True
                                while runningg:
                                    Screen.fill((0, 0, 0))
                                    pygame.display.flip()
                                    runningg = False
                                game_map, player_pos, enemies_pos = load_from_file(LEVEL_FILE[0])
                            else:
                                pygame.mixer.music.stop()
                                sound = pygame.mixer.Sound('sounds/game_win.mp3')
                                sound.play()

                                back_to_desktop = Button(WIDTH / 2 - (498 / 2), 900, 498, 107,
                                                         'Выйти из игры',
                                                         'menu_imgs/main_btn.png', 'menu_imgs/main_btn_hvr.png',
                                                         'sounds/btn.mp3')

                                while True:
                                    Screen.fill((0, 0, 0))
                                    Screen.blit(GAME_WIN, (0, 0))

                                    for event in pygame.event.get():
                                        if event.type == pygame.QUIT:
                                            running = False
                                            pygame.quit()
                                            sys.exit()

                                        if event.type == pygame.USEREVENT and event.button == back_to_desktop:
                                            pygame.quit()
                                            sys.exit()

                                        for btn in [back_to_desktop]:
                                            btn.handle_event(event)

                                    for btn in [back_to_desktop]:
                                        btn.check_hover(pygame.mouse.get_pos())
                                        btn.draw(Screen)

                                    if pygame.mouse.get_focused():
                                        x, y = pygame.mouse.get_pos()
                                        Screen.blit(CURSOR, (x - 4, y))

                                    pygame.display.flip()

                            game_map[player_pos[0]][player_pos[1]].character.health = current_health
                            game_map[player_pos[0]][player_pos[1]].character.armor = current_armor
                            game_map[player_pos[0]][player_pos[1]].character.attack = current_attack
                            render(game_map, Screen, tiles_images, tile_width, tile_height)
                            continue
                        else:
                            game_map[dest_y][dest_x].character.empty = False
                            game_map[dest_y][dest_x].character.variation = 0
                            game_map[dest_y][dest_x].character.health = game_map[player_pos[0]][player_pos[1]].character.health
                            game_map[dest_y][dest_x].character.attack = game_map[player_pos[0]][player_pos[1]].character.attack
                            game_map[dest_y][dest_x].character.armor = game_map[player_pos[0]][player_pos[1]].character.armor
                            game_map[player_pos[0]][player_pos[1]].character.empty = True
                            player_pos[0] = dest_y
                            player_pos[1] = dest_x
                    game_map, enemies_pos = process_enemy_moves(game_map, enemies_pos, player_pos)
                    if game_map[player_pos[0]][player_pos[1]].character.health < 1:
                        pygame.mixer.music.stop()
                        sound = pygame.mixer.Sound('sounds/death.mp3')
                        sound.play()

                        back_to_desktop = Button(WIDTH / 2 - (498 / 2), 900, 498, 107,
                                                 'Выйти из игры',
                                                 'menu_imgs/main_btn.png', 'menu_imgs/main_btn_hvr.png',
                                                 'sounds/btn.mp3')

                        while True:
                            Screen.fill((0, 0, 0))
                            Screen.blit(GAME_OVER, (0, 0))

                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    running = False
                                    pygame.quit()
                                    sys.exit()

                                if event.type == pygame.USEREVENT and event.button == back_to_desktop:
                                    pygame.quit()
                                    sys.exit()

                                for btn in [back_to_desktop]:
                                    btn.handle_event(event)

                            for btn in [back_to_desktop]:
                                btn.check_hover(pygame.mouse.get_pos())
                                btn.draw(Screen)

                            if pygame.mouse.get_focused():
                                x, y = pygame.mouse.get_pos()
                                Screen.blit(CURSOR, (x - 4, y))

                            pygame.display.flip()

                    render(game_map, Screen, tiles_images, tile_width, tile_height)

        pygame.display.flip()


if __name__ == '__main__':
    game_cycle(LEVEL_FILE[0])
5