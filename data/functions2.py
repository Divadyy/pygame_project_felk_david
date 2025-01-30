# Импортируем PyGame и все константы
from data.config import *

map_static = [[]]
map_dynamic = [[]]


class Enemy:
    def __init__(self, position, health):
        self.position = position
        self.health = health


class Item:
    def __init__(self, health_gain=0, attack_gain=0, armor_gain=0):
        self.health_gain = health_gain
        self.attack_gain = attack_gain
        self.armor_gain = armor_gain


class Tile:
    def __init__(self, structure, entity, health, item):
        self.structure = structure
        self.entity = entity
        self.health = health
        self.item = item


def load_from_file(file):
    game_map = []
    with open(file, 'r') as f:
        n = 0
        for line in f:
            game_map.append([])
            for symbol in line.strip():
                item = Item()
                if symbol == 'e':
                    symbol = Tile('f', 'e', 2, item)
                    game_map[n].append(symbol)
                elif symbol == 'p':
                    symbol = Tile('f', 'p', 10, item)
                    game_map[n].append(symbol)
                elif symbol == 'w':
                    symbol = Tile('w', '0', 0, item)
                    game_map[n].append(symbol)
                elif symbol == 'd':
                    symbol = Tile('d', '0', 0, item)
                    game_map[n].append(symbol)
                elif symbol == 'v':
                    symbol = Tile('v', '0', 0, item)
                    game_map[n].append(symbol)
                elif symbol == 'h':
                    item.health_gain = 2
                    symbol = Tile('f', 'i', 0, item)
                    game_map[n].append(symbol)
                elif symbol == 's':
                    item.attack_gain = 1
                    symbol = Tile('f', 'i', 0, item)
                    game_map[n].append(symbol)
                elif symbol == 'a':
                    item.armor_gain = 1
                    symbol = Tile('f', 'i', 0, item)
                    game_map[n].append(symbol)
                else:
                    symbol = Tile('f', '0', 0, item)
                    game_map[n].append(symbol)
            n += 1
    return game_map


def render(game_map, ):
    for y in range(len(game_map)):
        for x in range(len(game_map[0])):
            match game_map[y][x].structure:
                case 'w':
                    screen.blit(TILES_IMAGES['w'],
                                (x * TILE_WIDTH, y * TILE_HEIGHT))
                case 'f':
                    screen.blit(TILES_IMAGES['f'],
                                (x * TILE_WIDTH, y * TILE_HEIGHT))
                case 'v':
                    screen.blit(TILES_IMAGES['v'],
                                (x * TILE_WIDTH, y * TILE_HEIGHT))
                case 'd':
                    screen.blit(TILES_IMAGES['d'],
                                (x * TILE_WIDTH, y * TILE_HEIGHT))
            match game_map[y][x].entity:
                case 'e':
                    screen.blit(TILES_IMAGES['e'],
                                (x * TILE_WIDTH, y * TILE_HEIGHT))
                case 'p':
                    screen.blit(TILES_IMAGES['p'],
                                (x * TILE_WIDTH, y * TILE_HEIGHT))
                case 'i':
                    if game_map[y][x].item.attack_gain > 0:
                        screen.blit(TILES_IMAGES['s'],
                                    (x * TILE_WIDTH, y * TILE_HEIGHT))
                    elif game_map[y][x].item.armor_gain > 0:
                        screen.blit(TILES_IMAGES['a'],
                                    (x * TILE_WIDTH, y * TILE_HEIGHT))
                    elif game_map[y][x].item.health_gain > 0:
                        screen.blit(TILES_IMAGES['h'],
                                    (x * TILE_WIDTH, y * TILE_HEIGHT))


