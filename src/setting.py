import pygame
from .holder     import Link
from .background import Background
from .button     import Button
from .run_type   import Run_type

def  inc(data): return min(20,data+1)
def ninc(data): return max(5,data-1)      
def minc(data, module): return (data-1)%module
def mninc(data, module): return (data+1)%module
 
      
class Setting:
    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT):
        self.board           = Background(SCREEN_WIDTH, SCREEN_HEIGHT, Link.board)
        self.grid_size       = 480
        self.grid_div        = 10
        self.box_sz          = self.grid_size/self.grid_div

        self.o_cnt           = 0
        self.x_cnt           = 1
        self.box             = pygame.transform.scale(pygame.image.load(Link.box[0]), (self.box_sz, self.box_sz))
        self.wbox            = pygame.transform.scale(pygame.image.load(Link.box[1]), (self.box_sz, self.box_sz))
        self.x_img           = pygame.image.load(Link.p_img[self.x_cnt])
        self.x_img           = pygame.transform.scale(self.x_img, (self.box_sz, self.box_sz))
        self.o_img           = pygame.image.load(Link.p_img[self.o_cnt])
        self.o_img           = pygame.transform.scale(self.o_img, (self.box_sz, self.box_sz))
        
        self.setting_menu    = Background(106*4.55, 122*4.2,Link.setting_menu, 40, 58)
        self.font            = pygame.font.Font(None , 80)
        self.board_sz_txt    = self.font.render(str(self.grid_div), False, (255,255,255))
        
        self.inc_button_brd  = Button(420, 195, 50, 50, Link.inc, Link.inc_hover)
        self.ninc_button_brd = Button(270, 195, 50, 50, Link.ninc, Link.ninc_hover)
        
        self.inc_button_po   = Button(420, 295, 50, 50, Link.inc, Link.inc_hover)
        self.ninc_button_po  = Button(270, 295, 50, 50, Link.ninc, Link.ninc_hover)
        
        self.inc_button_px   = Button(420, 395, 50, 50, Link.inc, Link.inc_hover)
        self.ninc_button_px  = Button(270, 395, 50, 50, Link.ninc, Link.ninc_hover)
        
        self.status         = Button(525, 80, 250, 80, Link.status, Link.status)
        self.undo           = Button(525, 180, 250, 80, Link.undo, Link.undo_hover)
        self.reset          = Button(525, 280, 250, 80, Link.reset, Link.reset_hover)
        self.back_ing        = Button(525, 380, 250, 80,Link.ok, Link.ok_hover)
        
    def update(self):
        self.box_sz         = self.grid_size/self.grid_div
        self.board_sz_txt   = self.font.render(str(self.grid_div), False, (255,255,255))
        
        self.box             = pygame.transform.scale(pygame.image.load(Link.box[0]), (self.box_sz, self.box_sz))
        self.wbox            = pygame.transform.scale(pygame.image.load(Link.box[1]), (self.box_sz, self.box_sz))
        self.x_img          = pygame.image.load(Link.p_img[self.x_cnt])
        self.o_img          = pygame.image.load(Link.p_img[self.o_cnt])
        self.x_img          = pygame.transform.scale(self.x_img, (self.box_sz, self.box_sz))
        self.o_img          = pygame.transform.scale(self.o_img, (self.box_sz, self.box_sz))
        pygame.display.update()

    def event_handle(self, screen, running=Run_type().SETTING):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = Run_type().EXIT
            #BOARD SETTING
            if (self.inc_button_brd.is_pressed(event)):
                self.grid_div = inc(self.grid_div)
            if (self.ninc_button_brd.is_pressed(event)):
                self.grid_div = ninc(self.grid_div)
            
            #PLAYER O SETTING
            if (self.inc_button_po.is_pressed(event)):
                self.o_cnt = minc(self.o_cnt, len(Link.p_img))
                if (self.x_cnt==self.o_cnt): self.o_cnt = minc(self.o_cnt, len(Link.p_img))

            if (self.ninc_button_po.is_pressed(event)):
                self.o_cnt = mninc(self.o_cnt, len(Link.p_img))
                if (self.x_cnt==self.o_cnt): self.o_cnt = mninc(self.o_cnt, len(Link.p_img))
                
            #PLAYER X SETTING
            if (self.inc_button_px.is_pressed(event)):
                self.x_cnt = minc(self.x_cnt, len(Link.p_img))
                if (self.x_cnt==self.o_cnt): self.x_cnt = minc(self.x_cnt, len(Link.p_img))
                
            if (self.ninc_button_px.is_pressed(event)):
                self.x_cnt = mninc(self.x_cnt, len(Link.p_img))    
                if (self.x_cnt==self.o_cnt): self.x_cnt = mninc(self.x_cnt, len(Link.p_img))

            #BACK_TO_INGAME
            if (self.back_ing.is_pressed(event)):
                running = Run_type().IN_GAME

            self.update()
        return running        

    def draw(self, screen):
        self.board.draw(screen)
        self.status.draw(screen) 
        self.undo.draw(screen) 
        self.reset.draw(screen) 
        bg        = pygame.Surface((800, 600), pygame.SRCALPHA)
        bg.fill((0, 0, 0, 70))
        screen.blit(bg, (0, 0))

        self.setting_menu.draw(screen)
        screen.blit(self.board_sz_txt, (335, 200))       
        #line 1
        self.inc_button_brd.draw(screen) 
        self.ninc_button_brd.draw(screen)
        #line 2
        self.inc_button_po.draw(screen) 
        self.ninc_button_po.draw(screen)
        #line 3
        self.inc_button_px.draw(screen) 
        self.ninc_button_px.draw(screen)
        
        SET_O = pygame.transform.scale(self.o_img, (60, 60))
        SET_X = pygame.transform.scale(self.x_img, (60, 60))
        screen.blit(SET_O, (340, 295))
        screen.blit(SET_X, (340, 395))
        
        self.back_ing.draw(screen) 
        return self.event_handle(screen)
        
        
