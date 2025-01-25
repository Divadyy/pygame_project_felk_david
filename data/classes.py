from data.config import *


tiles_images = {'wall': pygame.image.load('textures/wall.png'),
                'floor': pygame.image.load('textures/floor.png'),
                'void': pygame.image.load('textures/void.png'),
                'door_closed': pygame.image.load('textures/door_cl.png'),
                'door_opened': pygame.image.load('textures/door_op.png'),
                'door_boss': pygame.image.load('textures/door_bs.png'),
                'entrance': pygame.image.load('textures/entrance.png'),
                'exit': pygame.image.load('textures/exit.png')}


class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self, sheet, columns, rows, x, y):
        super().__init__(all_sprites)
        self.frames = []
        self.cut_sheet(sheet, columns, rows)
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        self.rect = self.rect.move(x, y)

    def cut_sheet(self, sheet, columns, rows):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns,
                                sheet.get_height() // rows)
        for i in range(rows):
            for j in range(columns):
                frame_location = (self.rect.w * j, self.rect.h * i)
                self.frames.append(sheet.subsurface(pygame.Rect(frame_location,
                                                                self.rect.size)))

    def update(self):
        self.cur_frame = (self.cur_frame + 1) % len(self.frames)
        self.image = self.frames[self.cur_frame]


class Player(pygame.sprite.Sprite):
    def __init__(self, plr_img, att_plr_img, pos_x, pos_y):
        super().__init__(player_group, all_sprites)
        self.image = pygame.image.load(plr_img)
        self.image_attack = pygame.image.load(att_plr_img)
        self.rect = self.image.get_rect().move(TILE_WIDTH * pos_x, TILE_HEIGHT * pos_y)


class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_images, tile_type, pos_x, pos_y):
        super().__init__(tiles_group, all_sprites)
        self.image = tile_images[tile_type]
        self.rect = self.image.get_rect().move(TILE_WIDTH * pos_x, TILE_HEIGHT * pos_y)


class Camera:
    def __init__(self):
        self.x = 0
        self.y = 0

    def apply(self, obj):
        obj.rect.x += self.x
        obj.rect.y += self.y

    def update(self, target):
        self.x = -(target.rect.x + target.rect.w // 2 - WIDTH // 2)
        self.y = -(target.rect.y + target.rect.h // 2 - HEIGHT // 2)
