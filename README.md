# Quickmath
 A program/game I made to try and make my simple math faster.

## How does it work?
Upon running the script, the user will be prompted on what the maximum value for the operands should be. After answering, the game immediately starts. The operations tested are addiition, subtraction, multiplication, and division.

Players are rewarded on speed and consecutive correct answers. The score will exponentially decay based on the length of time it takes for the player to answer, with a minimum of one point. This game also counts streaks (consecutive correct answers) and rewards the player with a score multiplier that affects the points gained from their upcoming answers:
   * <5 streak rewards nothing; points are multiplied by 1x
   * 5+ streak provides a 1.5x multiplier for points given during the duration of the streak
   * 10+ streak provides a 2x multiplier
   * 20+ streak provides a 3x multiplier

## To do:
* saving scores maybe
* maybe a gui
* more options
* a config to customize options