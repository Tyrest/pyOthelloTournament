# Created for the ATCS 2019-2020 pyOthelloTournament

Uses a negamax algorithm (variant of minimax) with alpha-beta pruning. Uses multithreading for faster tree search. Evaluation method is custom-made and uses a combination of place on board and strength in patterns to determine the value of a gamestate.

GUI, game logic, and tournament hosting by Mr. Cesar.

The files in this repository are:

- othello.py - the main game engine
- board.py - all the board manipulation and information functions, some of these are useful for your Bots!
- player.py - the human and computer player classes
- ui.py - pygame GUI 
- config.py and setup.py - game-wide constants and configuration
- evaluator.pyc and minimax.pyc - compiled modules with computer player algorithms
