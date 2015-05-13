import media
import fresh_tomatoes

#The following code creates 6 instances of the Movie class (media.py). 
fear_loathing = media.Movie("Fear and Loathing in Las Vegas",
                            "Raoul Duke (Johnny Depp) and his attorney Dr. Gonzo (Benicio Del Toro) drive a red convertible across the Mojave desert to Las Vegas with a suitcase full of drugs to cover a motorcycle race",
                            "http://www.gstatic.com/tv/thumb/movieposters/20996/p20996_p_v7_aa.jpg",
                            "https://www.youtube.com/watch?v=_d0hEzXrWT4",
                            "1998")

donnie_darko = media.Movie("Donnie Darko",
                           "In a funny, moving and distinctly mind-bending journey through suburban America, one extraordinary but disenchanted teenager is about to take Time's Arrow for a ride",
                           "http://fr.web.img4.acsta.net/medias/nmedia/00/02/38/60/darko.jpg",
                           "https://www.youtube.com/watch?v=ZZyBaFYFySk",
                           "2001")

the_wrestler = media.Movie("The Wrestler",
                           "Aging wrestler Randy The Ram Robinson (Mickey Rourke) is long past his prime but still ready and rarin' to go on the pro-wrestling circuit",
                           "http://www.scriptmag.com/wp-content/uploads/the-wrestler.png",
                           "https://www.youtube.com/watch?v=61-GFxjTyV0",
                           "2008")

twentyone_jumpstreet = media.Movie("21 Jump Street",
                                  "When cops Schmidt (Jonah Hill) and Jenko (Channing Tatum) join the secret Jump Street unit, they use their youthful appearances to go under cover as high-school students",
                                   "http://ia.media-imdb.com/images/M/MV5BMTc3NzQ3OTg3NF5BMl5BanBnXkFtZTcwMjk5OTcxNw@@._V1_SX640_SY720_.jpg",
                                   "https://www.youtube.com/watch?v=ISJR4rVO0TQ",
                                   "2012")

hackers = media.Movie("Hackers",
                      "A teenage hacker finds himself framed for the theft of millions of dollars from a major corporation",
                      "http://www.gstatic.com/tv/thumb/movieposters/17164/p17164_p_v7_aa.jpg",
                      "https://www.youtube.com/watch?v=Ql1uLyuWra8",
                      "1995")

lego_movie = media.Movie("The Lego Movie",
                         "Emmet (Chris Pratt), an ordinary LEGO figurine who always follows the rules, is mistakenly identified as the Special -- an extraordinary being and the key to saving the world",
                         "http://ia.media-imdb.com/images/M/MV5BMTg4MDk1ODExN15BMl5BanBnXkFtZTgwNzIyNjg3MDE@._V1_SY1200_CR90,0,630,1200_AL_.jpg",
                         "https://www.youtube.com/watch?v=fZ_JOBCLF-I",
                         "2014")


movies = [the_wrestler,twentyone_jumpstreet,fear_loathing,donnie_darko,hackers,lego_movie]  #Add the Movie objects to the movies list


fresh_tomatoes.open_movies_page(movies)  #Pass the movies list to open_movies_page, which will render and output the html for our webpage
                      

                                   
