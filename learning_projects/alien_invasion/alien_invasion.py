import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    pygame.init()  #初始化背景设置
    alien_settings = Settings()
    screen = pygame.display.set_mode((alien_settings.screen_width,alien_settings.screen_height))  #创建窗口屏幕及其大小
    pygame.display.set_caption('Alien Invasion')  #窗口命名
    ship = Ship(alien_settings,screen)
    bullets = Group()

    while True:
        gf.check_events(alien_settings,screen,ship,bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(alien_settings,screen,ship,bullets)

run_game()