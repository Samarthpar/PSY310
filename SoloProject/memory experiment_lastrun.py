#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2023.1.3),
    on November 30, 2023, at 21:02
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
prefs.hardware['audioLib'] = 'ptb'
prefs.hardware['audioLatencyMode'] = '3'
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.tools import environmenttools
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2023.1.3'
expName = 'memory experiment'  # from the Builder filename that created this script
expInfo = {
    'participant': f"{randint(0, 999999):06.0f}",
    'session': '001',
}
# --- Show participant info dialog --
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\Samarth Parmar\\OneDrive\\Documents\\PSY310- Lab in Psychology\\SoloProject\\memory experiment_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# --- Setup the Window ---
win = visual.Window(
    size=(1024, 768), fullscr=True, screen=0, 
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    backgroundImage='', backgroundFit='none',
    blendMode='avg', useFBO=True, 
    units='height')
win.mouseVisible = False
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# --- Setup input devices ---
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# --- Initialize components for Routine "welcomeScreen" ---
textWelcome = visual.TextStim(win=win, name='textWelcome',
    text='Welcome to the experiment\n',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
keyWelcome = keyboard.Keyboard()

# --- Initialize components for Routine "studyTrial" ---
textStudy = visual.TextStim(win=win, name='textStudy',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "testInstructions" ---
textInstructions = visual.TextStim(win=win, name='textInstructions',
    text='Get ready for the test',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
keyInstructions = keyboard.Keyboard()

# --- Initialize components for Routine "testTrial" ---
textTest = visual.TextStim(win=win, name='textTest',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
keyTest = keyboard.Keyboard()

# --- Initialize components for Routine "testFeedback" ---
text = visual.TextStim(win=win, name='text',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# --- Initialize components for Routine "endScreen" ---
textEnd = visual.TextStim(win=win, name='textEnd',
    text='Thanks for Participating\n',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
keyEnd = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "welcomeScreen" ---
continueRoutine = True
# update component parameters for each repeat
keyWelcome.keys = []
keyWelcome.rt = []
_keyWelcome_allKeys = []
# keep track of which components have finished
welcomeScreenComponents = [textWelcome, keyWelcome]
for thisComponent in welcomeScreenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "welcomeScreen" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *textWelcome* updates
    
    # if textWelcome is starting this frame...
    if textWelcome.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textWelcome.frameNStart = frameN  # exact frame index
        textWelcome.tStart = t  # local t and not account for scr refresh
        textWelcome.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textWelcome, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'textWelcome.started')
        # update status
        textWelcome.status = STARTED
        textWelcome.setAutoDraw(True)
    
    # if textWelcome is active this frame...
    if textWelcome.status == STARTED:
        # update params
        pass
    
    # if textWelcome is stopping this frame...
    if textWelcome.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > textWelcome.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            textWelcome.tStop = t  # not accounting for scr refresh
            textWelcome.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'textWelcome.stopped')
            # update status
            textWelcome.status = FINISHED
            textWelcome.setAutoDraw(False)
    
    # *keyWelcome* updates
    waitOnFlip = False
    
    # if keyWelcome is starting this frame...
    if keyWelcome.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        keyWelcome.frameNStart = frameN  # exact frame index
        keyWelcome.tStart = t  # local t and not account for scr refresh
        keyWelcome.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(keyWelcome, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'keyWelcome.started')
        # update status
        keyWelcome.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(keyWelcome.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(keyWelcome.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if keyWelcome.status == STARTED and not waitOnFlip:
        theseKeys = keyWelcome.getKeys(keyList=['space'], waitRelease=False)
        _keyWelcome_allKeys.extend(theseKeys)
        if len(_keyWelcome_allKeys):
            keyWelcome.keys = _keyWelcome_allKeys[-1].name  # just the last key pressed
            keyWelcome.rt = _keyWelcome_allKeys[-1].rt
            keyWelcome.duration = _keyWelcome_allKeys[-1].duration
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in welcomeScreenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "welcomeScreen" ---
for thisComponent in welcomeScreenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if keyWelcome.keys in ['', [], None]:  # No response was made
    keyWelcome.keys = None
thisExp.addData('keyWelcome.keys',keyWelcome.keys)
if keyWelcome.keys != None:  # we had a response
    thisExp.addData('keyWelcome.rt', keyWelcome.rt)
    thisExp.addData('keyWelcome.duration', keyWelcome.duration)
thisExp.nextEntry()
# the Routine "welcomeScreen" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trialsStudy = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('study_word.xlsx'),
    seed=None, name='trialsStudy')
thisExp.addLoop(trialsStudy)  # add the loop to the experiment
thisTrialsStudy = trialsStudy.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrialsStudy.rgb)
if thisTrialsStudy != None:
    for paramName in thisTrialsStudy:
        exec('{} = thisTrialsStudy[paramName]'.format(paramName))

for thisTrialsStudy in trialsStudy:
    currentLoop = trialsStudy
    # abbreviate parameter names if possible (e.g. rgb = thisTrialsStudy.rgb)
    if thisTrialsStudy != None:
        for paramName in thisTrialsStudy:
            exec('{} = thisTrialsStudy[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "studyTrial" ---
    continueRoutine = True
    # update component parameters for each repeat
    textStudy.setText(stim_word)
    # keep track of which components have finished
    studyTrialComponents = [textStudy]
    for thisComponent in studyTrialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "studyTrial" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 1.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *textStudy* updates
        
        # if textStudy is starting this frame...
        if textStudy.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textStudy.frameNStart = frameN  # exact frame index
            textStudy.tStart = t  # local t and not account for scr refresh
            textStudy.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textStudy, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'textStudy.started')
            # update status
            textStudy.status = STARTED
            textStudy.setAutoDraw(True)
        
        # if textStudy is active this frame...
        if textStudy.status == STARTED:
            # update params
            pass
        
        # if textStudy is stopping this frame...
        if textStudy.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > textStudy.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                textStudy.tStop = t  # not accounting for scr refresh
                textStudy.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'textStudy.stopped')
                # update status
                textStudy.status = FINISHED
                textStudy.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in studyTrialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "studyTrial" ---
    for thisComponent in studyTrialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-1.000000)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trialsStudy'


# --- Prepare to start Routine "testInstructions" ---
continueRoutine = True
# update component parameters for each repeat
keyInstructions.keys = []
keyInstructions.rt = []
_keyInstructions_allKeys = []
# keep track of which components have finished
testInstructionsComponents = [textInstructions, keyInstructions]
for thisComponent in testInstructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "testInstructions" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *textInstructions* updates
    
    # if textInstructions is starting this frame...
    if textInstructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textInstructions.frameNStart = frameN  # exact frame index
        textInstructions.tStart = t  # local t and not account for scr refresh
        textInstructions.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textInstructions, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'textInstructions.started')
        # update status
        textInstructions.status = STARTED
        textInstructions.setAutoDraw(True)
    
    # if textInstructions is active this frame...
    if textInstructions.status == STARTED:
        # update params
        pass
    
    # *keyInstructions* updates
    waitOnFlip = False
    
    # if keyInstructions is starting this frame...
    if keyInstructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        keyInstructions.frameNStart = frameN  # exact frame index
        keyInstructions.tStart = t  # local t and not account for scr refresh
        keyInstructions.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(keyInstructions, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'keyInstructions.started')
        # update status
        keyInstructions.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(keyInstructions.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(keyInstructions.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if keyInstructions.status == STARTED and not waitOnFlip:
        theseKeys = keyInstructions.getKeys(keyList=['space'], waitRelease=False)
        _keyInstructions_allKeys.extend(theseKeys)
        if len(_keyInstructions_allKeys):
            keyInstructions.keys = _keyInstructions_allKeys[-1].name  # just the last key pressed
            keyInstructions.rt = _keyInstructions_allKeys[-1].rt
            keyInstructions.duration = _keyInstructions_allKeys[-1].duration
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in testInstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "testInstructions" ---
for thisComponent in testInstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if keyInstructions.keys in ['', [], None]:  # No response was made
    keyInstructions.keys = None
thisExp.addData('keyInstructions.keys',keyInstructions.keys)
if keyInstructions.keys != None:  # we had a response
    thisExp.addData('keyInstructions.rt', keyInstructions.rt)
    thisExp.addData('keyInstructions.duration', keyInstructions.duration)
thisExp.nextEntry()
# the Routine "testInstructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trialsTest = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('test_word.xlsx'),
    seed=None, name='trialsTest')
thisExp.addLoop(trialsTest)  # add the loop to the experiment
thisTrialsTest = trialsTest.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrialsTest.rgb)
if thisTrialsTest != None:
    for paramName in thisTrialsTest:
        exec('{} = thisTrialsTest[paramName]'.format(paramName))

for thisTrialsTest in trialsTest:
    currentLoop = trialsTest
    # abbreviate parameter names if possible (e.g. rgb = thisTrialsTest.rgb)
    if thisTrialsTest != None:
        for paramName in thisTrialsTest:
            exec('{} = thisTrialsTest[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "testTrial" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from codeTest
    #check if our old_new statuus is old or new and assign yn_key
    if(old_new == "old" ):
        yn_key = 'y'
    else:
        yn_key = 'n'
    textTest.setText(stim_word)
    keyTest.keys = []
    keyTest.rt = []
    _keyTest_allKeys = []
    # keep track of which components have finished
    testTrialComponents = [textTest, keyTest]
    for thisComponent in testTrialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "testTrial" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *textTest* updates
        
        # if textTest is starting this frame...
        if textTest.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textTest.frameNStart = frameN  # exact frame index
            textTest.tStart = t  # local t and not account for scr refresh
            textTest.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textTest, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'textTest.started')
            # update status
            textTest.status = STARTED
            textTest.setAutoDraw(True)
        
        # if textTest is active this frame...
        if textTest.status == STARTED:
            # update params
            pass
        
        # *keyTest* updates
        waitOnFlip = False
        
        # if keyTest is starting this frame...
        if keyTest.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            keyTest.frameNStart = frameN  # exact frame index
            keyTest.tStart = t  # local t and not account for scr refresh
            keyTest.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(keyTest, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'keyTest.started')
            # update status
            keyTest.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(keyTest.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(keyTest.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if keyTest.status == STARTED and not waitOnFlip:
            theseKeys = keyTest.getKeys(keyList=['y','n'], waitRelease=False)
            _keyTest_allKeys.extend(theseKeys)
            if len(_keyTest_allKeys):
                keyTest.keys = _keyTest_allKeys[-1].name  # just the last key pressed
                keyTest.rt = _keyTest_allKeys[-1].rt
                keyTest.duration = _keyTest_allKeys[-1].duration
                # was this correct?
                if (keyTest.keys == str(yn_key)) or (keyTest.keys == yn_key):
                    keyTest.corr = 1
                else:
                    keyTest.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in testTrialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "testTrial" ---
    for thisComponent in testTrialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if keyTest.keys in ['', [], None]:  # No response was made
        keyTest.keys = None
        # was no response the correct answer?!
        if str(yn_key).lower() == 'none':
           keyTest.corr = 1;  # correct non-response
        else:
           keyTest.corr = 0;  # failed to respond (incorrectly)
    # store data for trialsTest (TrialHandler)
    trialsTest.addData('keyTest.keys',keyTest.keys)
    trialsTest.addData('keyTest.corr', keyTest.corr)
    if keyTest.keys != None:  # we had a response
        trialsTest.addData('keyTest.rt', keyTest.rt)
        trialsTest.addData('keyTest.duration', keyTest.duration)
    # the Routine "testTrial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "testFeedback" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from codeFeedback
    
    if(old_new == "old"):
        if(keyTest.corr == 1):
             feedback_text = "Congratulations! it was old and you knew"
        elif(keyTest.corr == 0):
             feedback_text = "Sorry!!! The word was old"
    else:
        if(keyTest.corr == 1):
             feedback_text = "Congratulations! You didn't get fooled"
        elif(keyTest.corr == 0):
             feedback_text = "Sorry!!! That was a new item"
        
    text.setText(feedback_text)
    # keep track of which components have finished
    testFeedbackComponents = [text]
    for thisComponent in testFeedbackComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "testFeedback" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 2.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text* updates
        
        # if text is starting this frame...
        if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text.started')
            # update status
            text.status = STARTED
            text.setAutoDraw(True)
        
        # if text is active this frame...
        if text.status == STARTED:
            # update params
            pass
        
        # if text is stopping this frame...
        if text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                text.tStop = t  # not accounting for scr refresh
                text.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text.stopped')
                # update status
                text.status = FINISHED
                text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in testFeedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "testFeedback" ---
    for thisComponent in testFeedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-2.000000)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trialsTest'


# --- Prepare to start Routine "endScreen" ---
continueRoutine = True
# update component parameters for each repeat
keyEnd.keys = []
keyEnd.rt = []
_keyEnd_allKeys = []
# keep track of which components have finished
endScreenComponents = [textEnd, keyEnd]
for thisComponent in endScreenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "endScreen" ---
routineForceEnded = not continueRoutine
while continueRoutine and routineTimer.getTime() < 10.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *textEnd* updates
    
    # if textEnd is starting this frame...
    if textEnd.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textEnd.frameNStart = frameN  # exact frame index
        textEnd.tStart = t  # local t and not account for scr refresh
        textEnd.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textEnd, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'textEnd.started')
        # update status
        textEnd.status = STARTED
        textEnd.setAutoDraw(True)
    
    # if textEnd is active this frame...
    if textEnd.status == STARTED:
        # update params
        pass
    
    # if textEnd is stopping this frame...
    if textEnd.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > textEnd.tStartRefresh + 10-frameTolerance:
            # keep track of stop time/frame for later
            textEnd.tStop = t  # not accounting for scr refresh
            textEnd.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'textEnd.stopped')
            # update status
            textEnd.status = FINISHED
            textEnd.setAutoDraw(False)
    
    # *keyEnd* updates
    waitOnFlip = False
    
    # if keyEnd is starting this frame...
    if keyEnd.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        keyEnd.frameNStart = frameN  # exact frame index
        keyEnd.tStart = t  # local t and not account for scr refresh
        keyEnd.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(keyEnd, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'keyEnd.started')
        # update status
        keyEnd.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(keyEnd.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(keyEnd.clearEvents, eventType='keyboard')  # clear events on next screen flip
    
    # if keyEnd is stopping this frame...
    if keyEnd.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > keyEnd.tStartRefresh + 10-frameTolerance:
            # keep track of stop time/frame for later
            keyEnd.tStop = t  # not accounting for scr refresh
            keyEnd.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'keyEnd.stopped')
            # update status
            keyEnd.status = FINISHED
            keyEnd.status = FINISHED
    if keyEnd.status == STARTED and not waitOnFlip:
        theseKeys = keyEnd.getKeys(keyList=['space'], waitRelease=False)
        _keyEnd_allKeys.extend(theseKeys)
        if len(_keyEnd_allKeys):
            keyEnd.keys = _keyEnd_allKeys[-1].name  # just the last key pressed
            keyEnd.rt = _keyEnd_allKeys[-1].rt
            keyEnd.duration = _keyEnd_allKeys[-1].duration
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in endScreenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "endScreen" ---
for thisComponent in endScreenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if keyEnd.keys in ['', [], None]:  # No response was made
    keyEnd.keys = None
thisExp.addData('keyEnd.keys',keyEnd.keys)
if keyEnd.keys != None:  # we had a response
    thisExp.addData('keyEnd.rt', keyEnd.rt)
    thisExp.addData('keyEnd.duration', keyEnd.duration)
thisExp.nextEntry()
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-10.000000)

# --- End experiment ---
# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
