'''import pygame

class AnimateSprite(pygame.sprite.Sprite):

    def __init__(self, sprite_name):
        super().__init__()
        self.image = pygame.image.load(f'Feu/{sprite_name}.png')
        self.current_image = 0
        self.images = animation.get(sprite_name)

    def animate(self):
        self.current_image += 1
        if self.current_image >= len(self.images):
            self.current_image = 0

        self.image = self.images[self.current_image]


def load_animation_images(sprite_name):
    images = []
    path = f"Feu/{sprite_name}/{sprite_name}"

    for num in range(1, 24):
        image_path = path + str(num) + '.png'
        pygame.image.load(image_path)
        images.append(pygame.image.load(image_path))

    return images

animation = {
    'mummy': load_animation_images('mummy')

}

'''