def process_enemy_moves(game_map, enemies_pos, player_pos, player_health, player_armor):
    wave_path = [[-1] * len(game_map) for _ in range(len(game_map[0]))]
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
            player_health -= 2 - player_armor
        else:
            if n != 0 and wave_path[n - 1][m] == wave_path[n][m] - 1 and game_map[n - 1][m].entity != 'e':
                game_map[n - 1][m].entity = game_map[n][m].entity
                game_map[n - 1][m].health = game_map[n][m].health
                game_map[n][m].entity = '0'
                game_map[n][m].health = 0
                enemies_pos[i] = (n - 1, m)
                continue
            if n != len(game_map) - 1 and wave_path[n + 1][m] == wave_path[n][m] - 1 and game_map[n + 1][m].entity != 'e':
                game_map[n + 1][m].entity = game_map[n][m].entity
                game_map[n + 1][m].health = game_map[n][m].health
                game_map[n][m].entity = '0'
                game_map[n][m].health = 0
                enemies_pos[i] = (n + 1, m)
                continue
            if m != 0 and wave_path[n][m - 1] == wave_path[n][m] - 1 and game_map[n][m - 1].entity != 'e':
                game_map[n][m - 1].entity = game_map[n][m].entity
                game_map[n][m - 1].health = game_map[n][m].health
                game_map[n][m].entity = '0'
                game_map[n][m].health = 0
                enemies_pos[i] = (n, m - 1)
                continue
            if m != len(game_map[0]) - 1 and wave_path[n][m + 1] == wave_path[n][m] - 1 and game_map[n][m + 1].entity != 'e':
                game_map[n][m + 1].entity = game_map[n][m].entity
                game_map[n][m + 1].health = game_map[n][m].health
                game_map[n][m].entity = '0'
                game_map[n][m].health = 0
                enemies_pos[i] = (n, m + 1)
                continue
    return game_map, enemies_pos, player_health


