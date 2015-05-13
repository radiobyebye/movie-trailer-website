Entertainment_Center.py



Entertainment_Center.py is a simple application that takes a list of Movie objects and renders an HTML page
 for viewing movie information in a browser. The webpage displays the boxart for each movie, as well as a movie summary on hover,
 and a link to display the Youtube trailer for the movie.

 

How to Run Entertainment_Center.py




The program can be run as is by opening Entertainment_Center.py in IDLE and then selecting Run -> Run Module, or by pressing F5.
Once the program is run an HTML file called fresh_tomatoes.html will be generated in the projects directory, and the program
will open the webpage in your current browser in a new tab (if possible). If you'd like you can modify Entertainment_Center.py by
inserting your own movies, removing existing movies, or appending additional movies.



Included files : 

	Entertainment_center.py - Defines instances of the class Movie, and then puts them in a list. The program then passes the list to a 	function called open_movies_page that renders the html for viewing.

	Media.py - Contains the class information for Movie, as well as a function to display the movie trailer

	Fresh_tomatoes.py - Includes the logic for rendering the html, as well as functions for formatting a list of movie objects (media.py) 
	and generating the html/opening the page in a browser (in a new tab if possible)

