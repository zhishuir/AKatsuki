# -*- coding: utf-8 -*-
# main.py
import pygame
import sys
import traceback
import myrenzhe
import enemy
import bullet
import supply
import jineng
import time

from pygame.locals import *
from random import *

pygame.init()
pygame.mixer.init()

bg_size = width, height = 1500, 950
screen = pygame.display.set_mode(bg_size)
pygame.display.set_caption("追击晓")

background = pygame.image.load("images/background.jpg").convert()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# 载入游戏音乐
pygame.mixer.music.load("sound/game_music.wav")
pygame.mixer.music.set_volume(0.2)
bullet_sound = pygame.mixer.Sound("sound/bullet.wav")
bullet_sound.set_volume(0.2)
bomb_sound = pygame.mixer.Sound("sound/use_bomb.wav")
bomb_sound.set_volume(0.2)
health_sound = pygame.mixer.Sound("sound/use_health.wav")
health_sound.set_volume(0.2)
supply_sound = pygame.mixer.Sound("sound/supply.wav")
supply_sound.set_volume(0.2)
get_bomb_sound = pygame.mixer.Sound("sound/get_bomb.wav")
get_bomb_sound.set_volume(0.2)
get_wudi_sound = pygame.mixer.Sound("sound/get_wudi.wav")
get_wudi_sound.set_volume(0.2)
get_health_sound = pygame.mixer.Sound("sound/get_health.wav")
get_health_sound.set_volume(0.2)
get_bullet_sound = pygame.mixer.Sound("sound/get_bullet.wav")
get_bullet_sound.set_volume(0.2)
tongchu_sound = pygame.mixer.Sound("sound/tongchu.wav")
tongchu_sound.set_volume(0.2)
upgrade_sound = pygame.mixer.Sound("sound/upgrade.wav")
upgrade_sound.set_volume(0.2)
enemy15_fly_sound = pygame.mixer.Sound("sound/leiqie.wav")
enemy15_fly_sound.set_volume(0.2)
enemy1_down_sound = pygame.mixer.Sound("sound/enemy1_down.wav")
enemy1_down_sound.set_volume(0.2)
enemy2_down_sound = pygame.mixer.Sound("sound/enemy2_down.wav")
enemy2_down_sound.set_volume(0.2)
enemy3_down_sound = pygame.mixer.Sound("sound/enemy3_down.wav")
enemy3_down_sound.set_volume(0.5)
enemy4_down_sound = pygame.mixer.Sound("sound/enemy4_down.wav")
enemy4_down_sound.set_volume(0.2)
enemy5_down_sound = pygame.mixer.Sound("sound/enemy5_down.wav")
enemy5_down_sound.set_volume(0.2)
enemy6_down_sound = pygame.mixer.Sound("sound/enemy4_down.wav")
enemy6_down_sound.set_volume(0.2)
enemy7_down_sound = pygame.mixer.Sound("sound/enemy7_down.wav")
enemy7_down_sound.set_volume(0.2)
enemy8_down_sound = pygame.mixer.Sound("sound/enemy8_down.wav")
enemy8_down_sound.set_volume(0.2)
enemy9_down_sound = pygame.mixer.Sound("sound/enemy9_down.wav")
enemy9_down_sound.set_volume(0.2)
enemy10_down_sound = pygame.mixer.Sound("sound/enemy10_down.wav")
enemy10_down_sound.set_volume(0.2)
enemy11_down_sound = pygame.mixer.Sound("sound/enemy11_down.wav")
enemy11_down_sound.set_volume(0.2)
enemy12_down_sound = pygame.mixer.Sound("sound/enemy12_down.wav")
enemy12_down_sound.set_volume(0.2)
enemy13_down_sound = pygame.mixer.Sound("sound/enemy13_down.wav")
enemy13_down_sound.set_volume(0.2)
enemy14_down_sound = pygame.mixer.Sound("sound/enemy14_down.wav")
enemy14_down_sound.set_volume(0.2)
enemy15_down_sound = pygame.mixer.Sound("sound/enemy15_down.wav")
enemy15_down_sound.set_volume(0.2)
enemy16_down_sound = pygame.mixer.Sound("sound/enemy16_down.wav")
enemy16_down_sound.set_volume(0.2)
huzi_sound = pygame.mixer.Sound("sound/huzi.wav")
huzi_sound.set_volume(0.2)
fire_sound = pygame.mixer.Sound("sound/fire.wav")
fire_sound.set_volume(0.2)
tongchu_sound = pygame.mixer.Sound("sound/tongchu.wav")
tongchu_sound.set_volume(0.2)
me_down_sound = pygame.mixer.Sound("sound/me_down.wav")
me_down_sound.set_volume(0.2)
use_zhengqi_sound = pygame.mixer.Sound("sound/use_zhengqi.wav")
use_zhengqi_sound.set_volume(0.2)
use_baowei_sound = pygame.mixer.Sound("sound/use_baowei.wav")
use_baowei_sound.set_volume(0.2)
use_wudi_sound = pygame.mixer.Sound("sound/use_wudi.wav")
use_wudi_sound.set_volume(0.2)
def add_small_enemies(group1, group2, num):
    for i in range(num):
        e1 = enemy.SmallEnemy(bg_size)
        group1.add(e1)
        group2.add(e1)

def add_mid_enemies(group1, group2, num):
    for i in range(num):
        e2 = enemy.MidEnemy(bg_size)
        group1.add(e2)
        group2.add(e2)

def add_big_enemies(group1, group2, num):
    for i in range(num):
        e3 = enemy.BigEnemy(bg_size)
        group1.add(e3)
        group2.add(e3)

def add_rare_enemies(group1, group2, num):
    for i in range(num):
        e4 = enemy.RareEnemy(bg_size)
        group1.add(e4)
        group2.add(e4)

def add_mianju_enemies(group1, group2, num):
    for i in range(num):
        e5 = enemy.MianjuEnemy(bg_size)
        group1.add(e5)
        group2.add(e5)

def add_didala_enemies(group1, group2, num):
    for i in range(num):
        e6 = enemy.DidalaEnemy(bg_size)
        group1.add(e6)
        group2.add(e6)

def add_jiaodu_enemies(group1, group2, num):
    for i in range(num):
        e7 = enemy.JiaoduEnemy(bg_size)
        group1.add(e7)
        group2.add(e7)

