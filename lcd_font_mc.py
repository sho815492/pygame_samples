# from math import log
import pygame
from pygame.locals import Rect
from lcd_font_pg import LCD_font as LCD_font_pg
from mc_remote.minecraft import Minecraft
import param_mc_remote as param
from param_mc_remote import PLAYER_ORIGIN as PO
from param_mc_remote import block

LCD_0 = (0, 1, 1, 1, 0,
         1, 0, 0, 0, 1,
         1, 0, 0, 1, 1,
         1, 0, 1, 0, 1,
         1, 1, 0, 0, 1,
         1, 0, 0, 0, 1,
         0, 1, 1, 1, 0)

LCD_1 = (0, 0, 1, 0, 0,
         0, 1, 1, 0, 0,
         0, 0, 1, 0, 0,
         0, 0, 1, 0, 0,
         0, 0, 1, 0, 0,
         0, 0, 1, 0, 0,
         0, 1, 1, 1, 0)

LCD_2 = (0, 1, 1, 1, 0,
         1, 0, 0, 0, 1,
         0, 0, 0, 0, 1,
         0, 0, 0, 1, 0,
         0, 0, 1, 0, 0,
         0, 1, 0, 0, 0,
         1, 1, 1, 1, 1)

LCD_3 = (1, 1, 1, 1, 0,
         0, 0, 0, 0, 1,
         0, 0, 0, 0, 1,
         1, 1, 1, 1, 0,
         0, 0, 0, 0, 1,
         0, 0, 0, 0, 1,
         1, 1, 1, 1, 0)

LCD_4 = (1, 0, 0, 0, 1,
         1, 0, 0, 0, 1,
         1, 0, 0, 0, 1,
         0, 1, 1, 1, 1,
         0, 0, 0, 0, 1,
         0, 0, 0, 0, 1,
         0, 0, 0, 0, 1)

LCD_5 = (0, 1, 1, 1, 1,
         1, 0, 0, 0, 0,
         1, 0, 0, 0, 0,
         0, 1, 1, 1, 0,
         0, 0, 0, 0, 1,
         0, 0, 0, 0, 1,
         1, 1, 1, 1, 0)

LCD_6 = (0, 1, 1, 1, 0,
         1, 0, 0, 0, 0,
         1, 0, 0, 0, 0,
         1, 1, 1, 1, 0,
         1, 0, 0, 0, 1,
         1, 0, 0, 0, 1,
         0, 1, 1, 1, 0)

LCD_7 = (0, 1, 1, 1, 0,
         1, 0, 0, 0, 1,
         1, 0, 0, 0, 1,
         1, 0, 0, 0, 1,
         0, 0, 0, 0, 1,
         0, 0, 0, 0, 1,
         0, 0, 0, 0, 1)

LCD_8 = (0, 1, 1, 1, 0,
         1, 0, 0, 0, 1,
         1, 0, 0, 0, 1,
         0, 1, 1, 1, 0,
         1, 0, 0, 0, 1,
         1, 0, 0, 0, 1,
         0, 1, 1, 1, 0)

LCD_9 = (0, 1, 1, 1, 0,
         1, 0, 0, 0, 1,
         1, 0, 0, 0, 1,
         0, 1, 1, 1, 1,
         0, 0, 0, 0, 1,
         0, 0, 0, 0, 1,
         0, 1, 1, 1, 0)

LCD_10 = (0, 0, 0, 0, 0,
         0, 1, 1, 0, 0,
         0, 1, 1, 0, 0,
         0, 0, 0, 0, 0,
         0, 1, 1, 0, 0,
         0, 1, 1, 0, 0,
         0, 0, 0, 0, 0)

LCD_11 = (0, 0, 0, 0, 0,
         0, 0, 0, 0, 0,
         0, 0, 0, 0, 0,
         1, 1, 1, 1, 1,
         0, 0, 0, 0, 0,
         0, 0, 0, 0, 0,
         0, 0, 0, 0, 0)

LCD_font_styles = (LCD_0, LCD_1, LCD_2, LCD_3, LCD_4, LCD_5, LCD_6, LCD_7, LCD_8, LCD_9, LCD_10, LCD_11)

class LCD_font_MC():
    def __init__(self, mc, PO_X, PO_Y, PO_Z):
        self.mc = mc    # 接続情報
        self.PO_X = PO_X # 基準X座標
        self.PO_Y = PO_Y # 基準Y座標
        self.PO_Z = PO_Z # 基準Z座標
        
    def init_col(self, BLOCK_ON="diamond_block", BLOCK_OFF="air"):
        
        self.BLOCK_ON = BLOCK_ON
        self.BLOCK_OFF = BLOCK_OFF
       
    def init_row(self, X_ORG=2, Y_ORG=8, Z_ORG =6, COL_INTV=6):  # 表示行の設定
        self.X_ORG = X_ORG
        self.Y_ORG = Y_ORG
        self.Z_ORG = Z_ORG
        self.COL_INTV = COL_INTV # 各桁のブロック間隔
        
        
    def update_col(self, col=0, code=2):  # ある桁にある文字を表示する関数
        # codeの文字をcol桁目に表示、桁は最上位桁の左から右へ進む。
        
        i = 0
        for y_dot in range(7):
            for x_dot in range(5):
                if LCD_font_styles[int(code)][i] == 1:
                    block_type = self.BLOCK_ON
                else:
                    block_type = self.BLOCK_OFF
                # 桁の原点
                x0 = self.X_ORG + self.COL_INTV * col
                y0 = self.Y_ORG
                z0 = self.Z_ORG
                # ドットの原点座標
                lcd_x = x0 + x_dot * self.COL_INTV
                lcd_y = y0 + y_dot * self.COL_INTV

                

                #絶対座標の計算とブロック設置
                mc_x = self.PO_X + lcd_x
                mc_y = self.PO_Y + lcd_y
                mc_z = self.PO_Z # Z軸は固定

                # ドットを描く
                print(mc_x, mc_y, mc_z, block_type)
                self.mc.setBlock(mc_x, mc_y, mc_z, block_type)
                
                i += 1

