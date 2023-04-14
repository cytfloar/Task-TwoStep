###This experimented is created based on 2 Step Task Money version and added the probe phase task
###This experimented was created using PsychoPy3 on Feb.15, 2023 by Serena J. Gu (RA at Columbia Center for Eating Disorders)
###Closed book test
import os
import re
from functools import partial
from psychopy import visual, core, data, logging, gui
import numpy as np
import pandas as pd
import psychopy
import csv

from twostep_library import *
import twostep_constants as c

_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

#########################Experiment Imformation########################
psychopy.useVersion('2022.2.4')
expName = '2Step2022'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '', 'spacelist': ['test1', '1', '2', '3', '4', '5']}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

#########################Saving Data File Info########################

save_filename = f"{_thisDir}/data/{expInfo['participant']}_{expInfo['date']}"
save_probename = f"{_thisDir}/data/{expInfo['participant']}_{expInfo['date']}_probe"

log_File = logging.LogFile(save_filename+'.log', level=logging.DEBUG)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

#########################Experiment Start########################
win = visual.Window([1470, 956],fullscr=True, winType='pyglet',
    monitor="testMonitor", units="height", color="#000000", colorSpace='hex',
    blendMode="avg")
win.mouseVisible = False
spacelist = f"{_thisDir}/payoff/payoff_{expInfo['spacelist']}.csv"
readsplist = pd.read_csv(spacelist)
readpraclist = pd.read_csv(f"{_thisDir}/payoff/payoff_test0.csv")
probelist = pd.read_excel("probe_alien_order.xlsx")

newBulk(partial(showInstImage, win), c.INSTRUCTION_SET_1, 3)

###Save Data###################################################
with open(f"{save_filename}.csv", 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, delimiter=',', fieldnames=["p1", "p2", "p3", "p4", 
        "trial", "key1", "rt1", "transition", "key2", "rt2", "totalgold", "winorlose"])
    writer.writeheader()
