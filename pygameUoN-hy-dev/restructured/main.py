# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 04:25:15 2020

@author: 戴可昕
"""

import tool
import var
import mainmenu
import story
import startgame
import Gameover
import music

import Wininterface
stateDict={"mainmenu":mainmenu.Mainmenu(),
           'story':story.Story(),
           'startgame':startgame.Start(),
           'gameover':Gameover.GameOver(),
           'win':Wininterface.Wininterface()
           }
def main():
    game=tool.Game(stateDict,"mainmenu")
    #state=mainmenu.Mainmenu()
    music.music()
    game.run()

main()