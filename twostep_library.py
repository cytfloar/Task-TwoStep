from psychopy import visual, event, core
from psychopy.hardware import keyboard
from random import uniform

def get():
    rand = np.random.rand()
    return int(rand > transprob) ^ (input - 1)
def newBulk(func, configuration, length):
    for instruction in configuration:
        options = instruction[length] if len(instruction) > length else {}
        func(*instruction[:length], **options)
def newCross(win):
    cross = visual.ShapeStim(
        win=win, name='fixationcross', vertices='cross',
        size=(0.035, 0.035),
        ori=0.0, pos=(0, 0),
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
        opacity=None, depth=0.0, interpolate=True)
    cross.draw()
    win.flip()
    wait_time = uniform(0.3, 0.5)
    core.wait(wait_time)
def newImage(win, image=None, zoom=0.7, pos=(-0.3, -0.35)):
    image = visual.ImageStim(
        win=win,
        name='image', units='norm', 
        image=image, mask=None,
        ori=0, pos=pos, size=None,
        color=[1,1,1], colorSpace='rgb', opacity=1,
        flipHoriz=False, flipVert=False,
        texRes=512, interpolate=True, depth=0.0)
    sz = image.size
    image.setSize((sz[0] * zoom, sz[1] * zoom))
    return image

def newKey(keyList=None, maxWait=float('inf')):
    #print(f"newKey(keyList={keyList},maxWait={maxWait})")
    key = None
    if keyList is None:
        key = event.waitKeys(maxWait=maxWait)
    else:
        if 'escape' not in keyList:
            keyList.append('escape')
        key = event.waitKeys(keyList=keyList,maxWait=maxWait)
    if key is not None and 'escape' in key:
        core.quit()
    return key
    
def newInstruction(win, name, text, keyList=None):
    inst = newText(win, name, text)
    inst.draw()
    win.flip()
    newKey(keyList=keyList)
def newInstruct(win, text, keyList=None):
    inst = newTxt(win, text)
    inst.draw()
    win.flip()
    newKey(keyList=keyList)

def newText(win, name, text, height=0.035, pos=(0, 0.1)):
    return visual.TextStim(win=win, name=name,
        text=text, font='Arial', pos=pos, height=height, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, languageStyle='LTR', depth=0.0)
def newTxt(win, text, height=0.035, pos=(0, 0), color='white'):
    return visual.TextStim(win=win, 
        text=text, font='Arial', pos=pos, height=height, wrapWidth=None, ori=0.0, 
        color=color, colorSpace='rgb', opacity=None, languageStyle='LTR', depth=0.0)
def rtKey(keyList=None, maxWait=4.0):
    clock = core.getTime()
    key = event.waitKeys(keyList=keyList, maxWait=4.0)
    if key is not None:
        pressTime = core.getTime() - clock
    else:
        return None
    return key, pressTime
def showInstImage(win, img_left, img_right, inst, keyList=['space'], pos_left =(-0.3, -0.35), pos_right=(0.3, -0.35),zoom=0.7):
    imageleft = newImage(win, image=img_left, pos=pos_left)
    imageright = newImage(win, image=img_right, pos=pos_right)
    inst = newText(win, "inst", inst, pos=(0, 0.1))
    imageleft.draw()
    imageright.draw()
    inst.draw()
    win.flip()
    newKey(keyList=keyList)
def showImage(win, bg_img, img_left, img_right, wait_time, keyList=['x', 'm'], pos_left =(-0.3, -0.35), pos_right=(0.3, -0.35)):
    bg_img = newImage(win, image=bg_img, zoom=1.0, pos=(0,0))
    imageleft = newImage(win, image=img_left, pos=pos_left)
    imageright = newImage(win, image=img_right, pos=pos_right)
    bg_img.draw()
    imageleft.draw()
    imageright.draw()
    win.flip()
    return rtKey(keyList=keyList, maxWait=wait_time)
def showImages(win, bg_img, img_left, img_right, img_center, wait_time, keyList=['x', 'm'], pos_left =(-0.3, -0.35), pos_right=(0.3, -0.35)):
    bg_img = newImage(win, image=bg_img, zoom=1.0, pos=(0,0))
    imageleft = newImage(win, image=img_left, pos=pos_left)
    imageright = newImage(win, image=img_right, pos=pos_right)
    imagecenter = newImage(win, image=img_center, pos=(0,0))
    bg_img.draw()
    imageleft.draw()
    imageright.draw()
    imagecenter.draw()
    win.flip()
    return rtKey(keyList=keyList, maxWait=wait_time)
def showSelection(win, bg_img, img_left, img_right, wait_time, pos_left =(-0.3, -0.35), pos_right=(0.3, -0.35)):
    bg_img = newImage(win, image=bg_img, zoom=1.0, pos=(0,0))
    imageleft = newImage(win, image=img_left, pos=pos_left)
    imageright = newImage(win, image=img_right, pos=pos_right)
    bg_img.draw()
    imageleft.draw()
    imageright.draw()
    win.flip()
    core.wait(wait_time)
def showResults(win, bg_img, img_up, img_center, wait_time, pos_up =(0, 0.3)):
    bg_img = newImage(win, image=bg_img, zoom=1.0, pos=(0,0))
    imageup = newImage(win, image=img_up, pos=pos_up)
    imagecenter = newImage(win, image=img_center, pos=(0,0))
    bg_img.draw()
    imageup.draw()
    imagecenter.draw()
    win.flip()
    core.wait(wait_time)
def timedKey(keyList=None, maxWait=4.0):
    remainder = maxWait
    clock = core.getTime()
    key = event.waitKeys(keyList=keyList, maxWait=remainder)
    pressTime = float('inf')
    if key is not None:
        pressTime = core.getTime() - clock
    else:
        return None
    remainder = maxWait - pressTime
    core.wait(remainder)
    return key, pressTime