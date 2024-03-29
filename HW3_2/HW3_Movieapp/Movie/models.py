#from django.db import models
#add 10 movies and save them
#movies_data = [
#    {"title": "Moonfall", "description": "Two former astronauts alongside a conspiracy theorist discover the hidden truth about Earth's moon when it leaves its orbit[^1^][3].", "director": "Roland Emmerich[^2^][4]", "release_year": "2022", "budget": "$138 million", "runtime": "Unknown", "rating": "Unknown", "genre": "Science Fiction"},
#    {"title": "The Meg 2: The Trench", "description": "Researchers fight for survival against massive prehistoric sea creatures and an equally predatory mining operation[^3^][18].", "director": "Unknown", "release_year": "2023", "budget": "Unknown", "runtime": "115 minutes", "rating": "PG-13", "genre": "Action"},
#    {"title": "Godzilla vs King Kong", "description": "Kong and a young girl who can communicate with him embark on a journey to find his true home, but they encounter a raging Godzilla who is being provoked by unseen forces[^4^][9].", "director": "Adam Wingard[^4^][9]", "release_year": "2021", "budget": "$155 million", "runtime": "113 minutes", "rating": "PG-13", "genre": "Action, Sci-Fi"},
#    {"title": "Terminator 2: Judgment Day", "description": "Two Terminators travel from the future to track down Sarah Connor's young son, John: One machine is programmed to kill him, the other to protect him[^5^][48].", "director": "Unknown", "release_year": "Unknown", "budget": "Unknown", "runtime": "Unknown", "rating": "Unknown", "genre": "Sci-Fi, Action"},
#    {"title": "Star Wars: Episode IV - A New Hope", "description": "Luke Skywalker joins forces with a Jedi Knight, a cocky pilot, a Wookiee and two droids to save the galaxy from the Empire's world-destroying battle station[^6^][13].", "director": "George Lucas[^7^][12]", "release_year": "1977", "budget": "Unknown", "runtime": "Unknown", "rating": "PG", "genre": "Action, Adventure, Fantasy, Science Fiction"},
#    {"title": "Spaceballs", "description": "Planet Spaceball, led by President Skroob, has wasted all of its air. Skroob schemes to steal air from the planet Druidia by kidnapping the daughter of King Roland[^8^][23].", "director": "Mel Brooks[^9^][22]", "release_year": "1987", "budget": "Unknown", "runtime": "Unknown", "rating": "Unknown", "genre": "Sci-Fi, Comedy"},
#    {"title": "The Lord of the Rings: The Two Towers", "description": "Frodo and Sam continue their journey towards Mordor to destroy the One Ring, now aided by Gollum. Merry and Pippin escape their orc captors, meet Treebeard the Ent, and help to plan an attack on Isengard[^10^][27].", "director": "Peter Jackson[^10^][27]", "release_year": "2002", "budget": "$94 million", "runtime": "179 minutes", "rating": "PG-13", "genre": "Action, Adventure, Drama, Fantasy"},
#    {"title": "Dungeons & Dragons: Honor Among Thieves", "description": "A charming thief and a band of unlikely adventurers undertake an epic heist to retrieve a lost relic, but things go dangerously awry when they run afoul of the wrong people[^11^][37].", "director": "Jonathan Goldstein, John Francis Daley[^11^][37]", "release_year": "2023", "budget": "$150 million", "runtime": "134 minutes", "rating": "PG-13", "genre": "Fantasy, Heist, Action, Comedy"},
#    {"title": "Whiplash", "description": "A promising young drummer enrolls at a cut-throat music conservatory where his dreams of greatness are mentored by an instructor who will stop at nothing to realize a student's potential[^12^][30].", "director": "Damien Chazelle[^12^][30]", "release_year": "2014", "budget": "$3.3 million", "runtime": "106 minutes", "rating": "R", "genre": "Drama, Music"},
#    {"title": "Pirates of the Caribbean: The Curse of the Black Pearl", "description": "Blacksmith Will Turner teams up with eccentric pirate \"Captain\" Jack Sparrow to save his love, the governor's daughter, from Jack's former pirate allies, who are now undead[^13^][42].", "director": "Gore Verbinski[^13^][42]", "release_year": "2003", "budget": "Unknown", "runtime": "143 minutes", "rating": "PG-13", "genre": "Action, Adventure, Fantasy"}
#]
# Create your models here.
from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    director = models.CharField(max_length=255)
    release_year = models.CharField(max_length=4, null=True, blank=True)
    budget = models.CharField(max_length=255, null=True, blank=True)
    runtime = models.CharField(max_length=255, null=True, blank=True)
    rating = models.CharField(max_length=50, null=True, blank=True)
    genre = models.CharField(max_length=255)