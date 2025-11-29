# demo for 7-segment simulation
# using the class 'Seven_seg' in seven_seg_pg.py
from datetime import datetime
import sys
import time


from mc_remote.minecraft import Minecraft
import param_mc_remote as param
from param_mc_remote import PLAYER_ORIGIN as PO
from param_mc_remote import block
from lcd_font_mc import LCD_font_MC as LCD_font_MC

# Connect to minecraft and open a session as player with origin location
mc = Minecraft.create(address=param.ADRS_MCR, port=param.PORT_MCR)
mc.setPlayer(param.PLAYER_NAME, PO.x, PO.y, PO.z)
result = mc.setPlayer(param.PLAYER_NAME, PO.x, PO.y, PO.z)


if ("Error" in result):
    sys.exit(result)
else:
    print(result)

# プレイヤーの原点座標を取得
PO_X, PO_Y, PO_Z = PO.x, PO.y, PO.z

mc.setBlock(5, param.Y_SEA + 3, 5,  'gold_block')


# ブロックの種類を定義（ダイヤモンドブロックと空気）
BLOCK_ON = 'diamond_block'
BLOCK_OFF = 'air'

lcd1 = LCD_font_MC(mc, PO_X, PO_Y, PO_Z)
lcd1.init_col(BLOCK_ON, BLOCK_OFF)
lcd1.init_row(X_ORG=-10, Y_ORG=param.Y_SEA + 15, Z_ORG=10, COL_INTV=6)

lcd2 = LCD_font_MC(mc, PO_X, PO_Y, PO_Z)
lcd2.init_col(BLOCK_ON, BLOCK_OFF)
lcd2.init_row(X_ORG=-10, Y_ORG=param.Y_SEA + 25, Z_ORG=10, COL_INTV=6)

running = True
# infinite loop top ----
while running:
    for count in range(16 ** 4):  # 0から65535まで
       
        dt_now = datetime.now()
        time_now = (dt_now.hour * 10000
                    + dt_now.minute * 100
                    + dt_now.second)
        
        lcd1.update_col(col=0, code=dt_now.hour // 10)
        lcd1.update_col(col=1, code=dt_now.hour % 10)
        lcd1.update_col(col=2, code=10)
        lcd1.update_col(col=3, code=dt_now.minute // 10)
        lcd1.update_col(col=4, code=dt_now.minute % 10)
        lcd1.update_col(col=5, code=10)
        lcd1.update_col(col=6, code=dt_now.second // 10)
        lcd1.update_col(col=7, code=dt_now.second % 10)

        month_str = str(dt_now.month).zfill(2)
        day_str = str(dt_now.day).zfill(2)
   
        lcd2.update_col(col=0, code=int(str(dt_now.year)[0]))
        lcd2.update_col(col=1, code=int(str(dt_now.year)[1]))
        lcd2.update_col(col=2, code=int(str(dt_now.year)[2]))
        lcd2.update_col(col=3, code=int(str(dt_now.year)[3]))
        lcd2.update_col(col=4, code=11)
        lcd2.update_col(col=5, code=int(month_str[0])) 
        lcd2.update_col(col=6, code=int(month_str[1])) 
        lcd2.update_col(col=7, code=11)
        lcd2.update_col(col=8, code=int(day_str[0]))
        lcd2.update_col(col=9, code=int(day_str[1]))
        lcd2.update_col(col=8, code=int(str(dt_now.day)[0]))
        
        import time 
        time.sleep(1)