def add_xie_enemies(group1, group2, num):
    for i in range(num):
        e8 = enemy.XieEnemy(bg_size)
        group1.add(e8)
        group2.add(e8)

def add_you_enemies(group1, group2, num):
    for i in range(num):
        e9 = enemy.YouEnemy(bg_size)
        group1.add(e9)
        group2.add(e9)
def add_xiaonan_enemies(group1, group2, num):
    for i in range(num):
        e10 = enemy.XiaonanEnemy(bg_size)
        group1.add(e10)
        group2.add(e10)
def add_tiandao_enemies(group1, group2, num):
    for i in range(num):
        e11 = enemy.TiandaoEnemy(bg_size)
        group1.add(e11)
        group2.add(e11)
def add_guijiao_enemies(group1, group2, num):
    for i in range(num):
        e12 = enemy.GuijiaoEnemy(bg_size)
        group1.add(e12)
        group2.add(e12)
def add_feiduan_enemies(group1, group2, num):
    for i in range(num):
        e13 = enemy.FeiduanEnemy(bg_size)
        group1.add(e13)
        group2.add(e13)
def add_jue_enemies(group1, group2, num):
    for i in range(num):
        e14 = enemy.JueEnemy(bg_size)
        group1.add(e14)
        group2.add(e14)
def add_kakaxi_enemies(group1, group2, num):
    for i in range(num):
        e15 = enemy.KakaxiEnemy(bg_size)
        group1.add(e15)
        group2.add(e15)

def add_fire_enemies(group1, group2, num):
    for i in range(num):
        e16 = enemy.FireEnemy(bg_size)
        group1.add(e16)
        group2.add(e16)

def inc_speed(target, inc):
    for each in target:
        each.speed += inc

