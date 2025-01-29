import sys

from data.config import *
from data.classes import Tile, Player, Camera


def generate_level(level):
    tiles_images = {'wall': pygame.image.load('textures/wall.png'),
                    'floor': pygame.image.load('textures/floor.png'),
                    'void': pygame.image.load('textures/void.png'),
                    'door_closed': pygame.image.load('textures/door_cl.png'),
                    'door_opened': pygame.image.load('textures/door_op.png'),
                    'door_boss': pygame.image.load('textures/door_bs.png'),
                    'entrance': pygame.image.load('textures/entrance.png'),
                    'exit': pygame.image.load('textures/exit.png')}

    player_image = 'textures/player.png'

    for y in range(len(level)):
        for x in range(len(level[y])):
            match level[y][x]:
                case '.': Tile(tiles_images, 'floor', x, y)
                case '#': Tile(tiles_images, 'wall', x, y)
                case '0': Tile(tiles_images, 'void', x, y)
                case '<': Tile(tiles_images, 'door_closed', x, y)
                case '>': Tile(tiles_images, 'door_opened', x, y)
                case '^': Tile(tiles_images, 'door_boss', x, y)
                case 'l': Tile(tiles_images, 'exit', x, y)
                case "@":
                    Tile(tiles_images, 'entrance', x, y)
                    new_player = Player(player_image, player_image, x, y)

    return new_player, x, y


def load_level(filename):
    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]
        print(level_map)
    max_width = max(map(len, level_map))
    return list(map(lambda x: x.ljust(max_width, '.'), level_map))


def game_cycle(difficulty):
    screen = pygame.display.set_mode((1920, 1080))
    player, x, y = generate_level(load_level(LEVELS_LIST[difficulty]))
    camera = Camera()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
            if event.type == pygame.KEYDOWN:
                match event.key:
                    case pygame.K_LEFT:
                        player.rect.x -= STEP
                    case pygame.K_RIGHT:
                        player.rect.x += STEP
                    case pygame.K_UP:
                        player.rect.y -= STEP
                    case pygame.K_DOWN:
                        player.rect.y += STEP
        camera.update(player)
        for sprite in all_sprites:
            camera.apply(sprite)
        screen.fill(pygame.Color(0, 0, 0))
        tiles_group.draw(screen)
        player_group.draw(screen)

        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    game_cycle(0)
