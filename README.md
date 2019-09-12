# Welcome to the pyOthello Tournament!

---
If you are on Mojave, then clone the mojave branch of this repository instead, using the following command:

	git clone --branch mojave https://github.com/MenloSchool-ATCS/pyOthelloTournament.git

If you are Mojave and you have already cloned the master branch of this repository, then you can run the following in terminal to move to the mojave branch:

	git checkout branch mojave
	
You may need to update your local copy of the repository first, by running:

	git pull 
---
After cloning this repository, make sure you have the pygame library installed. In terminal type:

	pip3 install pygame

Then you can run the basic game engine by typing the following in terminal, in the pyOthelloTournament repository directory:

	python3 othello.py

This will launch the GUI and you can play manually against a computer player.

When ready, copy yourname.py, and rename it to your actual name. Implement your bot, and then to test it type:

	python3 othello.py computer yourname.py

This will run the built-in computer player (as Black) versus the Bot in the file 'yourname.py' (as White). Switch the order if you want to switch who is Black (and therefore goes first). This will also generate a log file so you can see each move.

The files in this repository are:

- othello.py - the main game engine
- board.py - all the board manipulation and information functions, some of these are useful for your Bots!
- player.py - the human and computer player classes
- ui.py - pygame GUI 
- config.py and setup.py - game-wide constants and configuration
- evaluator.pyc and minimax.pyc - compiled modules with computer player algorithms
