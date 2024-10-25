"""
# TableReplay class for texas hold'em.
# Class displays 8-max table, along with hole cards and betting chips
"""

import tkinter as tk
import os

class TableReplay(tk.Canvas):
    
    pos_str = ('BN', 'SB', 'BB', 'UTG', 'EP', 'MP', 'HJ', 'CO')  # Добавлены UTG и HJ
    suits = {'c': '#00A318', 's': '#000000', 'h': '#FF3333', 'd': '#0093FB'}
    
    # Обновленные координаты для 8-макс стола
    chippos_x = (357, 459, 504, 459, 357, 239, 194, 239)
    chippos_y = (106, 137, 200, 253, 273, 253, 200, 137)

    btn_x = (344, 516, 564, 526, 425, 230, 170, 222)
    btn_y = (107, 135, 225, 283, 309, 299, 231, 135)

    labelpos_x = (148, 208, 432, 563, 618, 563, 328, 208)
    labelpos_y = (225, 122, 75, 122, 225, 339, 397, 339)

    def __init__(self, parent, heropos, vilpos, situation_index, herocards, theme, **kwargs):
        tk.Canvas.__init__(self, parent, width=1078, height=662, bg=theme.bgcolor, highlightbackground=theme.bgcolor, highlightcolor=theme.bgcolor, highlightthickness=0, bd=0)

        # defines the preflop situation/positions
        self.heropos = heropos
        self.vilpos = vilpos
        self.situation_index = situation_index
        self.herocards = herocards
        
        # define images
        img_dir = f'{os.getcwd()}\\Images'
        if theme.bgcolor == "#FFFFFF":
            self.ptable = tk.PhotoImage(file=f'{img_dir}\\handreplayer_table_med_default.png')
        else:
            self.ptable = tk.PhotoImage(file=f'{img_dir}\\handreplayer_table_med_dark.png')
        self.bn_marker = tk.PhotoImage(file=f'{img_dir}\\bn_marker.png')
        self.chips_sb = tk.PhotoImage(file=f'{img_dir}\\chips_sb.png')
        self.chips_bb = tk.PhotoImage(file=f'{img_dir}\\chips_bb.png')
        self.chips_2p5bb = tk.PhotoImage(file=f'{img_dir}\\chips_2p5bb.png')
        self.chips_8bb = tk.PhotoImage(file=f'{img_dir}\\chips_8bb.png')
        self.chips_22bb = tk.PhotoImage(file=f'{img_dir}\\chips_22bb.png')
        self.suit_h = tk.PhotoImage(file=f'{img_dir}\\suit_h.png')
        self.suit_d = tk.PhotoImage(file=f'{img_dir}\\suit_d.png')
        self.suit_c = tk.PhotoImage(file=f'{img_dir}\\suit_c.png')
        self.suit_s = tk.PhotoImage(file=f'{img_dir}\\suit_s.png')
        self.blank = tk.PhotoImage(file=f'{img_dir}\\blank.png')
        

        # !Размер картинки и стола (1078х662)
        # draw table template
        self.grid(row=0, column=0, sticky='w')
        self.create_image(539, 331, anchor='center', image=self.ptable)
        
        # draw position labels
        heropos_idx = TableReplay.pos_str.index(self.heropos)
        self.poslabels = []
        for i, pos in enumerate(TableReplay.pos_str):
            strdraw_idx = (heropos_idx + 2 + i) % len(TableReplay.pos_str)
            self.poslabels.append(self.create_text(TableReplay.labelpos_x[i], TableReplay.labelpos_y[i], text=TableReplay.pos_str[strdraw_idx], anchor='center', font=("Helvetica", 10, 'bold'), fill='white'))

        # post sb and bb and btn marker
        strdraw_idx = (5 - heropos_idx) % len(TableReplay.pos_str)
        self.sb_img = self.create_image(TableReplay.chippos_x[strdraw_idx], TableReplay.chippos_y[strdraw_idx], anchor='nw', image=self.chips_sb)
        strdraw_idx = (6 - heropos_idx) % len(TableReplay.pos_str)
        self.bb_img = self.create_image(TableReplay.chippos_x[strdraw_idx], TableReplay.chippos_y[strdraw_idx], anchor='nw', image=self.chips_bb)
        strdraw_idx = (4 - heropos_idx) % len(TableReplay.pos_str)
        self.btn_img = self.create_image(TableReplay.btn_x[strdraw_idx], TableReplay.btn_y[strdraw_idx], anchor='nw', image=self.bn_marker)
        
        self.itemconfigure(self.sb_img, state='hidden')
        self.itemconfigure(self.bb_img, state='hidden')
        self.itemconfigure(self.btn_img, state='hidden')



        # place bet amounts depending on preflop situation
        vilpos_idx = TableReplay.pos_str.index(self.vilpos)
        if self.situation_index == 1:
            strdraw_idx = (vilpos_idx + 4 - heropos_idx) % 8
            self.vilchips_img = self.create_image(TableReplay.chippos_x[strdraw_idx], TableReplay.chippos_y[strdraw_idx], anchor='nw', image=self.chips_2p5bb)
        elif self.situation_index == 2:
            strdraw_idx = 4
            self.herochips_img = self.create_image(TableReplay.chippos_x[strdraw_idx], TableReplay.chippos_y[strdraw_idx], anchor='nw', image=self.chips_2p5bb)
            strdraw_idx = (vilpos_idx + 4 - heropos_idx) % 8
            self.vilchips_img = self.create_image(TableReplay.chippos_x[strdraw_idx], TableReplay.chippos_y[strdraw_idx], anchor='nw', image=self.chips_8bb)
        else:
            strdraw_idx = 4
            self.herochips_img = self.create_image(TableReplay.chippos_x[strdraw_idx], TableReplay.chippos_y[strdraw_idx], anchor='nw', image=self.chips_8bb)
            strdraw_idx = (vilpos_idx + 4 - heropos_idx) % 8
            self.vilchips_img = self.create_image(TableReplay.chippos_x[strdraw_idx], TableReplay.chippos_y[strdraw_idx], anchor='nw', image=self.chips_22bb) 
        
        self.itemconfigure(self.vilchips_img, state='hidden')
        self.itemconfigure(self.herochips_img, state='hidden')
        
        # draw hand
        self.hand1crd_img = self.create_text(351, 347, text='', anchor='e', font=("Consolas", 20, 'bold'), fill=TableReplay.suits[self.herocards[1]])
        self.hand2crd_img = self.create_text(402, 347, text='', anchor='e', font=("Consolas", 20, 'bold'), fill=TableReplay.suits[self.herocards[3]]) 
        self.hand1suit_img = self.create_image(337, 358, anchor='nw', image=self.blank)
        self.hand2suit_img = self.create_image(388, 358, anchor='nw', image=self.blank)
            
    def update(self):
        heropos_idx = TableReplay.pos_str.index(self.heropos)
        vilpos_idx = TableReplay.pos_str.index(self.vilpos)
        
        # update position labels
        for i in range(8):  # Обновлено на 8
            strdraw_idx = (heropos_idx + 2 + i) % 8  # Обновлено на 8
            self.itemconfig(self.poslabels[i], text=TableReplay.pos_str[strdraw_idx])
            
        # update sb and bb and btn marker
        self.delete(self.sb_img)
        self.delete(self.bb_img)
        self.delete(self.btn_img)
        strdraw_idx = (5 - heropos_idx) % 8  # Обновлено на 8
        self.sb_img = self.create_image(TableReplay.chippos_x[strdraw_idx], TableReplay.chippos_y[strdraw_idx], anchor='nw', image=self.chips_sb)
        strdraw_idx = (6 - heropos_idx) % 8  # Обновлено на 8
        self.bb_img = self.create_image(TableReplay.chippos_x[strdraw_idx], TableReplay.chippos_y[strdraw_idx], anchor='nw', image=self.chips_bb)
        strdraw_idx = (4 - heropos_idx) % 8  # Обновлено на 8
        self.btn_img = self.create_image(TableReplay.btn_x[strdraw_idx], TableReplay.btn_y[strdraw_idx], anchor='nw', image=self.bn_marker)
        


        # update raise and open chips, and delete overlapping images
        if self.vilchips_img:
            self.delete(self.vilchips_img)
        if self.herochips_img:
            self.delete(self.herochips_img)
            
        if self.situation_index == 0:
            pass
        
        elif self.situation_index == 1:
            strdraw_idx = (vilpos_idx + 4 - heropos_idx) % 8
            self.vilchips_img = self.create_image(TableReplay.chippos_x[strdraw_idx], TableReplay.chippos_y[strdraw_idx], anchor = 'nw', image=self.chips_2p5bb)
            if vilpos_idx == 1:
                self.delete(self.sb_img)
                
        elif self.situation_index == 2:
            strdraw_idx = 4
            self.herochips_img =self.create_image(TableReplay.chippos_x[strdraw_idx], TableReplay.chippos_y[strdraw_idx], anchor = 'nw', image=self.chips_2p5bb)
            strdraw_idx = (vilpos_idx + 4 - heropos_idx) % 8
            self.vilchips_img = self.create_image(TableReplay.chippos_x[strdraw_idx], TableReplay.chippos_y[strdraw_idx], anchor = 'nw', image=self.chips_8bb)
            if heropos_idx == 1:
                self.delete(self.sb_img)
            if vilpos_idx == 1:
                self.delete(self.sb_img)
            if vilpos_idx == 2:
                self.delete(self.bb_img)
            
        else:
            strdraw_idx = 4
            self.herochips_img = self.create_image(TableReplay.chippos_x[strdraw_idx], TableReplay.chippos_y[strdraw_idx], anchor = 'nw', image=self.chips_8bb)
            strdraw_idx = (vilpos_idx + 4 - heropos_idx) % 8
            self.vilchips_img = self.create_image(TableReplay.chippos_x[strdraw_idx], TableReplay.chippos_y[strdraw_idx], anchor = 'nw', image=self.chips_22bb)
            if heropos_idx == 1:
                self.delete(self.sb_img)
            if heropos_idx == 2:
                self.delete(self.bb_img)  
            if vilpos_idx == 1:
                self.delete(self.sb_img)
            


        # draw hand
        self.itemconfigure(self.hand1crd_img, text=self.herocards[0])
        self.itemconfigure(self.hand2crd_img, text=self.herocards[1])
        self.itemconfigure(self.hand1suit_img, image=self.suit_h if self.herocards[2] == 'h' else self.suit_s if self.herocards[2] == 's' else self.suit_c if self.herocards[2] == 'c' else self.suit_d)
        self.itemconfigure(self.hand2suit_img, image=self.suit_h if self.herocards[3] == 'h' else self.suit_s if self.herocards[3] == 's' else self.suit_c if self.herocards[3] == 'c' else self.suit_d)
        
        # show bet amounts
        self.itemconfigure(self.vilchips_img, state='normal')
        self.itemconfigure(self.herochips_img, state='normal')


            
        # update dealt hand
        if self.hand1crd_img:
            self.delete(self.hand1crd_img)
            self.delete(self.hand2crd_img)
            self.delete(self.hand1suit_img)
            self.delete(self.hand2suit_img)
            
            self.hand1crd_img = self.create_text(351, 347, text=self.herocards[0], anchor='e', font=("Consolas", 20, 'bold'), fill=TableReplay.suits[self.herocards[1]])
            self.hand2crd_img = self.create_text(402, 347, text=self.herocards[2], anchor='e', font=("Consolas", 20, 'bold'), fill=TableReplay.suits[self.herocards[3]]) 
            
            if self.herocards[1] == 'h':
                self.hand1suit_img = self.create_image(337, 358, anchor='nw', image=self.suit_h)
            elif self.herocards[1] == 'c':
                self.hand1suit_img = self.create_image(337, 358, anchor='nw', image=self.suit_c)
            elif self.herocards[1] == 'd':
                self.hand1suit_img = self.create_image(337, 358, anchor='nw', image=self.suit_d)
            elif self.herocards[1] == 's':
                self.hand1suit_img = self.create_image(337, 358, anchor='nw', image=self.suit_s)
                
            if self.herocards[3] == 'h':
                self.hand2suit_img = self.create_image(388, 358, anchor='nw', image=self.suit_h)
            if self.herocards[3] == 'c':
                self.hand2suit_img = self.create_image(388, 358, anchor='nw', image=self.suit_c)
            if self.herocards[3] == 'd':
                self.hand2suit_img = self.create_image(388, 358, anchor='nw', image=self.suit_d)
            if self.herocards[3] == 's':
                self.hand2suit_img = self.create_image(388, 358, anchor='nw', image=self.suit_s)
        