def game_cycle(file):
    game_map = load_from_file(file)
    player_pos = [0, 0]
    player_health = 8
    player_attack = 1
    player_armor = 0
    enemies_pos = []
    row_num = 0
    for row in game_map:
        column_num = 0
        for tile in row:
            if tile.entity == 'p':
                player_pos[0] = row_num
                player_pos[1] = column_num
            if tile.entity == 'e':
                enemies_pos.append((row_num, column_num))
            column_num += 1
        row_num += 1

    render(game_map)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
            if event.type == pygame.KEYDOWN:
                match event.key:
                    case pygame.K_LEFT:
                        if player_pos[1] != 0 and game_map[player_pos[0]][player_pos[1] - 1].structure != 'w':
                            if game_map[player_pos[0]][player_pos[1] - 1].entity == 'e':
                                game_map[player_pos[0]][player_pos[1] - 1].health -= player_attack
                                if game_map[player_pos[0]][player_pos[1] - 1].health <= 0:
                                    game_map[player_pos[0]][player_pos[1] - 1].entity = '0'
                                    enemies_pos.remove((player_pos[0], player_pos[1] - 1))
                            else:
                                if game_map[player_pos[0]][player_pos[1] - 1].entity == 'i':
                                    player_attack += game_map[player_pos[0]][player_pos[1] - 1].item.attack_gain
                                    player_health += game_map[player_pos[0]][player_pos[1] - 1].item.health_gain
                                    player_armor += game_map[player_pos[0]][player_pos[1] - 1].item.armor_gain
                                game_map[player_pos[0]][player_pos[1]].entity = '0'
                                game_map[player_pos[0]][player_pos[1] - 1].entity = 'p'
                                game_map[player_pos[0]][player_pos[1]].health = 0
                                game_map[player_pos[0]][player_pos[1] - 1].health = player_health
                                player_pos[1] = player_pos[1] - 1

                            game_map, enemies_pos, player_health = process_enemy_moves(game_map, enemies_pos,
                                                                                       player_pos, player_health, player_armor)
                            game_map[player_pos[0]][player_pos[1]].health = player_health
                            render(game_map)
                    case pygame.K_RIGHT:
                        if player_pos[1] != len(game_map[0]) - 1 and game_map[player_pos[0]][player_pos[1] + 1].structure != 'w':
                            if game_map[player_pos[0]][player_pos[1] + 1].entity == 'e':
                                game_map[player_pos[0]][player_pos[1] + 1].health -= player_attack
                                if game_map[player_pos[0]][player_pos[1] + 1].health <= 0:
                                    game_map[player_pos[0]][player_pos[1] + 1].entity = '0'
                                    enemies_pos.remove((player_pos[0], player_pos[1] + 1))
                            else:
                                if game_map[player_pos[0]][player_pos[1] + 1].entity == 'i':
                                    player_attack += game_map[player_pos[0]][player_pos[1] + 1].item.attack_gain
                                    player_health += game_map[player_pos[0]][player_pos[1] + 1].item.health_gain
                                    player_armor += game_map[player_pos[0]][player_pos[1] + 1].item.armor_gain
                                game_map[player_pos[0]][player_pos[1]].entity = '0'
                                game_map[player_pos[0]][player_pos[1] + 1].entity = 'p'
                                game_map[player_pos[0]][player_pos[1]].health = 0
                                game_map[player_pos[0]][player_pos[1] + 1].health = player_health
                                player_pos[1] = player_pos[1] + 1

                            game_map, enemies_pos, player_health = process_enemy_moves(game_map, enemies_pos,
                                                                                       player_pos, player_health, player_armor)
                            game_map[player_pos[0]][player_pos[1]].health = player_health
                            render(game_map)
                    case pygame.K_UP:
                        if player_pos[0] != 0 and game_map[player_pos[0] - 1][player_pos[1]].structure != 'w':
                            if game_map[player_pos[0] - 1][player_pos[1]].entity == 'e':
                                game_map[player_pos[0] - 1][player_pos[1]].health -= player_attack
                                if game_map[player_pos[0] - 1][player_pos[1]].health <= 0:
                                    game_map[player_pos[0] - 1][player_pos[1]].entity = '0'
                                    enemies_pos.remove((player_pos[0] - 1, player_pos[1]))
                            else:
                                if game_map[player_pos[0] - 1][player_pos[1]].entity == 'i':
                                    player_attack += game_map[player_pos[0] - 1][player_pos[1]].item.attack_gain
                                    player_health += game_map[player_pos[0] - 1][player_pos[1]].item.health_gain
                                    player_armor += game_map[player_pos[0] - 1][player_pos[1]].item.armor_gain
                                game_map[player_pos[0]][player_pos[1]].entity = '0'
                                game_map[player_pos[0] - 1][player_pos[1]].entity = 'p'
                                game_map[player_pos[0]][player_pos[1]].health = 0
                                game_map[player_pos[0] - 1][player_pos[1]].health = player_health
                                player_pos[0] = player_pos[0] - 1

                            game_map, enemies_pos, player_health = process_enemy_moves(game_map, enemies_pos,
                                                                                       player_pos, player_health, player_armor)
                            game_map[player_pos[0]][player_pos[1]].health = player_health
                            render(game_map)
                    case pygame.K_DOWN:
                        if player_pos[0] != len(game_map) - 1 and game_map[player_pos[0] + 1][player_pos[1]].structure != 'w':
                            if game_map[player_pos[0] + 1][player_pos[1]].entity == 'e':
                                game_map[player_pos[0] + 1][player_pos[1]].health -= player_attack
                                if game_map[player_pos[0] + 1][player_pos[1]].health <= 0:
                                    game_map[player_pos[0] + 1][player_pos[1]].entity = '0'
                                    enemies_pos.remove((player_pos[0] + 1, player_pos[1]))
                            else:
                                if game_map[player_pos[0] + 1][player_pos[1]].entity == 'i':
                                    player_attack += game_map[player_pos[0] + 1][player_pos[1]].item.attack_gain
                                    player_health += game_map[player_pos[0] + 1][player_pos[1]].item.health_gain
                                    player_armor += game_map[player_pos[0] + 1][player_pos[1]].item.armor_gain
                                game_map[player_pos[0]][player_pos[1]].entity = '0'
                                game_map[player_pos[0] + 1][player_pos[1]].entity = 'p'
                                game_map[player_pos[0]][player_pos[1]].health = 0
                                game_map[player_pos[0] + 1][player_pos[1]].health = player_health
                                player_pos[0] = player_pos[0] + 1

                            game_map, enemies_pos, player_health = process_enemy_moves(game_map, enemies_pos,
                                                                                       player_pos, player_health, player_armor)
                            game_map[player_pos[0]][player_pos[1]].health = player_health
                            render(game_map)

        pygame.display.flip()


if __name__ == '__main__':
    game_cycle(LEVEL_FILE)
