# Author: Daniel Harvey

You must have Python3 installed.

Use ./<<programname>> To run each of the programs.

ch9Strings.py:
	enter text and the program will sum the integers found in the input

hangman1.py:
	all files in the hangman folder.  guess the words one letter at a time, or try to guess the whole word.  win the game by gaining a score of 1000!  if your score drops below zero, you lose!   each word is worth a different number of points.  guessing the whole word counts as one try.  You get 6 tries before you lose the round.  words and sores are stored in dictionary.txt

shapes:
	all files are in the shapes folder. run the Driver.py file.  this reads in all of the shapes stored in shapes.txt and calculates the area based on herons formula for triangles, and length times width for rectangles.

RPC:
	all files in the RPC folder. the client program reads in the operations and operands found in the calculate.txt file.  IP addresses of the server host are hard coded in the client file.  port numbers are 8000 for add server and 8001 for multiply server.  the multiply server program is in the multServer.py file.  the add server program is in the addServer.py file.  run both of these servers on hosts, make sure the client has the correct host IP adresses, and the client will call the methods in the hosts to calculate the sums and products of the long integer strings.  screen shot of two servers running on two instances and client running from a third machine is included in the folder.


