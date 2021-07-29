#!/usr/bin/env python
# coding: utf-8

# In[5]:


from IPython.display import clear_output
def display_board(board):
    print(board[7]+'|'+board[8]+'|'+board[9])
    print(board[4]+'|'+board[5]+'|'+board[6])
    print(board[1]+'|'+board[2]+'|'+board[3])


# In[6]:


test_board=['#','X','O','X','O','X','O','X','O','X']
display_board(test_board)


# In[7]:


def player_input():
    marker=''
    #KEEP ASKING PLAYER 1 TO CHOOSE X or O
    while marker !='X' and marker != 'O':
        marker=input('Player 1 choose X or O: ').upper()
    #ASSIGN PLAYER 2, THE OPPSITE MARKER
    player1=marker
    if player1=='X':
        player2='O'
    else:
        player2='X'
    
    return(player1,player2)

#or we can use 
#if marker =='x':
#return ('x','o')
#else: return ('o','x')


# In[8]:


player_input()


# In[10]:


def place_marker(board,marker,postion):
    board[postion]=marker


# In[11]:


test_board


# In[12]:


place_marker(test_board,'$',8)


# In[13]:


display_board(test_board)


# In[14]:


def win_check(board,mark):
    return ((board[7]==mark and board[8]==mark and board[9]==mark) or
    (board[4]==mark and board[5]==mark and board[6]==mark)or
    (board[1]==mark and board[2]==mark and board[3]==mark)or
    (board[7]==mark and board[4]==mark and board[1]==mark)or
    (board[8]==mark and board[5]==mark and board[2]==mark)or
    (board[9]==mark and board[6]==mark and board[3]==mark)or
    (board[7]==mark and board[8]==mark and board[9]==mark)or
    (board[7]==mark and board[5]==mark and board[3]==mark)or
    (board[9]==mark and board[5]==mark and board[3]==mark))



# In[15]:


display_board(test_board)
win_check(test_board,'X')


# In[16]:


import random
def choose_first():
    flip=random.randint(0,1)
    
    if flip==0:
        return 'player  1'
    else:
        return 'player 2'


# In[17]:


def space_check(board,postion):
    return board[postion]==''
    


# In[18]:


def full_board_check(board):
    
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True


# In[19]:


def player_choice(board):
    postion=0
    while postion not in [1,2,3,4,5,6,7,8,9] or not space_check(board,postion):
        postion=int(input('Choose a postion: (1-9) '))
    return postion


# In[20]:


def replay():
    input('Play again? Enter Yes or No')
    return choice =='Yes'


# In[ ]:


print('Welcome to Tic Tac Toe!')
while True:
    
    the_board=['']*10
    player1_marker,player2_marker=player_input()
    turn=choose_first()
    print(turn+' will go first')
    play_game=input('Ready to play? y or n?')
    if play_game=='y':
        game_on=True
    else:
        game_on=False
while game_on:
    if turn=='Player 1':
        display_board(the_board)
        postion=player_choice(the_board)
        place_marker(the_board,player1_marker,postion)
        
        if win_check(the_board,player1_marker):
            display_board(the_board)
            print('Player 1 is won!!')
            game_on = False
        else:
            if full_board_check(board):
                display_board()
                print('TIE GAME!!')
                game_on=False
            else:
                turn = 'palyer 2'
    else:
        display_board(the_board)
        postion=player_choice(the_board)
        place_marker(the_board,player2_marker,postion)
        
        if win_check(the_board,player2_marker):
            display_board(the_board)
            print('Player 2 is won!!')
            game_on = False
        else:
            if full_board_check(board):
                display_board()
                print('TIE GAME!!')
                game_on=False
            else:
                turn = 'palyer 1'
        
        
    if not replay():
        break
    


# In[ ]:





# In[ ]:




