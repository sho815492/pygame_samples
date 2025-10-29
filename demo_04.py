# demo for 7-segment simulation
# using the class 'Seven_seg' in seven_seg_pg.py

from datetime import datetime
import pygame
from seven_seg_pg import Seven_seg
from lcd_font_pg import LCD_font

import sys

from mcje.minecraft import Minecraft
import param_MCJE as param
from param_MCJE import PLAYER_ORIGIN as po

# Connect to minecraft and open a session as player with origin location
mc = Minecraft.create(address=param.ADRS_MCR, port=param.PORT_MCR)
result = mc.setPlayer(param.PLAYER_NAME, po.x, po.y, po.z)
if ("Error" in result):
    sys.exit(result)
else:
    print(result)


mc.postToChat('kadai #1  the first golden block')

mc.setBlock(5, 70, 5,  param.GOLD_BLOCK)

import sys
from time import sleep

import param_MCJE as param
from mcje.minecraft import Minecraft
from param_MCJE import PLAYER_ORIGIN as po

# axis parameters
AXIS_BLOCK_X = param.DIAMOND_BLOCK
AXIS_BLOCK_Y = param.SEA_LANTERN_BLOCK
AXIS_BLOCK_Z = param.GOLD_BLOCK
AXIS_BLOCK_TOP = param.GLOWSTONE

def draw_XYZ_axis(mc, wait=0.5):
    mc.postToChat("Drawing x-axis from negative to positive region")
    for x in range(-param.AXIS_WIDTH, param.AXIS_WIDTH + 1):
        block_type = AXIS_BLOCK_X if x >= 0 else (param.AIR if x % 2 == 0 else AXIS_BLOCK_X)
        mc.setBlock(x, param.AXIS_Y_V_ORG, 0, block_type)
        sleep(wait)

    mc.postToChat("Drawing y-axis from bottom to top")
    for y in range(param.AXIS_BOTTOM, param.AXIS_TOP + 1):
        block_type = AXIS_BLOCK_Y if y >= param.AXIS_Y_V_ORG else (param.AIR if y % 2 == 0 else AXIS_BLOCK_Y)
        mc.setBlock(0, y, 0, block_type)
        sleep(wait)

    mc.postToChat("Drawing z-axis from negative to positive region")
    for z in range(-param.AXIS_WIDTH, param.AXIS_WIDTH + 1):
        block_type = AXIS_BLOCK_Z if z >= 0 else (param.AIR if z % 2 == 0 else AXIS_BLOCK_Z)
        mc.setBlock(0, param.AXIS_Y_V_ORG, z, block_type)
        sleep(wait)

def clear_XYZ_axis(mc, wait=0.5):
    mc.postToChat("Clearing x-axis from negative to positive region")
    for x in range(-param.AXIS_WIDTH, param.AXIS_WIDTH + 1):
        mc.setBlock(x, param.air, 0, debug=True)
        sleep(wait)

    mc.postToChat("Clearing y-axis from bottom to top")
    for y in range(param.AXIS_BOTTOM, param.AXIS_TOP + 1):
        mc.setBlock(x, param.air, 0, debug=True)
        sleep(wait)

    mc.postToChat("Clearing z-axis from negative to positive region")
    for z in range(-param.AXIS_WIDTH, param.AXIS_WIDTH + 1):
        mc.setBlock(x, param.air, 0, debug=True)
        sleep(wait)

def reset_minecraft_world(mc, width=48):
    mc.setBlocks(-width, param.Y_SEA + 1, -width, width, param.AXIS_TOP, width, param.AIR)
    sleep(1)
    mc.setBlocks(-width, param.Y_SEA, -width, width, param.Y_SEA, width, param.GRASS_BLOCK)
    sleep(1)

if __name__ == "__main__":
    # Connect to minecraft and open a session as player with origin location
    mc = Minecraft.create(address=param.ADRS_MCR, port=param.PORT_MCR)
    result = mc.setPlayer(param.PLAYER_NAME, po.x, po.y, po.z)
    if ("Error" in result):
        sys.exit(result)
    else:
        print(result)

    mc.postToChat("axis_flat.py")
    reset_minecraft_world(mc, width=48)
    # draw_XYZ_axis(mc)
    # clear_XYZ_axis(mc, wait=0.05)
    draw_XYZ_axis(mc, wait=0.25)

    if __name__ == "__main__":
    # ... (省略: 接続とプレイヤー設定) ...

     mc.postToChat("axis_flat.py")
    reset_minecraft_world(mc, width=48)
    
    # 軸を描画する
    draw_XYZ_axis(mc, wait=0.25)
    
    # --- 軸の消去を実行 ---
    mc.postToChat("Clearing axis...")
    sleep(2) # 描画された軸をしばらく観察できるように待機
    clear_XYZ_axis(mc, wait=0.05) 

DARK_GRAY = (40, 40, 40)
GRAY = (80, 80, 80)
RED = (255, 0, 0)
GREEN = (10, 250, 10)
CYAN = (120, 120, 250)
YELLOW = (250, 250, 20)
WHITE = (250, 250, 250)

pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode([600, 450])
pygame.display.set_caption("pygame 7-segment display simulation")
screen.fill(DARK_GRAY)

display1 = Seven_seg(screen)
display1.init_col(BLOCK_SIZE=9, BLOCK_INTV=10, COLOR_ON=GREEN, COLOR_OFF=DARK_GRAY)
display1.init_row(X_ORG=8, Y_ORG=22, COL_INTV=6)

display2 = Seven_seg(screen)
display2.init_col(BLOCK_SIZE=7, BLOCK_INTV=8, COLOR_ON=RED, COLOR_OFF=GRAY)
display2.init_row(X_ORG=2, Y_ORG=18, COL_INTV=6)

display3 = Seven_seg(screen)
display3.init_col(BLOCK_SIZE=4, BLOCK_INTV=4)
display3.init_row(X_ORG=20, Y_ORG=66, COL_INTV=6)

display4 = Seven_seg(screen)
display4.init_col(BLOCK_SIZE=4, BLOCK_INTV=4)
display4.init_row(X_ORG=2, Y_ORG=76, COL_INTV=6)

display5 = Seven_seg(screen)
display5.init_col(BLOCK_SIZE=9, BLOCK_INTV=9, COLOR_ON=(120, 200, 250), COLOR_OFF=GRAY)
display5.init_row(X_ORG=8, Y_ORG=8, COL_INTV=6)

lcd1 = LCD_font(screen)
lcd1.init_col(BLOCK_SIZE=7, BLOCK_INTV=8, COLOR_ON=GREEN, COLOR_OFF=GRAY)
lcd1.init_row(X_ORG=2, Y_ORG=20, COL_INTV=6)

lcd2 = LCD_font(screen)
lcd2.init_col(BLOCK_SIZE=5, BLOCK_INTV=7, COLOR_ON=RED, COLOR_OFF=GRAY)
lcd2.init_row(X_ORG=3, Y_ORG=15, COL_INTV=6)

running = True
# infinite loop top ----
while running:
    for count in range(16 ** 4):  # 0から65535まで
        # press ctrl-c or close the window to stop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        if not running:
            break
        # 「for count」のループから抜ける。whileループも抜ける。


        dt_now = datetime.now()
        time_now = (dt_now.hour * 10000
                    + dt_now.minute * 100
                    + dt_now.second)
        display5.disp_num2(zfil=True, rjust=6, num=time_now, base=10)

        lcd1.update_col(col=0, code=dt_now.hour // 10)
        lcd1.update_col(col=1, code=dt_now.hour % 10)
        lcd1.update_col(col=2, code=10)
        lcd1.update_col(col=3, code=dt_now.minute // 10)
        lcd1.update_col(col=4, code=dt_now.minute % 10)
        lcd1.update_col(col=5, code=10)
        lcd1.update_col(col=6, code=dt_now.second // 10)
        lcd1.update_col(col=7, code=dt_now.second % 10)

        lcd2.update_col(col=0, code=int(str(dt_now.year)[0]))
        lcd2.update_col(col=1, code=int(str(dt_now.year)[1]))
        lcd2.update_col(col=2, code=int(str(dt_now.year)[2]))
        lcd2.update_col(col=3, code=int(str(dt_now.year)[3]))
        lcd2.update_col(col=4, code=11)
        lcd2.update_col(col=5, code=int(str(dt_now.month)[0]))
        lcd2.update_col(col=6, code=int(str(dt_now.month)[1]))
        lcd2.update_col(col=7, code=11)
        lcd2.update_col(col=8, code=int(str(dt_now.day)[0]))
        lcd2.update_col(col=9, code=int(str(dt_now.day)[1]))
        


        pygame.display.flip()  # update_col
        clock.tick(20)  # FPS, Frame Per Second
    screen.fill(DARK_GRAY)
# infinit loop bottom ----

pygame.quit()


