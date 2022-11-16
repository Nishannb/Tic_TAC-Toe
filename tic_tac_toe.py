import pygame
from sys import exit
from time import sleep


pygame.init()

screen=pygame.display.set_mode((600,650))
screen.fill((0,0,0))
pygame.display.set_caption('Tic-Tac-Toe')

boardnumlist=[(196, 196),
                (396, 196),
                (596, 196),
                (196, 396),
                (396, 396),
                (596, 396),
                (196, 596),
                (396, 596),
                (596, 596)]

plain_board=pygame.image.load('C:/Users/Owner/Desktop/python/projects/tic_tac_toe/components/background.png').convert_alpha()
plain_board=pygame.transform.scale(plain_board, (196,196))
plain_board_rect1=plain_board.get_rect(bottomright=(196, 196))
plain_board_rect2=plain_board.get_rect(bottomright=(396, 196))
plain_board_rect3=plain_board.get_rect(bottomright=(596, 196))
plain_board_rect4=plain_board.get_rect(bottomright=(196, 396))
plain_board_rect5=plain_board.get_rect(bottomright=(396, 396))
plain_board_rect6=plain_board.get_rect(bottomright=(596, 396))
plain_board_rect7=plain_board.get_rect(bottomright=(196, 596))
plain_board_rect8=plain_board.get_rect(bottomright=(396, 596))
plain_board_rect9=plain_board.get_rect(bottomright=(596, 596))

plain_board_list=[plain_board_rect1, plain_board_rect2, plain_board_rect3, plain_board_rect4, plain_board_rect5, plain_board_rect6, plain_board_rect7, plain_board_rect8, plain_board_rect9]

clicksound=pygame.mixer.Sound('mouseclick.mp3')

cross=pygame.image.load('C:/Users/Owner/Desktop/python/projects/tic_tac_toe/components/X.png').convert_alpha()
circle=pygame.image.load('C:/Users/Owner/Desktop/python/projects/tic_tac_toe/components/O.png').convert_alpha()
cross=pygame.transform.scale(cross, (196,196))
circle=pygame.transform.scale(circle, (196,196))

msg_font=pygame.font.Font('Pixeltype.ttf', 40)
game_result="Enter Space to play"
gamename=msg_font.render('Tic-Tac-Toe', False, 'Green', 'Yellow')
restartoption=msg_font.render(f'{game_result} again..', False, (94,129,162))
restartoption_rect=restartoption.get_rect(topleft=(150,350))

game_active=False
clock=pygame.time.Clock()

player_index=True
Player= ['Player 1', 'Player 2']
num_count=0



x=-8000
y=-8000
boardnum=0
player1_gamedata=[]
player2_gamedata=[]

game_winner_check=[]
game_winner_check_player2=[]



while True:
    
    for  event in (pygame.event.get()):
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()

        if game_active==False:
            if event.type==pygame.KEYDOWN:
                clicksound.play()
                if event.key==pygame.K_SPACE: 
                    game_active=True
        
        if player_index==True:
            
            if event.type==pygame.MOUSEBUTTONUP:
                clicksound.play()
                for board in plain_board_list:
                    
                    # print(board.x)
                    if board.collidepoint(event.pos):
                        if board.bottomright not in player1_gamedata or board.bottomright not in player2_gamedata:
                            # print(board.bottomright)
                            game_winner_check.append(boardnumlist.index(board.bottomright))
                            # print(boardnum)
                            player1_gamedata.append((board.x, board.y))
                        
                        
                            player_index=False
                       
                    
                        
        
        else:
            if event.type==pygame.MOUSEBUTTONUP:
                clicksound.play()
                for board in plain_board_list:
                    if board.collidepoint(event.pos):
                        if board.bottomright not in player2_gamedata or board.bottomright not in player1_gamedata:
                            game_winner_check_player2.append(boardnumlist.index(board.bottomright))
                            player2_gamedata.append((board.x, board.y))
                        
                            player_index=True
                  

                       
                               
    if game_active:
        screen.fill((0,0,0))
        #boxes placement
        screen.blit(plain_board, plain_board_rect1)
        screen.blit(plain_board, plain_board_rect2)
        screen.blit(plain_board, plain_board_rect3)
        screen.blit(plain_board, plain_board_rect4)
        screen.blit(plain_board, plain_board_rect5)
        screen.blit(plain_board, plain_board_rect6)
        screen.blit(plain_board, plain_board_rect7)
        screen.blit(plain_board, plain_board_rect8)
        screen.blit(plain_board, plain_board_rect9)
        
        
        for  gamedata1 in player1_gamedata:
            screen.blit(cross, gamedata1)
            
        for gamedata2 in player2_gamedata:
            screen.blit(circle, gamedata2)
           
        if len(player1_gamedata)>=5 or len(player2_gamedata)>=5:
            game_result="Game has been drawn"
            game_active=False
        
        
        if player_index==True: 
            player_change=msg_font.render(f"{Player[0]}", False, "Yellow")
            player_change_rect=player_change.get_rect(topleft=(250,610))
            screen.blit(player_change, player_change_rect)
        else: 
            player_change=msg_font.render(f"{Player[1]}", False, "Yellow")
            player_change_rect=player_change.get_rect(topleft=(250,610))
            screen.blit(player_change, player_change_rect)
        