################################################################
##################### PRACTICE SESSION #########################
################################################################
    for index, row in readpraclist.iterrows():
        n_trial = 0
        bg = c.EARTH
        selectspkey = showImage(win, bg, c.ROCKETBL, c.ROCKETGR, 4.0-0.05)

        #transition
        input = 3
        def get(transprob):
          rand = np.random.rand()
          return int(rand > transprob) ^ (input - 1)
        ##transprob of getting 2 and (1 - transprob of getting 3)
        imgcenter = c.ROCKETBLDEACT

        #select spaceship 
        trans = get(0.7) #70% of getting 2 and 30% of getting 3
        if selectspkey is None:
            showSelection(win, bg, c.ROCKETBLSP, c.ROCKETGRSP, 1.0)
            continue
        elif selectspkey[0][0] == 'x': #if press x, 70% of getting 2 - purple planet
            showSelection(win, bg, c.ROCKETBLA, c.ROCKETGRDEACT, 0.5, pos_left =(0,0))
            showSelection(win, bg, c.ROCKETBLB, c.ROCKETGRDEACT, 0.5, pos_left =(0,0))
        elif selectspkey[0][0] == 'm': #if press m, 70% of getting 3 - red planet
            showSelection(win, bg, c.ROCKETBLDEACT, c.ROCKETGRA, 0.5, pos_right=(0,0))
            showSelection(win, bg, c.ROCKETBLDEACT, c.ROCKETGRB, 0.5, pos_right =(0,0))
            trans = 5 - trans
            imgcenter = c.ROCKETGRDEACT

        #transition planet
        if trans == 2: 
            bg = c.PURPLEPLANET
            probset = [row['p3'], row['p4']]
            alienset = [c.ALIENCSP, c.ALIENDSP, c.ALIENCA, c.ALIENCB, c.ALIENDA, c.ALIENDB, c.ALIENC_DEACT, c.ALIEND_DEACT]
            alkey = showImages(win, bg, c.ALIENC, c.ALIEND, imgcenter, 4.0-0.05)
        else: 
            bg = c.REDPLANET
            probset = [row['p1'], row['p2']]
            alienset = [c.ALIENASP, c.ALIENBSP, c.ALIENAA, c.ALIENAB, c.ALIENBA, c.ALIENBB, c.ALIENA_DEACT, c.ALIENB_DEACT]
            alkey = showImages(win, bg, c.ALIENA, c.ALIENB, imgcenter, 4.0-0.05)

        #select alien
        if alkey is None: 
            showSelection(win, bg, alienset[0], alienset[1], 1.0)
            continue
        elif alkey[0][0] == 'x': #selected alien 1/a OR 3/c
            alselect_de = alienset[-2]
            probs = probset[0]
            transmoney = get(probs) #probs% of getting 2 - close to 70% or 60%
            showSelection(win, bg, alienset[2], alienset[-1], 0.5, pos_left =(0,0))
            showSelection(win, bg, alienset[3], alienset[-1], 0.5, pos_left =(0,0))
        elif alkey[0][0] == 'm': #selected alien 2/b OR 4/d
            alselect_de = alienset[-1]
            probs = probset[1]
            transmoney = get(probs) #probs% of getting 2 - close to 30% or 40%
            showSelection(win, bg, alienset[-2], alienset[4], 0.5, pos_right =(0,0))
            showSelection(win, bg, alienset[-2], alienset[5], 0.5, pos_right =(0,0))

        #if there is reward
        if transmoney == 2: ##there is a reward
            showResults(win, bg, c.SPACEGOLD, alselect_de, 1.0, pos_up =(0, 0.3))
        else: ##there is no reward
            showResults(win, bg, None, alselect_de, 1.0, pos_up =(0, 0.3))

        csvrow = {
            "p1": row['p1'],
            "p2": row['p2'],
            "p3": row['p3'],
            "p4": row['p4'],
            "trial": n_trial,
            "key1": "None" if selectspkey is None else selectspkey[0][0], 
            "rt1": "None" if selectspkey is None else selectspkey[1], 
            "transition": bg, 
            "key2": "None" if alkey is None else alkey[0][0], 
            "rt2": "None" if alkey is None else alkey[1], 
            "totalgold": 0,
            "winorlose": None
        }
        n_trial += 1
        writer.writerow(csvrow)
        csvfile.flush()

    newInstruct(win, c.STARTEXP, keyList=['space'])
    ################################################################
    ###########REAL EXPERIMENT STARTS HERE##########################
    ################################################################
    totalgold = 0
    n_trial = 0
    for index, row in readsplist.iterrows():
        trialgain = 0
        n_trial += 1
        bg = c.EARTH
        selectspkey = showImage(win, bg, c.ROCKETBL, c.ROCKETGR, 4.0-0.05)

        #transition
        input = 3
        def get(transprob):
          rand = np.random.rand()
          return int(rand > transprob) ^ (input - 1)
        imgcenter = c.ROCKETBLDEACT

        #select spaceship
        trans = get(0.7)
        if selectspkey is None:
            showSelection(win, bg, c.ROCKETBLSP, c.ROCKETGRSP, 1.0)
            continue
        elif selectspkey[0][0] == 'x':
            showSelection(win, bg, c.ROCKETBLA, c.ROCKETGRDEACT, 0.5, pos_left =(0,0))
            showSelection(win, bg, c.ROCKETBLB, c.ROCKETGRDEACT, 0.5, pos_left =(0,0))
        elif selectspkey[0][0] == 'm':
            showSelection(win, bg, c.ROCKETBLDEACT, c.ROCKETGRA, 0.5, pos_right=(0,0))
            showSelection(win, bg, c.ROCKETBLDEACT, c.ROCKETGRB, 0.5, pos_right =(0,0))
            trans = 5 - trans
            imgcenter = c.ROCKETGRDEACT

        #transition planet
        if trans == 2:
            bg = c.PURPLEPLANET
            probset = [row['p3'], row['p4']]
            alienset = [c.ALIENCSP, c.ALIENDSP, c.ALIENCA, c.ALIENCB, c.ALIENDA, c.ALIENDB, c.ALIENC_DEACT, c.ALIEND_DEACT]
            alkey = showImages(win, bg, c.ALIENC, c.ALIEND, imgcenter, 4.0-0.05)
        else:
            bg = c.REDPLANET
            probset = [row['p1'], row['p2']]
            alienset = [c.ALIENASP, c.ALIENBSP, c.ALIENAA, c.ALIENAB, c.ALIENBA, c.ALIENBB, c.ALIENA_DEACT, c.ALIENB_DEACT]
            alkey = showImages(win, bg, c.ALIENA, c.ALIENB, imgcenter, 4.0-0.05)

        #select alien
        if alkey is None: 
            showSelection(win, bg, alienset[0], alienset[1], 1.0)
            continue
        elif alkey[0][0] == 'x':
            alselect_de = alienset[-2]
            probs = probset[0]
            transmoney = get(probs)
            showSelection(win, bg, alienset[2], alienset[-1], 0.5, pos_left =(0,0))
            showSelection(win, bg, alienset[3], alienset[-1], 0.5, pos_left =(0,0))
        elif alkey[0][0] == 'm':
            alselect_de = alienset[-1]
            probs = probset[1]
            transmoney = get(probs)
            showSelection(win, bg, alienset[-2], alienset[4], 0.5, pos_right =(0,0))
            showSelection(win, bg, alienset[-2], alienset[5], 0.5, pos_right =(0,0))

        #if there is reward
        if transmoney == 2:
            totalgold += 1
            trialgain = 1
            showResults(win, bg, c.SPACEGOLD, alselect_de, 1.0, pos_up =(0, 0.3))
        else:
            showResults(win, bg, None, alselect_de, 1.0, pos_up =(0, 0.3))

        #if there should be a break
        if index in [74, 149, 224]:
            newInstruct(win, c.ADDBREAK, keyList=['space'])

        csvrow = {
            "p1": row['p1'], "p2": row['p2'], "p3": row['p3'],"p4": row['p4'],
            "trial": n_trial, "key1": "None" if selectspkey is None else selectspkey[0][0], 
            "rt1": "None" if selectspkey is None else selectspkey[1], 
            "transition": bg, "key2": "None" if alkey is None else alkey[0][0], 
            "rt2": "None" if alkey is None else alkey[1], 
            "totalgold": totalgold, "winorlose": trialgain
        }
        writer.writerow(csvrow)
        csvfile.flush()

newInstruct(win, c.END%(totalgold), keyList=['space'])

################################################################
###############PROBE PHASE STARTS HERE##########################
################################################################
with open(f"{save_probename}.csv", 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, delimiter=',', fieldnames=["probela",
        "probera", "probekey","probert"])
    writer.writeheader()
    newInstruct(win, c.PROBE, keyList=['space'])
    for i in range(5):
        for index, row in probelist.iterrows():
            newCross(win)
            alienfollowup = showImage(win, None, row['probe_la'], row['probe_ra'], 3.0)
            csvrow = {
                "probela": row['probe_la'], "probera": row['probe_ra'],
                "probekey": "None" if alienfollowup is None else alienfollowup[0][0],
                "probert":  "None" if alienfollowup is None else alienfollowup[1]
            }
            writer.writerow(csvrow)
            csvfile.flush()
    newInstruct(win, c.ENDTASK, keyList=['space'])

#cleanup
win.close()
core.quit()