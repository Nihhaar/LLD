# Design system like Cricbuzz
From [Wikipedia](https://en.wikipedia.org/wiki/Cricbuzz) -
> Cricbuzz is an Indian cricket news website owned by Times Internet. It features, news, articles and live coverage of cricket matches including videos, text commentary, player stats and team rankings. Their website also offers a mobile app.

https://www.cricbuzz.com/

## Requirements
As a cricket news app, you need to deliver:

* Scores by tournament, match, team, player - high level entities
* Upcoming, live and historic matches
* News feed

### Entities
* Tournament
  * Contains many matches
  * Schedule/Order of the matches

* Match
  * Teams - t1 and t2
  * Date and Location
  * Match type (T20, test, ...)
  * First bat or bowl (Toss)
  * Umpire
  * Aggregate Scores (Scoreboard)
  * List[Score for each bowl and over along with timestamp]
    * Bowler
    * Batsman
    * Score
  * Highlights
    * Fours, Sixes, Wicket, ...
    * Custom text
  * Commentary

* Team
  * N Players
  * Team name
  * Team splitup (7 batsmen, 4 bowlers, ...)

* Player
  * Player name
  * Player type (bowler/batsman/...)
  * Statistics
    * Fours, Sixes, ...

* Commenter
  * Commenter name
  * List of matches

* Umpire
  * Umpire name
  * List of matches

### Services
* Search Service (Search matches, tournaments, players, ...)
* Live / Historic Scoreboard Service
