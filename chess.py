from multiprocessing.sharedctypes import Value
from random import *
import itertools as itr
from traceback import print_tb
from turtle import right
import streamlit as st
import numpy as np
import json
import requests
from streamlit_lottie import st_lottie



def CreateBorad(n):
    board = [[0 for i in range(n)] for i in range(n)]
    for c in range(n):
        for r in range(n):
            board[c][r] = 1

    return board

def isAtack(board, x, y,n):

    if not (x >= 0 and x < n and y >= 0 and y < n):
        return True
    if board[x][y] == 1:
       return True
    if (x + 1 < n) and (y - 2 >= 0):
        if (board[x + 1][y - 2] == 1):
            return True

    if (x + 2 < n) and (y - 1 >= 0):
        if (board[x + 2][y - 1] == 1):
            return True

    if (x + 2 < n) and (y + 1 < n):
        if (board[x + 2][y + 1] == 1):
            return True

    if (x + 1 < n) and (y + 2 < n):
        if (board[x + 1][y + 2] == 1):
            return True

    if (x - 1 >= 0) and (y + 2 < n):
        if (board[x - 1][y + 2] == 1):
            return True
    if (x - 2 >= 0) and (y + 1 < n):
        if (board[x - 2][y + 1] == 1):
            return True
    if (x - 2 >= 0 and y - 1 >= 0):
        if (board[x - 2][y - 1] == 1):
            return True

    if (x - 1 >= 0 and y - 2 >= 0):
        if (board[x - 1][y - 2] == 1):
            return True
    else:
        return False

def notAttacked(bd, x, y,n):
    if not isAtack(bd, x + 1, y + 2,n):
        return True
    elif not isAtack(bd, x + 2, y + 1,n):
        return True
    elif not isAtack(bd, x + 2, y - 1,n):
        return True
    elif not isAtack(bd, x + 1, y - 2,n):
        return True
    elif not isAtack(bd, x - 1, y + 2,n):
        return True
    elif not isAtack(bd, x - 2, y + 1,n):
        return True
    elif not isAtack(bd, x - 2, y - 1,n):
        return True
    elif not isAtack(bd, x - 1, y - 2,n):
        return True
    else:
        return False


def sol(n):
    n=int(n)

    c = 0
    knight = n * n
    k=0
    while(c!=2500):
        board = CreateBorad(n)
        ar = list(range(n))
        L = ar + ar
        p = list(itr.permutations(L, 2))
        while (len(p) > 0):
            indx = choices(list(p), k=1)
            x, y = indx[0]
            p.remove((x, y))
            if isAtack(board, x, y, n):
                board[x][y] = 0
            if notAttacked(board, x, y, n):
                board[x][y] = 1
        
        for x in range(n):
            for y in range(n):
                if not isAtack(board,x,y,n) : board[x][y] = 1
        k = 0
        for x1 in range(n):
            for y1 in range(n):
                if (board[x1][y1] == 1):
                    k += 1
        if k <= knight:
            bd = board
            knight = k
        k1=0  
        if(c==2499):
            for x in range(n):
                for y in range(n):
                    if (bd[x][y] == 1):
                        k1+=1
            for x in range(n):
                for y in range(n):
                    if (bd[x][y] == 1):
                        bd[x][y]='🐴'
                    if (bd[x][y] == 0):
                        bd[x][y]=' '
            
            
        #print1(bd, n)
        c += 1
    
    
    convert = np.matrix(bd)
    
    st.dataframe(convert) 
    st.write("Number of knights is : ",knight)
    
    
    
    
    
lottie_horse="https://assets6.lottiefiles.com/private_files/lf30_yhevmis3.json"
def load_lottieurl(url: str):
    
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


horse = load_lottieurl(lottie_horse)



with st.container():
    st.title("Minimal number of knights needed to occupy or attack every square of an n × n chessboard.:horse:")
    n = st.number_input("Enter The Size Of The Board",value=0)  
    left_column , right_column=st.columns(2)
    with left_column:
        if(st.button('Solve')):
            if(n<=0):
                st.write("invalid input")

            else:
                    sol(int(n))
        
    with right_column:
        st_lottie(horse,height=250,speed=0,loop=False ,key="Horse")









