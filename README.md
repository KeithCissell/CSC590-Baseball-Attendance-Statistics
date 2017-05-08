# CSC590-Baseball-Attendance-Statistics
This is a project assigned for CSC 590 - Sports Data Analytics through Missouri State University.

## Description
We are using various MLB datasets to create stoical analysis based around the attendance of a baseball game.
The data we have been working with is all recorded MLB games from 1970 - 2016 found in the sources listed at the bottom.

## Statistics Produced

### Home Game Attendance Percentage VS Home Game Winning Percentage
For this statistic we gather the winning percentage per team per year and compare it to the attendance percentage
of the same time for the same year. For each team, we only looked at home games that they played.

__Attendance percentage__ is based on the actual attendance over the year (average attendance * number of home games)
divided by the possible attendance (capacity of the ball park * number of home games).

### Team Home Game Attendance Percentage VS Home Game Winning Percentage
This is the same statistic as shown above, only we extracted the data into each team. So, each team has a plot built
to look at the correlation of attendance percentage against winning percentage for each year they played.

### Attendance Win Relation
For this statistic we looked at the relation of exceptionally high/low attendance with the win/loss outcome of the game.
We setup two global counters to use for the outcome percentage. For each team, only home games were analyzed.
- __supported__ - games with a high attendance level that resulted in a win and games with a low attendance level that resulted in a loss
- __games_amalyzed__ - total number of games with attendance outside the standard deviation

First, we get the standard deviation of the attendance level of a team for a given year.

Next, we look at each individual game for that team and year. If the attendance level for that game falls outside of the
standard deviation of attendance for that year, we add 1 to the __games_analyzed__ counter.

Then, if the attendance level was above the standard deviation and resulted in a win, we add 1 to __supported__
or if the attendance level was below the standard deviation and resulted in a loss, we add 1 to __supported__

Once we have looked at every game of every team for every year, we return:
__supported_percentage__ = __supported__ / __games_analyzed__
This percentage shows us if the attendance levels appear to help or hurt the outcome of games


What the Supported Percentage means:

Helped: if the __supported_percentage__ is well above 50%, this means that the size of the crowd helped the outcome

        (high attendance -> wins; low attendance -> losses)

Indifferent: if the __supported_percentage__ is close to 50%, this means that the size of the crowd had no effect on the outcome

Hurt: if the __supported_percentage__ is well below 50%, this means that the size of the crowd hurt the outcome of the game

        (high attendance -> losses; low attendance -> wins)

### Team Attendance Win Relation
These statistics are the same as above, but the data is analyzed per team. So, for each team we get __supported__ and
__games_analyzed__ from every game they played for each year they played.

The Helped/Indifferent/Hurt scale for the __supported_percentage__ still holds the same for a team as it does for overall.
This stat can help to see how well certain teams tend to play while under pressure.

## Data Sources
-http://www.ballparksofbaseball.com/capacity.htm
-http://www.seanlahman.com/baseball-archive/statistics/
