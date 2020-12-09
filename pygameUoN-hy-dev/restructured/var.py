# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 17:04:31 2020

@author: 戴可昕
"""
#abstract class
import pygame
import sys
import os
WIDTH=1060
HEIGHT=546
SCREEN_SIZE=(WIDTH,HEIGHT)
speedx=5
speedy=0
frame=0
direction='right'
jumpStatus=False
jumpCooltime=0
bulletCooltime=0
bulletCoolStatus=True
directory='blue.png'
loc_old=0
Newton = 0.5

# Enemy data section
mBat1 = {'rightFrameRect': [(0 * 48, 2 * 48, 48, 48),
                            (1 * 48, 2 * 48, 48, 48),
                            (2 * 48, 2 * 48, 48, 48)],
         'leftFrameRect': [(0 * 48, 1 * 48, 48, 48),
                           (1 * 48, 1 * 48, 48, 48),
                           (2 * 48, 1 * 48, 48, 48)],
         'xLeftLimit': 567,
         'xRightLimit': 612,
         'scale': 1,
         'score': 1}

mBat2 = {'rightFrameRect': [(0 * 48, 2 * 48, 48, 48),
                            (1 * 48, 2 * 48, 48, 48),
                            (2 * 48, 2 * 48, 48, 48)],
         'leftFrameRect': [(0 * 48, 1 * 48, 48, 48),
                           (1 * 48, 1 * 48, 48, 48),
                           (2 * 48, 1 * 48, 48, 48)],
         'xLeftLimit': 800,
         'xRightLimit': 936,
         'scale': 1,
         'score': 1}

mFrog1 = {'rightFrameRect': [(3 * 48, 2 * 48, 48, 48),
                             (4 * 48, 2 * 48, 48, 48),
                             (5 * 48, 2 * 48, 48, 48)],
          'leftFrameRect': [(3 * 48, 1 * 48, 48, 48),
                            (4 * 48, 1 * 48, 48, 48),
                            (5 * 48, 1 * 48, 48, 48)],
          'xLeftLimit': 1080,
          'xRightLimit': 1171,
          'scale': 1,
          'score': 1}

mFrog2 = {'rightFrameRect': [(3 * 48, 2 * 48, 48, 48),
                             (4 * 48, 2 * 48, 48, 48),
                             (5 * 48, 2 * 48, 48, 48)],
          'leftFrameRect': [(3 * 48, 1 * 48, 48, 48),
                            (4 * 48, 1 * 48, 48, 48),
                            (5 * 48, 1 * 48, 48, 48)],
          'xLeftLimit': 1412,
          'xRightLimit': 1627,
          'scale': 1,
          'score': 1}

mGreenPig1 = {'rightFrameRect': [(6 * 48, 2 * 48, 48, 48),
                                 (7 * 48, 2 * 48, 48, 48),
                                 (8 * 48, 2 * 48, 48, 48)],
              'leftFrameRect': [(6 * 48, 1 * 48, 48, 48),
                                (7 * 48, 1 * 48, 48, 48),
                                (8 * 48, 1 * 48, 48, 48)],
              'xLeftLimit': 3884,
              'xRightLimit': 4006,
              'scale': 1,
              'score': 3}

mGreenPig2 = {'rightFrameRect': [(6 * 48, 2 * 48, 48, 48),
                                 (7 * 48, 2 * 48, 48, 48),
                                 (8 * 48, 2 * 48, 48, 48)],
              'leftFrameRect': [(6 * 48, 1 * 48, 48, 48),
                                (7 * 48, 1 * 48, 48, 48),
                                (8 * 48, 1 * 48, 48, 48)],
              'xLeftLimit': 4102,
              'xRightLimit': 4320,
              'scale': 1,
              'score': 3}

mPurpleBull1 = {'rightFrameRect': [(9 * 48, 2 * 48, 48, 48),
                                   (10 * 48, 2 * 48, 48, 48),
                                   (11 * 48, 2 * 48, 48, 48)],
                'leftFrameRect': [(9 * 48, 1 * 48, 48, 48),
                                  (10 * 48, 1 * 48, 48, 48),
                                  (11 * 48, 1 * 48, 48, 48)],
                'xLeftLimit': 1726,
                'xRightLimit': 1822,
                'scale': 1,
                'score': 3}

mPurpleBull2 = {'rightFrameRect': [(9 * 48, 2 * 48, 48, 48),
                                   (10 * 48, 2 * 48, 48, 48),
                                   (11 * 48, 2 * 48, 48, 48)],
                'leftFrameRect': [(9 * 48, 1 * 48, 48, 48),
                                  (10 * 48, 1 * 48, 48, 48),
                                  (11 * 48, 1 * 48, 48, 48)],
                'xLeftLimit': 1823,
                'xRightLimit': 1964,
                'scale': 1,
                'score': 3}

mVampire1 = {'rightFrameRect': [(0 * 48, 6 * 48, 48, 48),
                                (1 * 48, 6 * 48, 48, 48),
                                (2 * 48, 6 * 48, 48, 48)],
             'leftFrameRect': [(0 * 48, 5 * 48, 48, 48),
                               (1 * 48, 5 * 48, 48, 48),
                               (2 * 48, 5 * 48, 48, 48)],
             'xLeftLimit': 2110,
             'xRightLimit': 2490,
             'scale': 1,
             'score': 3}

mVampire2 = {'rightFrameRect': [(0 * 48, 6 * 48, 48, 48),
                                (1 * 48, 6 * 48, 48, 48),
                                (2 * 48, 6 * 48, 48, 48)],
             'leftFrameRect': [(0 * 48, 5 * 48, 48, 48),
                               (1 * 48, 5 * 48, 48, 48),
                               (2 * 48, 5 * 48, 48, 48)],
             'xLeftLimit': 2684,
             'xRightLimit': 2778,
             'scale': 1,
             'score': 3}

mVampire3 = {'rightFrameRect': [(0 * 48, 6 * 48, 48, 48),
                                (1 * 48, 6 * 48, 48, 48),
                                (2 * 48, 6 * 48, 48, 48)],
             'leftFrameRect': [(0 * 48, 5 * 48, 48, 48),
                               (1 * 48, 5 * 48, 48, 48),
                               (2 * 48, 5 * 48, 48, 48)],
             'xLeftLimit': 3164,
             'xRightLimit': 3251,
             'scale': 1,
             'score': 3}

mSkeleton1 = {'rightFrameRect': [(3 * 48, 6 * 48, 48, 48),
                                 (4 * 48, 6 * 48, 48, 48),
                                 (5 * 48, 6 * 48, 48, 48)],
              'leftFrameRect': [(3 * 48, 5 * 48, 48, 48),
                                (4 * 48, 5 * 48, 48, 48),
                                (5 * 48, 5 * 48, 48, 48)],
              'xLeftLimit': 2732,
              'xRightLimit': 3251,
              'scale': 1,
              'score': 3}

mSkeleton2 = {'rightFrameRect': [(3 * 48, 6 * 48, 48, 48),
                                 (4 * 48, 6 * 48, 48, 48),
                                 (5 * 48, 6 * 48, 48, 48)],
              'leftFrameRect': [(3 * 48, 5 * 48, 48, 48),
                                (4 * 48, 5 * 48, 48, 48),
                                (5 * 48, 5 * 48, 48, 48)],
              'xLeftLimit': 3437,
              'xRightLimit': 3790,
              'scale': 1,
              'score': 3}

mGhost1 = {'rightFrameRect': [(6 * 48, 6 * 48, 48, 48),
                              (7 * 48, 6 * 48, 48, 48),
                              (8 * 48, 6 * 48, 48, 48)],
           'leftFrameRect': [(6 * 48, 5 * 48, 48, 48),
                             (7 * 48, 5 * 48, 48, 48),
                             (8 * 48, 5 * 48, 48, 48)],
           'xLeftLimit': 4506,
           'xRightLimit': 4545,
           'scale': 1,
           'score': 5}

mGhost2 = {'rightFrameRect': [(6 * 48, 6 * 48, 48, 48),
                              (7 * 48, 6 * 48, 48, 48),
                              (8 * 48, 6 * 48, 48, 48)],
           'leftFrameRect': [(6 * 48, 5 * 48, 48, 48),
                             (7 * 48, 5 * 48, 48, 48),
                             (8 * 48, 5 * 48, 48, 48)],
           'xLeftLimit': 4640,
           'xRightLimit': 4725,
           'scale': 1,
           'score': 5}

mData = {'mBat1': mBat1,
         'mBat2': mBat2,
         'mFrog1': mFrog1,
         'mFrog2': mFrog2,
         'mGreenPig1': mGreenPig1,
         'mGreenPig2': mGreenPig2,
         'mPurpleBull1': mPurpleBull1,
         'mPurpleBull2': mPurpleBull2,
         'mVampire1': mVampire1,
         'mVampire2': mVampire2,
         'mVampire3': mVampire3,
         'mSkeleton1': mSkeleton1,
         'mSkeleton2': mSkeleton2,
         'mGhost1': mGhost1,
         'mGhost2': mGhost2}
         # 'mEndBoss': mEndBoss}

# Boss data section
bBoss = {'rightFrameRect': [(9 * 48, 6 * 48, 48, 48),
                               (10 * 48, 6 * 48, 48, 48),
                               (11 * 48, 6 * 48, 48, 48)],
         'leftFrameRect': [(9 * 48, 5 * 48, 48, 48),
                              (10 * 48, 5 * 48, 48, 48),
                              (11 * 48, 5 * 48, 48, 48)],
         'frontImage': (9 * 48, 4 * 48, 48, 48),
         'leftImage': (9 * 48, 5 * 48, 48, 48),
         'rightImage': (9 * 48, 6 * 48, 48, 48),
         'backImage': (9 * 48, 7 * 48, 48, 48),
         'xPos': 5392,
         'yPos': 157,
         'scale': 2,
         'score': 10,
         'maxHP': 10}



# Attack data section
eEarth = {'FrameRect': [
                        (0 * 192, 1 * 192, 192, 192),
                        (1 * 192, 1 * 192, 192, 192),
                        (2 * 192, 1 * 192, 192, 192),
                        (3 * 192, 1 * 192, 192, 192),
                        (4 * 192, 1 * 192, 192, 192)],
          'FrameNumber': 5,
          'FileName': 'Earth4.png'}
eMoon = {'FrameRect': [(0 * 192, 0 * 192, 192, 192),
                        (1 * 192, 0 * 192, 192, 192),
                        (2 * 192, 0 * 192, 192, 192),
                        (3 * 192, 0 * 192, 192, 192),
                        (4 * 192, 0 * 192, 192, 192),
                        ],
          'FrameNumber': 5,
          'FileName': 'eMoon.png'}
eData = {'eEarth': eEarth,
         'eMoon':eMoon}

# Boss attack data section
beEarth = {'FrameRect': [(0 * 192, 1 * 192, 192, 192),
                         (1 * 192, 1 * 192, 192, 192),
                         (2 * 192, 1 * 192, 192, 192),
                         (3 * 192, 1 * 192, 192, 192),
                         (4 * 192, 1 * 192, 192, 192)],
           'FrameNumber': 5,
           'FileName': 'Earth.png',
           'RestrictZone': (5000, 5310, 292, 292),
           'scale': (48, 48)}

beThunder = {'FrameRect': [(0 * 192, 0 * 192, 192, 192),
                           (1 * 192, 0 * 192, 192, 192),
                           (2 * 192, 0 * 192, 192, 192),
                           (3 * 192, 0 * 192, 192, 192),
                           (4 * 192, 1 * 192, 192, 192)],
             'FrameNumber': 5,
             'FileName': 'Thunder4.png',
             'RestrictZone': (5000, 5230, 0, 0),
             'scale': (120, 190)}

beClaw1 = {'FrameRect': [(0 * 192, 0 * 192, 192, 192),
                         (0 * 192, 0 * 192, 192, 192),
                         (0 * 192, 0 * 192, 192, 192),
                         (0 * 192, 0 * 192, 192, 192),
                         (0 * 192, 0 * 192, 192, 192),
                         (1 * 192, 0 * 192, 192, 192),
                         (1 * 192, 0 * 192, 192, 192),
                         (1 * 192, 0 * 192, 192, 192),
                         (1 * 192, 0 * 192, 192, 192),
                         (1 * 192, 0 * 192, 192, 192),
                         (1 * 192, 0 * 192, 192, 192),
                         (1 * 192, 0 * 192, 192, 192),
                         (2 * 192, 0 * 192, 192, 192),
                         (2 * 192, 0 * 192, 192, 192),
                         (2 * 192, 0 * 192, 192, 192),
                         (2 * 192, 0 * 192, 192, 192),
                         (2 * 192, 0 * 192, 192, 192),
                         (2 * 192, 0 * 192, 192, 192),
                         (2 * 192, 0 * 192, 192, 192),
                         (2 * 192, 0 * 192, 192, 192),
                         (3 * 192, 0 * 192, 192, 192),
                         (3 * 192, 0 * 192, 192, 192),
                         (3 * 192, 0 * 192, 192, 192),
                         (3 * 192, 0 * 192, 192, 192),
                         (3 * 192, 0 * 192, 192, 192),
                         (4 * 192, 1 * 192, 192, 192),
                         (4 * 192, 1 * 192, 192, 192),
                         (4 * 192, 1 * 192, 192, 192),
                         (4 * 192, 1 * 192, 192, 192),
                         (4 * 192, 1 * 192, 192, 192)],
           'FrameNumber': 30,
           'FileName': 'Claw.png',
           'RestrictZone': (4775, 5080, 0, 0),
           'scale': (80, 80)}

beClaw2 = {'FrameRect': [(0 * 192, 0 * 192, 192, 192),
                         (1 * 192, 0 * 192, 192, 192),
                         (2 * 192, 0 * 192, 192, 192),
                         (3 * 192, 0 * 192, 192, 192),
                         (4 * 192, 1 * 192, 192, 192)],
           'FrameNumber': 5,
           'FileName': 'Claw.png',
           'RestrictZone': (4956, 4956, 210, 210)}

beData = {'beEarth': beEarth,
          'beThunder': beThunder,
          'beClaw1': beClaw1,
          'beClaw2': beClaw2}

# Treasure data section
tCheery = {'FileName': 'I_C_Cherry.png'}
tAntidote = {'FileName': 'I_Antidote.png'}
tMedicine = {'FileName': 'P_Medicine01.png'}

tData = {'tCheery': tCheery,
         'tAntidote': tAntidote,
         'tMedicine': tMedicine}



pygame.init()
screen=pygame.display.set_mode(SCREEN_SIZE)