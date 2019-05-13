# Author: Daniel Harvey

You must have Python3 installed.

Use ./<<program-name>> <<argument-list[,...]>> To run each of the programs.

Books for demo run are Emma and Pride and Prejudice by Jane Austen @ URLs
http://www.gutenberg.org/files/158/158-0.txt
http://www.gutenberg.org/cache/epub/42671/pg42671.txt


torrent.py:
	run this program first.  no arguments required.  the program will accept two clients
	and introduce them to each other.  the program must be killed and restarted to accept
	a new batch of clients.


peer.py:
	run this program with two arguments: torrent host and the url of the utf-8 book to 
	fetch and analyze.  the first peer to run will be assigned the server role and be 
	responsible for listening to the other peer.  the second peer will be assigned the 
	passive client role and be responsible for connecting to the server peer.  they will
	both analyze their books and then share their results with each other, and print
	the results of the intersected word frequencies data set to the console.  the programs
	should work locally and across different machine (as long as the public ip forwards the
	ports correctly).  the word frequency counting splits words on whitespace and em-dashes.
	any surrounding punctuation for a word is removed in the sanitization process (for instances
	of word: or word?" or "word. etc).  
