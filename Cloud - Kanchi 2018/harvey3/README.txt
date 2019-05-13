# Author: Daniel Harvey

You must have Python3 installed.

Use ./<<program-name>> <<argument-list[,...]>> To run each of the programs.

client.py works for both server programs

chat room:
	run the server in the chat folder.  no arguments, will start on port 9009
	run the chat client with arguments "<server-host-ip> 9009".  you will join the chat room.  
	send messages, or Ctl+C to quit


Tic Tac Toe:
	Run the server in the tic folder with no arguments, will start on port 9009
	Run the client with arguments "<server-host-ip> 9009".  you will join the game.
	The server will send a message saying which team you joined.  all other player online will
	get a message saying that you joined and which team you are on.
	X team plays a piece first.  all other responses from the X Team are thrown out.  If you try
	to send a piece position when it isn't you're team's turn, the server will let you know that
	it isn't your turn.  Each time someone successfully places a piece, an updated game board is
	sent to all player with a message of which team placed a piece and whose turn it is now.
	If the position you're trying to play is malformed or out of bounds, the server will send you
	a message detailing what went wrong.
	If all members of one team disconnect, the remaining player are informed the the other team
	left and the game server will end.  When one team wins, the players are informed of who won,
	the final game board onfiguration is displayed and the server ends.
