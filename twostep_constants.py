WELCMSG = """Welcome to the experiment!
In this task, you will see pairs of spaceships and aliens. Your job 
is to choose one of the spaceships and then one of the aliens. 
Each type of alien has a certain chance of having a piece of spacegold. Your aim is to find the alien with the highest chance 
of having spacegold, and choose it. Your goal is to win as much spacegold as possible. Press any key to continue.
"""
INSTCONT = """To select the left spaceship/alien, press the “x” key. 
To select the right spaceship/alien, press the “m” key. 
When you select an item, it will be highlighted. 
Press any key to continue.
"""

INSTCONTD = """If you take too long to make a choice, the trial will end. 
In that case, you will see red Xs on the screen and a new trial 
will start. Do not feel rushed, but please try to respond in time on every trial.
"""

INSTGOLD = """After you choose an alien, you will learn the result of your 
choice - whether you get the spacegold or not. Different aliens 
may have a higher or lower chance of having spacegold. Your 
aim is to figure out how to get as much spacegold as possible during the game.
Press any key to continue.
"""

INSTSTART = """Here is the practice section. 
Remember, your goal is to try to find the alien with spacegold. 
Press any key to continue.
"""

STARTEXP = """Now we will begin the experiment. Remember, press ‘x’ for left item and ‘m for right item.

Press any key to continue.
"""

ADDBREAK = """The task will continue after a short break. Press 'space' to continue whenever you are ready."""

PROBE = """Now we will begin the follow up experiment. The aim of this task is to select the alien in each pair which is more likely to have spacegold. This task will be played only once, without any practice. 
Again, press ‘x’ for left item and ‘m for right item.

Press any key to continue."""

END = """You have earned %d gold."""

ENDTASK = """End of experiment. Thank you for participating."""

ROCKETBL = 'image/rocket1_norm.png'
ROCKETBLA = 'image/rocket1_a1.png'
ROCKETBLB = 'image/rocket1_a2.png'
ROCKETBLDEACT= 'image/rocket1_deact.png'

ROCKETGR = 'image/rocket2_norm.png'
ROCKETGRDEACT = 'image/rocket2_deact.png'
ROCKETGRA = 'image/rocket2_a1.png'
ROCKETGRB = 'image/rocket2_a2.png'

ROCKETGRSP = 'image/rocket2_sp.png'
ROCKETBLSP = 'image/rocket1_sp.png'
PURPLEPLANET = 'image/purpleplanet.jpg'
REDPLANET = 'image/redplanet.jpg'

#background
EARTH = 'image/earth.jpg'
BLACK = 'image/black.png'

#alien image norm
ALIENA = 'image/alien1_norm.png'
ALIENB = 'image/alien2_norm.png'
ALIENC  = 'image/alien3_norm.png'
ALIEND = 'image/alien4_norm.png'

#alien image deact
ALIENA_DEACT = 'image/alien1_deact.png'
ALIENB_DEACT = 'image/alien2_deact.png'
ALIENC_DEACT = 'image/alien3_deact.png'
ALIEND_DEACT = 'image/alien4_deact.png'

#alien image with a border
ALIENAA = 'image/alien1_a1.png'
ALIENAB= 'image/alien1_a2.png'
ALIENBA = 'image/alien2_a1.png'
ALIENBB = 'image/alien2_a2.png'
ALIENCA = 'image/alien3_a1.png'
ALIENCB = 'image/alien3_a2.png'
ALIENDA = 'image/alien4_a1.png'
ALIENDB = 'image/alien4_a2.png'

#alien image with a cross 
ALIENASP = 'image/alien1_sp.png'
ALIENBSP = 'image/alien2_sp.png'
ALIENCSP = 'image/alien3_sp.png'
ALIENDSP  = 'image/alien4_sp.png'

#spacegold
SPACEGOLD = 'image/t.png'
SPACEGOLD_OLD = 'image/t_old.png'

INSTRUCTION_SET_1 = [
	(ROCKETBL, ROCKETGR, WELCMSG),
	(ROCKETBLA, ROCKETGRA, INSTCONT),
	(ROCKETBLSP, ROCKETGRSP, INSTCONTD),
	(SPACEGOLD, None, INSTGOLD, { 'pos_left': (0, -0.35)} ), # pos_left
	(None, None, INSTSTART)
]

# showInstImage(win, twostep_constants.ROCKETBL, twostep_constants.ROCKETGR, twostep_constants.WELCMSG)
# showInstImage(win, twostep_constants.ROCKETBLA, twostep_constants.ROCKETGRA, twostep_constants.INSTCONT)
# showInstImage(win, twostep_constants.ROCKETBLSP, twostep_constants.ROCKETGRSP, twostep_constants.INSTCONTD)
# showInstImage(win, twostep_constants.SPACEGOLD, None, twostep_constants.INSTGOLD, pos_left =(0, -0.35))
# showInstImage(win, None, None, twostep_constants.INSTSTART)