def main():
    pygame.mixer.music.play(-1)

    # 生成我方
    me = myrenzhe.MyRenzhe(bg_size)
    enemies = pygame.sprite.Group()

    # 生成小型敌方
    small_enemies = pygame.sprite.Group()
    add_small_enemies(small_enemies, enemies, 1)

    # 生成中型敌方
    mid_enemies = pygame.sprite.Group()
    add_mid_enemies(mid_enemies, enemies, 1)

    # 生成大型敌方
    big_enemies = pygame.sprite.Group()
    add_big_enemies(big_enemies, enemies, 1)

    # 生成稀有迪达拉
    rare_enemies = pygame.sprite.Group()
    add_rare_enemies(rare_enemies, enemies, 1)
    
    # 生成飞行迪达拉
    didala_enemies = pygame.sprite.Group()
    add_didala_enemies(didala_enemies, enemies, 0)

    # 生成面具男
    mianju_enemies = pygame.sprite.Group()
    add_mianju_enemies(mianju_enemies, enemies, 0)

    # 生成角都
    jiaodu_enemies = pygame.sprite.Group()
    add_jiaodu_enemies(jiaodu_enemies, enemies, 1)
    # 生成蝎
    xie_enemies = pygame.sprite.Group()
    add_xie_enemies(xie_enemies, enemies, 0)
    # 生成鼬
    you_enemies = pygame.sprite.Group()
    add_you_enemies(you_enemies, enemies, 0)
    # 生成小南
    xiaonan_enemies = pygame.sprite.Group()
    add_xiaonan_enemies(xiaonan_enemies, enemies, 0)
    # 生成天道
    tiandao_enemies = pygame.sprite.Group()
    add_tiandao_enemies(tiandao_enemies, enemies, 0)
    # 生成鬼鲛
    guijiao_enemies = pygame.sprite.Group()
    add_guijiao_enemies(guijiao_enemies, enemies, 0)
    # 生成飞段
    feiduan_enemies = pygame.sprite.Group()
    add_feiduan_enemies(feiduan_enemies, enemies, 0)
    # 生成绝
    jue_enemies = pygame.sprite.Group()
    add_jue_enemies(jue_enemies, enemies, 0)
    # 生成卡卡西
    kakaxi_enemies = pygame.sprite.Group()
    add_kakaxi_enemies(kakaxi_enemies, enemies, 0)
    # 生成火球
    fire_enemies = pygame.sprite.Group()
    add_fire_enemies(fire_enemies, enemies, 0)


    # 生成蒸汽
    zhengqi = []
    zhengqi_index = 0
    ZHENGQI_NUM = 1
    for i in range(ZHENGQI_NUM):
        zhengqi.append(jineng.Zhengqi(me.rect.midtop))

    # 生成蒸危暴威
    baowei = []
    baowei_index = 0
    BAOWEI_NUM = 1
    for i in range(BAOWEI_NUM):
        baowei.append(jineng.Baowei(me.rect.midtop))

    
    # 生成普通子弹
    bullet1 = []
    bullet1_index = 0
    BULLET1_NUM = 10
    for i in range(BULLET1_NUM):
        bullet1.append(bullet.Bullet1(me.rect.midright))

    # 生成超级子弹
    bullet2 = []
    bullet2_index = 0
    BULLET2_NUM = 10
    for i in range(BULLET2_NUM//2):
        bullet2.append(bullet.Bullet2((me.rect.centerx-33, me.rect.centery)))
        bullet2.append(bullet.Bullet2((me.rect.centerx+30, me.rect.centery)))

    clock = pygame.time.Clock()
    # 中弹图片索引
    e1_destroy_index = 0
    e2_destroy_index = 0
    e3_destroy_index = 0
    e4_destroy_index = 0
    e5_destroy_index = 0
    e6_destroy_index = 0
    e7_destroy_index = 0
    e8_destroy_index = 0
    e9_destroy_index = 0
    e10_destroy_index = 0
    e11_destroy_index = 0
    e12_destroy_index = 0
    e13_destroy_index = 0
    e14_destroy_index = 0
    e15_destroy_index = 0
    e16_destroy_index = 0
    me_destroy_index = 0

    # 统计得分
    score = 0
    score_font = pygame.font.Font("font/font.ttf", 36)

    # 标志是否暂停游戏
    paused = False
    pause_nor_image = pygame.image.load("images/pause_nor.png").convert_alpha()
    pause_pressed_image = pygame.image.load("images/pause_pressed.png").convert_alpha()
    resume_nor_image = pygame.image.load("images/resume_nor.png").convert_alpha()
    resume_pressed_image = pygame.image.load("images/resume_pressed.png").convert_alpha()
    paused_rect = pause_nor_image.get_rect()
    paused_rect.left, paused_rect.top = width - paused_rect.width - 20, 80
    paused_image = pause_nor_image

    # 设置难度级别
    level = 1
    current_level=1
    #设置无敌数量
    wudi_num=1

    # 全屏炸弹
    bomb_image = pygame.image.load("images/bomb.png").convert_alpha()
    bomb_rect = bomb_image.get_rect()
    bomb_font = pygame.font.Font("font/font.ttf", 48)
    bomb_num = 1
    
    # 每6秒发放一个补给包
    bullet_supply = supply.Bullet_Supply(bg_size)
    bomb_supply = supply.Bomb_Supply(bg_size)
    health_supply = supply.Health_Supply(bg_size)
    restore_supply = supply.Restore_Supply(bg_size)
    wudi_supply = supply.Wudi_Supply(bg_size)
    SUPPLY_TIME = USEREVENT
    pygame.time.set_timer(SUPPLY_TIME, 6 *1000)        


    # 超级子弹定时器
    DOUBLE_BULLET_TIME = USEREVENT + 1

    # 标志是否使用蒸汽技能
    is_jineng_zhengqi = False

    # 标志是否使用爆危技能
    is_jineng_baowei = False
    
    # 标志是否使用超级子弹
    is_double_bullet = False

    # 解除我方无敌状态定时器
    INVINCIBLE_TIME = USEREVENT + 2

    # 生命数量
    life_image = pygame.image.load("images/life.png").convert_alpha()
    life_rect = life_image.get_rect()
    life_num = 3


    # 用于阻止重复打开记录文件
    recorded = False

    # 游戏结束画面
    zhengqi_font= pygame.font.Font("font/font.TTF", 48)
    gameover_font = pygame.font.Font("font/font.TTF", 48)
    again_image = pygame.image.load("images/again.png").convert_alpha()
    again_rect = again_image.get_rect()
    gameover_image = pygame.image.load("images/gameover.png").convert_alpha()
    gameover_rect = gameover_image.get_rect()

    # 用于切换图片
    switch_image = True

    # 用于延迟
    delay = 100
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1 and paused_rect.collidepoint(event.pos):
                    paused = not paused
                    if paused:
                        pygame.time.set_timer(SUPPLY_TIME, 0)
                        pygame.mixer.music.pause()
                        pygame.mixer.pause()
                    else:
                        pygame.time.set_timer(SUPPLY_TIME, 4 * 1000)
                        pygame.mixer.music.unpause()
                        pygame.mixer.unpause()

            elif event.type == MOUSEMOTION:
                if paused_rect.collidepoint(event.pos):
                    if paused:
                        paused_image = resume_pressed_image
                    else:
                        paused_image = pause_pressed_image
                else:
                    if paused:
                        paused_image = resume_nor_image
                    else:
                       paused_image = pause_nor_image

            elif event.type == KEYDOWN:
                if event.key == K_SPACE:
                    if bomb_num:
                        bomb_num -= 1
                        bomb_sound.play()
                        for each in enemies:
                            if each.rect.bottom > 0:
                                each.active = False

            if event.type == KEYDOWN:
                if event.key == K_p:
                    get_bullet_sound.play()
                    is_double_bullet = True
                    pygame.time.set_timer(DOUBLE_BULLET_TIME, 20 * 1000)
                    bullet_supply.active = False

            if event.type == KEYDOWN:
                if event.key == K_n:
                    score+=1


            if event.type == KEYDOWN:
                if event.key == K_1:
                    add_kakaxi_enemies(kakaxi_enemies, enemies, 1)

            if event.type == KEYDOWN:
                if event.key == K_2:
                    add_didala_enemies(didala_enemies, enemies, 2)
                    inc_speed(didala_enemies, 1)
                   

            if event.type == KEYDOWN:
                if event.key == K_3 and level>=7:
                    add_fire_enemies(fire_enemies, enemies, 3)
                    add_mianju_enemies(mianju_enemies, enemies, 1)


            if event.type == KEYDOWN:
                if event.key == K_4 and level>=10:
                    add_jue_enemies(jue_enemies, enemies, 10)
                    

            if event.type == KEYDOWN:
                if event.key == K_i and wudi_num>0:
                    huzi_sound.play()
                    wudi_num-=1
                    ZHENGQI_NUM+=1

            if event.type == KEYDOWN:
                if event.key == K_o and wudi_num>0:
                    wudi_num-=1
                    me.invincible = True
                    use_wudi_sound.play()
                    pygame.time.set_timer(INVINCIBLE_TIME,2000)



            if event.type == KEYDOWN:
                if event.key == K_m and score%10==6:
                    if bomb_num<3 and level<5:
                        bomb_num+=1

            if event.type == KEYDOWN:
                if event.key == K_q:
                    add_didala_enemies(didala_enemies, enemies, 1)  
                    inc_speed(didala_enemies, 1)

            if event.type == SUPPLY_TIME:
                supply_sound.play()
                if choice([True, False]):
                    bomb_supply.reset()
                else:
                    wudi_supply.reset()

            
                
            elif level>current_level:
                    health_supply.reset()
                    current_level+=1
                    ZHENGQI_NUM+=2


            elif event.type == DOUBLE_BULLET_TIME:
                is_double_bullet = False
                pygame.time.set_timer(DOUBLE_BULLET_TIME, 0)

            elif event.type == INVINCIBLE_TIME:
                me.invincible = False
                pygame.time.set_timer(INVINCIBLE_TIME, 0)

            elif event.type == KEYDOWN:
                if event.key == K_k:                   
                    if ZHENGQI_NUM>0:
                        is_jineng_zhengqi = True
                        ZHENGQI_NUM-=1
                        use_zhengqi_sound.play()
                        jinengs = zhengqi
                        jinengs[zhengqi_index].reset(me.rect.midtop)
                    else:
                        is_jineng_zhengqi = False

            if event.type == KEYDOWN:
                if event.key == K_l:                   
                    if ZHENGQI_NUM>0:
                        is_jineng_baowei = True
                        ZHENGQI_NUM-=1
                        use_baowei_sound.play()
                        jinengs = baowei
                        jinengs[baowei_index].reset(me.rect.midtop)
                    else:
                        is_jineng_baowei = False
            

            

                                            

                    
        # 根据用户的得分增加难度
        if level == 1 and score > 50000:
            level = 2
            upgrade_sound.play()
            # 增加敌怪
            add_small_enemies(small_enemies, enemies, 1)
            add_mid_enemies(mid_enemies, enemies, 1)
            add_didala_enemies(didala_enemies, enemies, 1)
        elif level == 2 and score > 100000:
            level = 3
            upgrade_sound.play()
            # 增加敌怪
            add_xie_enemies(xie_enemies, enemies, 1)
            add_jiaodu_enemies(jiaodu_enemies, enemies, 1)
            # 提升敌怪速度
            inc_speed(small_enemies, 1)
        elif level == 3 and score > 250000:
            level = 4
            upgrade_sound.play()
            # 增加敌怪
            add_you_enemies(you_enemies, enemies, 1)
            # 提升敌怪速度
            inc_speed(mid_enemies, 1)
        elif level == 4 and score > 500000:
            level = 5
            upgrade_sound.play()
            # 增加敌怪
            add_xiaonan_enemies(xiaonan_enemies, enemies, 1)
            add_you_enemies(you_enemies, enemies, 1)
            # 提升敌怪速度
            inc_speed(small_enemies, 1)
            inc_speed(big_enemies, 1)
        elif level == 5 and score > 1000000:
            level = 6
            upgrade_sound.play()
            # 增加敌怪
            add_didala_enemies(didala_enemies, enemies, 1)
            add_tiandao_enemies(tiandao_enemies, enemies, 1)
            add_xiaonan_enemies(xiaonan_enemies, enemies, 1)
            add_xie_enemies(xie_enemies, enemies, 1)
            # 提升敌怪速度
            inc_speed(small_enemies, 1)
            inc_speed(xiaonan_enemies, 1)
            inc_speed(rare_enemies, 1)
        elif level == 6 and score > 2500000:
            level = 7
            upgrade_sound.play()
            # 增加敌怪
            add_mianju_enemies(mianju_enemies, enemies, 1)
            add_tiandao_enemies(tiandao_enemies, enemies, 1)
            add_fire_enemies(fire_enemies, enemies, 2)
            # 提升敌怪速度
            inc_speed(big_enemies, 1)
            inc_speed(tiandao_enemies, 1)
        elif level == 7 and score > 5000000:
            level = 8
            upgrade_sound.play()
            # 增加敌怪
            add_mianju_enemies(mianju_enemies, enemies, 1)
            add_guijiao_enemies(guijiao_enemies, enemies, 1)
            # 提升敌怪速度
            inc_speed(small_enemies, 1)
            inc_speed(mid_enemies, 1)
            inc_speed(mianju_enemies, 1)
        elif level == 8 and score > 10000000:
            level = 9
            upgrade_sound.play()
            # 增加敌怪
            add_rare_enemies(rare_enemies, enemies, 1)
            add_feiduan_enemies(feiduan_enemies, enemies, 1)
            add_guijiao_enemies(guijiao_enemies, enemies, 1)
            # 提升敌怪速度
            inc_speed(didala_enemies, 1)
            inc_speed(mid_enemies, 1)
            inc_speed(big_enemies, 1)
            inc_speed(rare_enemies, 1)
        elif level == 9 and score > 25000000:
            level = 10
            upgrade_sound.play()
            # 增加敌怪
            add_jue_enemies(jue_enemies, enemies, 15)
            add_guijiao_enemies(guijiao_enemies, enemies, 1)
            add_feiduan_enemies(feiduan_enemies, enemies, 1)
        elif level == 10 and score > 50000000:
            level = 11
            upgrade_sound.play()
            # 增加敌怪
            add_you_enemies(you_enemies, enemies, 2)
            add_mianju_enemies(mianju_enemies, enemies, 1)
            # 提升敌怪速度
            inc_speed(you_enemies, 1)
            inc_speed(mianju_enemies, 1)
        elif level == 11 and score > 100000000:
            level = 12
            upgrade_sound.play()
            # 增加敌怪
            add_feiduan_enemies(feiduan_enemies, enemies, 1)
            add_jiaodu_enemies(jiaodu_enemies, enemies, 1)
            # 提升敌怪速度
            inc_speed(feiduan_enemies, 1)
            inc_speed(jiaodu_enemies, 1)


        screen.blit(background, (0, 0))
                
        if life_num and not paused:
            # 检测用户的键盘操作
            key_pressed = pygame.key.get_pressed()

            if key_pressed[K_w] or key_pressed[K_UP]:
                me.moveUp()
            if key_pressed[K_s] or key_pressed[K_DOWN]:
                me.moveDown()
            if key_pressed[K_a] or key_pressed[K_LEFT]:
                me.moveLeft()
            if key_pressed[K_d] or key_pressed[K_RIGHT]:
                me.moveRight()
            

            # 绘制全屏炸弹补给并检测是否获得
            if bomb_supply.active:
                bomb_supply.move()
                screen.blit(bomb_supply.image, bomb_supply.rect)
                if pygame.sprite.collide_mask(bomb_supply, me):
                    get_bomb_sound.play()
                    if bomb_num < 3:
                        bomb_num += 1
                    bomb_supply.active = False

            # 绘制蒸汽补给并检测是否获得
            if restore_supply.active:
                restore_supply.move()
                screen.blit(restore_supply.image, restore_supply.rect)
                if pygame.sprite.collide_mask(restore_supply, me):
                    get_health_sound.play()
                    if ZHENGQI_NUM >=0:
                        ZHENGQI_NUM += 1
                    restore_supply.active = False

            # 绘制生命补给并检测是否获得
            if health_supply.active:
                health_supply.move()
                screen.blit(health_supply.image, health_supply.rect)
                if pygame.sprite.collide_mask(health_supply, me):
                    get_health_sound.play()
                    if life_num < 16:
                        life_num += 1
                        health_supply.active=False
                    else:
                        health_supply.active=False
                        
        

            # 绘制无敌补给并检测是否获得
            if wudi_supply.active:
                wudi_supply.move()
                screen.blit(wudi_supply.image, wudi_supply.rect)
                if pygame.sprite.collide_mask(wudi_supply, me):
                    get_wudi_sound.play()
                    if wudi_num <1:
                        wudi_num += 1
                        wudi_supply.active=False
                    else:
                        wudi_supply.active=False

            # 发射子弹
            if not(delay % 10):
                bullet_sound.play()
                if is_double_bullet:
                    bullets = bullet2
                    bullets[bullet2_index].reset((me.rect.centerx-33, me.rect.centery))
                    bullets[bullet2_index+1].reset((me.rect.centerx+30, me.rect.centery))
                    bullet2_index = (bullet2_index + 2) % BULLET2_NUM
                else:
                    bullets = bullet1
                    bullets[bullet1_index].reset(me.rect.midright)
                    bullet1_index = (bullet1_index + 1) % BULLET1_NUM


                
            # 检测子弹是否击中敌方
            for b in bullets:
                if b.active:
                    b.move()
                    screen.blit(b.image, b.rect)
                    enemy_hit = pygame.sprite.spritecollide(b, enemies, False, pygame.sprite.collide_mask)
                    if enemy_hit:
                        b.active = False
                        for e in enemy_hit:
                            if e  not in small_enemies:
                                e.hit = True
                                e.energy -= 1
                                if e.energy == 0:
                                    e.active = False
                            else:
                                e.active = False

            # 检测蒸汽人是否击中敌方
            for c in zhengqi:
                if is_jineng_zhengqi==True:
                    c.move()
                    screen.blit(c.image, c.rect)
                    enemy_hit = pygame.sprite.spritecollide(c, enemies, False, pygame.sprite.collide_mask)
                    if enemy_hit:
                        is_jineng_zhengqi = True
                        for e in enemy_hit:
                            if e not in small_enemies:
                                e.hit = True
                                e.energy-=1
                                if e.energy == 0:
                                    e.active = False
                            else:
                                e.active = False

            # 检测蒸危暴威是否击中敌方
            for d in baowei:
                if is_jineng_baowei==True:
                    d.move()
                    screen.blit(d.image, d.rect)
                    enemy_hit = pygame.sprite.spritecollide(d, enemies, False, pygame.sprite.collide_mask)
                    if enemy_hit:
                        is_jineng_baowei=False
                        for g in enemy_hit:
                            g.active = False

            # 绘制卡卡西
            for each in kakaxi_enemies:
                if each.active:
                    each.move()

                    if each.hit:
                        screen.blit(each.image_hit, each.rect)
                        each.hit = False
                    else:
                        screen.blit(each.image, each.rect)
                    # 即将出现在画面中，播放音效
                    if each.rect.left == 1400:
                        enemy15_fly_sound.play()

                else:
                    # 毁灭
                    if not(delay % 3):
                        if e15_destroy_index == 0:
                            enemy15_down_sound.play()
                        screen.blit(each.destroy_images[e15_destroy_index], each.rect)
                        e15_destroy_index = (e15_destroy_index + 1) % 4
                        if e15_destroy_index == 0:
                            enemy15_fly_sound.stop()
                            score += 10000
                            each.reset()
                            if choice([True, False]):
                                if choice([True, False]):
                                    if choice([True, False]):
                                            restore_supply.reset()                         
            # 绘制绝：
            for each in jue_enemies:
                if each.active:
                    each.move()

                    if each.hit:
                        screen.blit(each.image_hit, each.rect)
                        each.hit = False
                    else:
                        screen.blit(each.image, each.rect)

                else:
                    # 毁灭
                    if not(delay % 3):
                        if e14_destroy_index == 0:
                            enemy14_down_sound.play()
                        screen.blit(each.destroy_images[e14_destroy_index], each.rect)
                        e14_destroy_index = (e14_destroy_index + 1) % 4
                        if e14_destroy_index == 0:
                            score += 30000
                            each.reset()
                            if choice([True, False]):
                                if choice([True, False]):
                                    if choice([True, False]):
                                            restore_supply.reset()

             # 绘制火球：
            for each in fire_enemies:
                if each.active:
                    each.move()
                    if each.hit:
                        screen.blit(each.image_hit, each.rect)
                        each.hit = False
                    else:
                        screen.blit(each.image, each.rect)
                    # 即将出现在画面中，播放音效
                    if each.rect.left == 1480:
                        fire_sound.play()
                else:
                    # 毁灭
                    if not(delay % 3):
                        if e16_destroy_index == 0:
                            enemy16_down_sound.play()
                        screen.blit(each.destroy_images[e16_destroy_index], each.rect)
                        e16_destroy_index = (e16_destroy_index + 1) % 4
                        if e16_destroy_index == 0:
                            each.reset()
                                                        


            # 绘制飞段：
            for each in feiduan_enemies:
                if each.active:
                    each.move()

                    if each.hit:
                        screen.blit(each.image_hit, each.rect)
                        each.hit = False
                    else:
                        screen.blit(each.image, each.rect)

                    # 绘制血槽
                    pygame.draw.line(screen, BLACK, \
                                     (each.rect.left, each.rect.top - 5), \
                                     (each.rect.right, each.rect.top - 5), \
                                     2)
                    # 当生命大于30%显示绿色，否则显示红色
                    energy_remain = each.energy / enemy.FeiduanEnemy.energy
                    if energy_remain > 0.3:
                        energy_color = GREEN
                    else:
                        energy_color = RED
                    pygame.draw.line(screen, energy_color, \
                                     (each.rect.left, each.rect.top - 5), \
                                     (each.rect.left + each.rect.width * energy_remain, \
                                      each.rect.top - 5), 2)
                else:
                    # 毁灭
                    if not(delay % 3):
                        if e13_destroy_index == 0:
                            enemy13_down_sound.play()
                        screen.blit(each.destroy_images[e13_destroy_index], each.rect)
                        e13_destroy_index = (e13_destroy_index + 1) % 4
                        if e13_destroy_index == 0:
                            score += 250000
                            each.reset()
                            if choice([True, False]):
                                if choice([True, False]):
                                    if choice([True, False]):
                                            restore_supply.reset()




            # 绘制鬼鲛：
            for each in guijiao_enemies:
                if each.active:
                    each.move()

                    if each.hit:
                        screen.blit(each.image_hit, each.rect)
                        each.hit = False
                    else:
                        screen.blit(each.image, each.rect)

                    # 绘制血槽
                    pygame.draw.line(screen, BLACK, \
                                     (each.rect.left, each.rect.top - 5), \
                                     (each.rect.right, each.rect.top - 5), \
                                     2)
                    # 当生命大于30%显示绿色，否则显示红色
                    energy_remain = each.energy / enemy.GuijiaoEnemy.energy
                    if energy_remain > 0.3:
                        energy_color = GREEN
                    else:
                        energy_color = RED
                    pygame.draw.line(screen, energy_color, \
                                     (each.rect.left, each.rect.top - 5), \
                                     (each.rect.left + each.rect.width * energy_remain, \
                                      each.rect.top - 5), 2)
                else:
                    # 毁灭
                    if not(delay % 3):
                        if e12_destroy_index == 0:
                            enemy12_down_sound.play()
                        screen.blit(each.destroy_images[e12_destroy_index], each.rect)
                        e12_destroy_index = (e12_destroy_index + 1) % 4
                        if e12_destroy_index == 0:
                            score += 150000
                            each.reset()
                            if choice([True, False]):
                                if choice([True, False]):
                                    if choice([True, False]):
                                            restore_supply.reset()


            # 绘制面具男：
            for each in mianju_enemies:
                if each.active:
                    each.move()
                    
                    if each.hit:
                        screen.blit(each.image_hit, each.rect)
                        each.hit = False
                    else:
                        screen.blit(each.image, each.rect)

                    # 绘制血槽
                    pygame.draw.line(screen, BLACK, \
                                     (each.rect.left, each.rect.top - 5), \
                                     (each.rect.right, each.rect.top - 5), \
                                     2)
                    # 当生命大于30%显示绿色，否则显示红色
                    energy_remain = each.energy / enemy.MianjuEnemy.energy
                    if energy_remain > 0.3:
                        energy_color = GREEN
                    else:
                        energy_color = RED
                    pygame.draw.line(screen, energy_color, \
                                     (each.rect.left, each.rect.top - 5), \
                                     (each.rect.left + each.rect.width * energy_remain, \
                                      each.rect.top - 5), 2)
                else:
                    # 毁灭
                    if not(delay % 3):
                        if e5_destroy_index == 0:
                            enemy5_down_sound.play()
                        screen.blit(each.destroy_images[e5_destroy_index], each.rect)
                        e5_destroy_index = (e5_destroy_index + 1) % 4
                        if e5_destroy_index == 0:
                            score += 100000
                            each.reset()
                            if choice([True, False]):
                                if choice([True, False]):
                                            restore_supply.reset()
            # 绘制天道：
            for each in tiandao_enemies:
                if each.active:
                    each.move()

                    if each.hit:
                        screen.blit(each.image_hit, each.rect)
                        each.hit = False
                    else:
                        screen.blit(each.image, each.rect)

                    # 绘制血槽
                    pygame.draw.line(screen, BLACK, \
                                     (each.rect.left, each.rect.top - 5), \
                                     (each.rect.right, each.rect.top - 5), \
                                     2)
                    # 当生命大于30%显示绿色，否则显示红色
                    energy_remain = each.energy / enemy.TiandaoEnemy.energy
                    if energy_remain > 0.3:
                        energy_color = GREEN
                    else:
                        energy_color = RED
                    pygame.draw.line(screen, energy_color, \
                                     (each.rect.left, each.rect.top - 5), \
                                     (each.rect.left + each.rect.width * energy_remain, \
                                      each.rect.top - 5), 2)

                # 即将出现在画面中，播放音效
                    if each.rect.left == 1450:
                        tongchu_sound.play()
                else:
                    # 毁灭
                    if not(delay % 3):
                        if e11_destroy_index == 0:
                            enemy11_down_sound.play()
                        screen.blit(each.destroy_images[e4_destroy_index], each.rect)
                        e11_destroy_index = (e11_destroy_index + 1) % 4
                        if e11_destroy_index == 0:
                            tongchu_sound.stop()
                            score += 90000
                            each.reset()
                            if choice([True, False]):
                                if choice([True, False]):
                                    if choice([True, False]):
                                            restore_supply.reset()


            # 绘制小南：
            for each in xiaonan_enemies:
                if each.active:
                    each.move()

                    if each.hit:
                        screen.blit(each.image_hit, each.rect)
                        each.hit = False
                    else:
                        screen.blit(each.image, each.rect)

                    # 绘制血槽
                    pygame.draw.line(screen, BLACK, \
                                     (each.rect.left, each.rect.top - 5), \
                                     (each.rect.right, each.rect.top - 5), \
                                     2)
                    # 当生命大于30%显示绿色，否则显示红色
                    energy_remain = each.energy / enemy.XiaonanEnemy.energy
                    if energy_remain > 0.3:
                        energy_color = GREEN
                    else:
                        energy_color = RED
                    pygame.draw.line(screen, energy_color, \
                                     (each.rect.left, each.rect.top - 5), \
                                     (each.rect.left + each.rect.width * energy_remain, \
                                      each.rect.top - 5), 2)
                else:
                    # 毁灭
                    if not(delay % 3):
                        if e10_destroy_index == 0:
                            enemy10_down_sound.play()
                        screen.blit(each.destroy_images[e10_destroy_index], each.rect)
                        e10_destroy_index = (e10_destroy_index + 1) % 4
                        if e10_destroy_index == 0:
                            score += 70000
                            each.reset()
                            if choice([True, False]):
                                if choice([True, False]):
                                    if choice([True, False]):
                                            restore_supply.reset()


            # 绘制鼬：
            for each in you_enemies:
                if each.active:
                    each.move()

                    if each.hit:
                        screen.blit(each.image_hit, each.rect)
                        each.hit = False
                    else:
                        screen.blit(each.image, each.rect)

                    # 绘制血槽
                    pygame.draw.line(screen, BLACK, \
                                     (each.rect.left, each.rect.top - 5), \
                                     (each.rect.right, each.rect.top - 5), \
                                     2)
                    # 当生命大于30%显示绿色，否则显示红色
                    energy_remain = each.energy / enemy.YouEnemy.energy
                    if energy_remain > 0.3:
                        energy_color = GREEN
                    else:
                        energy_color = RED
                    pygame.draw.line(screen, energy_color, \
                                     (each.rect.left, each.rect.top - 5), \
                                     (each.rect.left + each.rect.width * energy_remain, \
                                      each.rect.top - 5), 2)
                else:
                    # 毁灭
                    if not(delay % 3):
                        if e9_destroy_index == 0:
                            enemy9_down_sound.play()
                        screen.blit(each.destroy_images[e9_destroy_index], each.rect)
                        e9_destroy_index = (e9_destroy_index + 1) % 4
                        if e9_destroy_index == 0:
                            score += 50000
                            each.reset()
                            if choice([True, False]):
                                if choice([True, False]):
                                    if choice([True, False]):
                                            restore_supply.reset()


            # 绘制蝎：
            for each in xie_enemies:
                if each.active:
                    each.move()

                    if each.hit:
                        screen.blit(each.image_hit, each.rect)
                        each.hit = False
                    else:
                        screen.blit(each.image, each.rect)

                else:
                    # 毁灭
                    if not(delay % 3):
                        if e8_destroy_index == 0:
                            enemy8_down_sound.play()
                        screen.blit(each.destroy_images[e8_destroy_index], each.rect)
                        e8_destroy_index = (e8_destroy_index + 1) % 4
                        if e8_destroy_index == 0:
                            score += 30000
                            each.reset()
                            if choice([True, False]):
                                if choice([True, False]):
                                    if choice([True, False]):
                                            restore_supply.reset()


            # 绘制角都：
            for each in jiaodu_enemies:
                if each.active:
                    each.move()

                    if each.hit:
                        screen.blit(each.image_hit, each.rect)
                        each.hit = False
                    else:
                        screen.blit(each.image, each.rect)

                    # 绘制血槽
                    pygame.draw.line(screen, BLACK, \
                                     (each.rect.left, each.rect.top - 5), \
                                     (each.rect.right, each.rect.top - 5), \
                                     2)
                    # 当生命大于30%显示绿色，否则显示红色
                    energy_remain = each.energy / enemy.JiaoduEnemy.energy
                    if energy_remain > 0.3:
                        energy_color = GREEN
                    else:
                        energy_color = RED
                    pygame.draw.line(screen, energy_color, \
                                     (each.rect.left, each.rect.top - 5), \
                                     (each.rect.left + each.rect.width * energy_remain, \
                                      each.rect.top - 5), 2)
                else:
                    # 毁灭
                    if not(delay % 3):
                        if e7_destroy_index == 0:
                            enemy7_down_sound.play()
                        screen.blit(each.destroy_images[e7_destroy_index], each.rect)
                        e7_destroy_index = (e7_destroy_index + 1) % 4
                        if e7_destroy_index == 0:
                            score += 20000
                            each.reset()
                            if choice([True, False]):
                                if choice([True, False]):
                                    if choice([True, False]):
                                            restore_supply.reset()
                                            

            # 绘制迪达拉：
            for each in rare_enemies:
                if each.active:
                    each.move()

                    if each.hit:
                        screen.blit(each.image_hit, each.rect)
                        each.hit = False
                    else:
                        screen.blit(each.image, each.rect)

                    # 绘制血槽
                    pygame.draw.line(screen, BLACK, \
                                     (each.rect.left, each.rect.top - 5), \
                                     (each.rect.right, each.rect.top - 5), \
                                     2)
                    # 当生命大于30%显示绿色，否则显示红色
                    energy_remain = each.energy / enemy.RareEnemy.energy
                    if energy_remain > 0.3:
                        energy_color = GREEN
                    else:
                        energy_color = RED
                    pygame.draw.line(screen, energy_color, \
                                     (each.rect.left, each.rect.top - 5), \
                                     (each.rect.left + each.rect.width * energy_remain, \
                                      each.rect.top - 5), 2)
                else:
                    # 毁灭
                    if not(delay % 3):
                        if e4_destroy_index == 0:
                            enemy4_down_sound.play()
                        screen.blit(each.destroy_images[e4_destroy_index], each.rect)
                        e4_destroy_index = (e4_destroy_index + 1) % 4
                        if e4_destroy_index == 0:
                            score += 4000
                            each.reset()
                            if choice([True, False]):
                                if choice([True, False]):
                                    if choice([True, False]):
                                            restore_supply.reset()

            # 绘制飞行迪达拉：
            for each in didala_enemies:
                if each.active:
                    each.move()

                    if each.hit:
                        screen.blit(each.image_hit, each.rect)
                        each.hit = False
                    else:
                        screen.blit(each.image, each.rect)

                    # 绘制血槽
                    pygame.draw.line(screen, BLACK, \
                                     (each.rect.left, each.rect.top - 5), \
                                     (each.rect.right, each.rect.top - 5), \
                                     2)
                    # 当生命大于30%显示绿色，否则显示红色
                    energy_remain = each.energy / enemy.DidalaEnemy.energy
                    if energy_remain > 0.3:
                        energy_color = GREEN
                    else:
                        energy_color = RED
                    pygame.draw.line(screen, energy_color, \
                                     (each.rect.left, each.rect.top - 5), \
                                     (each.rect.left + each.rect.width * energy_remain, \
                                      each.rect.top - 5), 2)
                else:
                    # 毁灭
                    if not(delay % 3):
                        if e6_destroy_index == 0:
                            enemy6_down_sound.play()
                        screen.blit(each.destroy_images[e6_destroy_index], each.rect)
                        e6_destroy_index = (e6_destroy_index + 1) % 4
                        if e6_destroy_index == 0:
                            score += 8000
                            each.reset()
                            if choice([True, False]):
                                if choice([True, False]):
                                    if choice([True, False]):
                                            restore_supply.reset()


            
                        
            # 绘制鸣人
            for each in big_enemies:
                if each.active:
                    each.move()
                    if each.hit:
                        screen.blit(each.image_hit, each.rect)
                        each.hit = False
                    else:
                        if switch_image:
                            screen.blit(each.image1, each.rect)
                        else:
                            screen.blit(each.image2, each.rect)
                else:
                    # 毁灭
                    if not(delay % 3):
                        if e3_destroy_index == 0:
                            enemy3_down_sound.play()
                        screen.blit(each.destroy_images[e3_destroy_index], each.rect)
                        e3_destroy_index = (e3_destroy_index + 1) % 6
                        if e3_destroy_index == 0:
                            score += 3000
                            each.reset()
                            if choice([True, False]):
                                if choice([True, False]):
                                    if choice([True, False]):
                                        if choice([True, False]):
                                            restore_supply.reset()

                            
                            

            # 绘制佐助：
            for each in mid_enemies:
                if each.active:
                    each.move()

                    if each.hit:
                        screen.blit(each.image_hit, each.rect)
                        each.hit = False
                    else:
                        screen.blit(each.image, each.rect)

                else:
                    # 毁灭
                    if not(delay % 3):
                        if e2_destroy_index == 0:
                            enemy2_down_sound.play()
                        screen.blit(each.destroy_images[e2_destroy_index], each.rect)
                        e2_destroy_index = (e2_destroy_index + 1) % 4
                        if e2_destroy_index == 0:
                            score += 2000
                            each.reset()
                         
                           

            # 绘制小樱：
            for each in small_enemies:
                if each.active:
                    each.move()
                    screen.blit(each.image, each.rect)
                else:
                    # 毁灭
                    if not(delay % 3):
                        if e1_destroy_index == 0:
                            enemy1_down_sound.play()
                        screen.blit(each.destroy_images[e1_destroy_index], each.rect)
                        e1_destroy_index = (e1_destroy_index + 1) % 4
                        if e1_destroy_index == 0:
                            score += 1000
                            each.reset()
                    
            # 检测我方是否被撞
            enemies_down = pygame.sprite.spritecollide(me, enemies, False, pygame.sprite.collide_mask)
            if enemies_down and not me.invincible:
                me.active = False
                for e in enemies_down:
                    e.active = False
            
            # 绘制我方
            if me.active:
                if switch_image:
                    screen.blit(me.image1, me.rect)
                else:
                    screen.blit(me.image2, me.rect)
            else:
                # 毁灭
                if not(delay % 3):
                    if me_destroy_index == 0:
                        me_down_sound.play()
                    screen.blit(me.destroy_images[me_destroy_index], me.rect)
                    me_destroy_index = (me_destroy_index + 1) % 4
                    if me_destroy_index == 0:
                        life_num -= 1
                        me.reset()
                        pygame.time.set_timer(INVINCIBLE_TIME, 3 * 1000)
                    

            # 绘制全屏炸弹数量
            bomb_text = bomb_font.render(" X %d" % bomb_num, True, WHITE)
            text_rect = bomb_text.get_rect()
            screen.blit(bomb_image, (50,830))
            screen.blit(bomb_text, (150,850))

            # 绘制剩余生命数量
            if life_num:
                for i in range(life_num):
                    screen.blit(life_image, \
                                (width-5-(i+1)*120, \
                                 height-850-life_rect.height))
        

            # 绘制剩余技能数量
            zhengqi_image= pygame.image.load("images/zheng.png").convert_alpha()
            zhengqi_text = zhengqi_font.render(" X %d" % ZHENGQI_NUM, True, WHITE)
            text_rect = zhengqi_text.get_rect()
            screen.blit(zhengqi_image, (600, 820))
            screen.blit( zhengqi_text, (750, 850))


            # 绘制剩余无敌数量
            wudi_image= pygame.image.load("images/wuditu.png").convert_alpha()
            wudi_text = zhengqi_font.render(" X %d" % wudi_num, True, WHITE)
            text_rect = wudi_text.get_rect()
            screen.blit(wudi_image, (1000, 800))
            screen.blit( wudi_text, (1150, 850))
            
            #绘制等级
            level_font = pygame.font.Font("font/font.ttf", 48)
            level_txt=level_font.render("Level : %s" % str(level), True, WHITE)
            screen.blit(level_txt, (10,50))
            # 绘制得分
            score_text = score_font.render("Score : %s" % str(score), True, WHITE)
            screen.blit(score_text, (10, 5))

        # 绘制游戏结束画面
        elif life_num == 0:
            # 背景音乐停止
            pygame.mixer.music.stop()

            # 停止全部音效
            pygame.mixer.stop()

            # 停止发放补给
            pygame.time.set_timer(SUPPLY_TIME, 0)       

            if not recorded:
                recorded = True
                # 读取历史最高得分
                with open("最高分在此记录.txt", "r") as f:
                    record_score = int(f.read())

                # 如果玩家得分高于历史最高得分，则存档
                if score > record_score:
                    with open("最高分在此记录.txt", "w") as f:
                        f.write(str(score))
    
            # 绘制结束画面
            record_score_text = score_font.render("This : %d" % score, True, (255, 255, 255))
            screen.blit(record_score_text, (50, 50))
            
            gameover_text1 = gameover_font.render("Your Score", True, (255, 255, 255))
            gameover_text1_rect = gameover_text1.get_rect()
            gameover_text1_rect.left, gameover_text1_rect.top = \
                                 (width - gameover_text1_rect.width) // 2, height // 3
            screen.blit(gameover_text1, gameover_text1_rect)
            
            gameover_text2 = gameover_font.render(str(score), True, (255, 255, 255))
            gameover_text2_rect = gameover_text2.get_rect()
            gameover_text2_rect.left, gameover_text2_rect.top = \
                                 (width - gameover_text2_rect.width) // 2, \
                                 gameover_text1_rect.bottom + 10
            screen.blit(gameover_text2, gameover_text2_rect)

            again_rect.left, again_rect.top = \
                             (width - again_rect.width) // 2, \
                             gameover_text2_rect.bottom + 50
            screen.blit(again_image, again_rect)

            gameover_rect.left, gameover_rect.top = \
                                (width - again_rect.width) // 2, \
                                again_rect.bottom + 10
            screen.blit(gameover_image, gameover_rect)

            # 如果用户按下鼠标左键
            if pygame.mouse.get_pressed()[0]:
                # 获取鼠标坐标
                pos = pygame.mouse.get_pos()
                # 如果用户点击“重新开始”
                if again_rect.left < pos[0] < again_rect.right and \
                   again_rect.top < pos[1] < again_rect.bottom:
                    # 调用main函数，重新开始游戏
                    main()
                # 如果用户点击“结束游戏”            
                elif gameover_rect.left < pos[0] < gameover_rect.right and \
                     gameover_rect.top < pos[1] < gameover_rect.bottom:
                    # 退出游戏
                    pygame.quit()
                    sys.exit()      

        # 绘制暂停按钮
        screen.blit(paused_image, paused_rect)

        # 切换图片
        if not(delay % 5):
            switch_image = not switch_image

        delay -= 1
        if not delay:
            delay = 100

        pygame.display.flip()
        clock.tick(60)
        
if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        pass
    except:
        traceback.print_exc()
        pygame.quit()
        input()
