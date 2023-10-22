import pygame
import os

class AllImages():
    '''定义图像集合类，从此类读取各项图片'''

    def __init__(self):
        self.icon = pygame.image.load('.\\images\\icon.png')
        self.plane = []
        self.bkground = [pygame.image.load('.\\images\\background_space1.png'), pygame.image.load('.\\images\\background_space2.png')]

    def get_plane_imgs(self, ship_index=0):
        '''刷新飞船图片集'''
        plane_images = []
        image_path = ".\images\planes"
        final_path = os.path.join(image_path, os.listdir(image_path)[ship_index])
        for filename in os.listdir(final_path):
            if os.path.isfile(os.path.join(final_path, filename)) and filename.lower().endswith(".png"):
                plane_images.append(pygame.image.load(os.path.join(final_path, filename)))
        plane_images = [pygame.transform.scale(plane,(64, 64)) for plane in plane_images]

        self.plane = plane_images