#CHECKER PLAYER 1
        if len(game_winner_check) >= 3:
            for checkbox in range(0,8):
                
                if 0 in game_winner_check and (1 in game_winner_check and 2 in game_winner_check):
                    pygame.draw.line(screen, (0,0,0), (0,100), (600, 100), width= 5)
                    game_active=False
                    game_result= 'X'
                elif 0 in game_winner_check and (3 in game_winner_check and 6 in game_winner_check):
                    pygame.draw.line(screen, (0,0,0), (100,0), (100, 600), width= 5)
                    game_active=False
                    game_result= 'X'
                elif 0 in game_winner_check and (4 in game_winner_check and 8 in game_winner_check):
                    pygame.draw.line(screen, (0,0,0), (0,0), (600, 600), width= 5)
                    game_active=False
                    game_result= 'X'
                elif 1 in game_winner_check and 4 in game_winner_check and 7 in game_winner_check: 
                    pygame.draw.line(screen, (0,0,0), (300,0), (300, 600), width=5)
                    game_active=False
                    game_result= 'X'
                elif 2 in game_winner_check and (4 in game_winner_check and 6 in game_winner_check):
                    pygame.draw.line(screen, (0,0,0), (600,0), (0, 600), width=5)
                    game_active=False
                    game_result= 'X'
                elif 2 in game_winner_check and (5 in game_winner_check and 8 in game_winner_check):
                    pygame.draw.line(screen, (0,0,0), (500,0), (500, 600), width=5)
                    game_active=False
                    game_result= 'X'
                elif 3 in game_winner_check and 4 in game_winner_check and 5 in game_winner_check:
                    pygame.draw.line(screen, (0,0,0), (0,300), (600, 300), width=5)
                    game_active=False
                    game_result= 'X'
                elif 6 in game_winner_check and 8 in game_winner_check and 7 in game_winner_check:
                    pygame.draw.line(screen, (0,0,0), (0,500), (600, 500), width=5)
                    game_active=False
                    game_result= 'X'
                         
        
#CHECKER PLAYER 2 
        if len(game_winner_check_player2) >= 3:
            for checkbox in range(0,8):
                if 0 in game_winner_check_player2 and (1 in game_winner_check_player2 and 2 in game_winner_check_player2):
                    pygame.draw.line(screen, (0,0,0), (0,100), (600, 100), width= 5)
                    game_active=False
                    game_result='O'
                elif 0 in game_winner_check_player2 and (3 in game_winner_check_player2 and 6 in game_winner_check_player2):
                    pygame.draw.line(screen, (0,0,0), (0,100), (100, 600), width= 5)
                    game_active=False
                    game_result='O'
                elif 0 in game_winner_check_player2 and (4 in game_winner_check_player2 and 8 in game_winner_check_player2):
                    pygame.draw.line(screen, (0,0,0), (0,0), (600, 600), width= 5)
                    game_active=False
                    game_result='O'
                elif 1 in game_winner_check_player2 and 4 in game_winner_check_player2 and 7 in game_winner_check_player2: 
                    pygame.draw.line(screen, (0,0,0), (300,0), (300, 600), width=5)
                    game_active=False
                    game_result='O'
                elif 2 in game_winner_check_player2 and 4 in game_winner_check_player2 and 6 in game_winner_check_player2:
                    pygame.draw.line(screen, (0,0,0), (600,0), (0, 600), width=5)
                    game_active=False
                    game_result='O'
                elif 2 in game_winner_check_player2 and 5 in game_winner_check_player2 and 8 in game_winner_check_player2:
                    pygame.draw.line(screen, (0,0,0), (500,0), (500, 600), width=5)
                    game_active=False
                    game_result='O'
                elif 3 in game_winner_check_player2 and 4 in game_winner_check_player2 and 5 in game_winner_check_player2:
                    pygame.draw.line(screen, (0,0,0), (0,300), (600, 300), width=5)
                    game_active=False
                    game_result='O'
                elif 6 in game_winner_check_player2 and 8 in game_winner_check_player2 and 7 in game_winner_check_player2:
                    pygame.draw.line(screen, (0,0,0), (0,500), (600, 500), width=5)
                    game_active=False
                    game_result='O'
                
    else:
        
        if game_result!="Enter Space to play" :
            sleep(0.5)
        player2_gamedata.clear()
        player1_gamedata.clear()
        game_winner_check_player2.clear()
        game_winner_check.clear()
        screen.fill((94,129,162))
        end_plain_board=pygame.image.load('C:/Users/Owner/Desktop/python/projects/tic_tac_toe/components/background.png').convert_alpha()
        end_plain_board=pygame.transform.scale(end_plain_board, (400,400))
        end_plain_board_rect=end_plain_board.get_rect(center=(300, 300))
        screen.blit(end_plain_board, end_plain_board_rect)

        screen.blit(gamename, (210,180))
        if game_result!="Enter Space to play":
            if game_result=="Game has been drawn":
                over_msg=msg_font.render(f'{game_result}', False, "Red")
                over_msg_rect=over_msg.get_rect(center=(300,250))
                screen.blit(over_msg, over_msg_rect)
                screen.blit(restartoption, restartoption_rect)
            else: 
                over_msg=msg_font.render(f'Player "{game_result}" wins the game........', False, "Red")
                over_msg_rect=over_msg.get_rect(center=(300,250))
                screen.blit(over_msg, over_msg_rect)
                screen.blit(restartoption, restartoption_rect)

            
        else:
            over_msg=msg_font.render(f'     {game_result}........', False, "Red")
            over_msg_rect=over_msg.get_rect(topleft=(150,350))
            screen.blit(over_msg, over_msg_rect)
        

    pygame.key.get_pressed()
    pygame.display.update()
    clock.tick(100)


