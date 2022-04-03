# Overview

We created this project to help educators find fun ways to review material. We worked as a team to design a game that is customizable, fun, and competitive.

We model the software off the game show “Who Wants to be a Millionaire?” It is to be played as individuals or teams who each play the game individually and compare scores in the end. Each time a player answers a question correctly, they lock in the new monetary value (point/score). There is a timer on each question for 60 seconds each. If the player runs out of time, or they answer a question incorrectly, their game will end, with only the last locked in score preserved. Phone a friend with reveal a hint from the database if the player does not know the answer to the question.

To start the program, you must have Django installed, then inside the outer directory “millionaire” run “py manage.py runserver” and follow the link to the site.

To add more questions or edit which questions are used... 


# Development Environment

This software was written with Visual Studio Code and SQLite Studio 3.3.3.

The app was developed using Python Django and model libraries.

# Collaborators

- Brayden Jones
- Cody Mickelsen
- Tianna DeSpain tiannadespain@gmail.com

# Useful Websites

- [Youtube - CS Dojo](https://www.youtube.com/watch?v=h7rvyDK70FA&list=PLBZBJbE_rGRXBhJNdKbN7IUy-ctlOFxA1&index=2)
- [Django Documentation](https://docs.djangoproject.com/en/4.0/topics/db/models/)
- [Data Flair - Django Tutorial](https://data-flair.training/blogs/create-quiz-application-python-django/)
- [StackOverflow - JS Timer Question](https://stackoverflow.com/questions/10603409/how-to-implement-countdown-timer-in-django)
- [jsfiddle.net](https://jsfiddle.net/Mottie/sML8b/)
- [CSS Tricks](https://css-tricks.com/css-dappled-light-effect/)
- [SQlite Documentation](https://www.sqlite.org/docs.html)

# Future Work

- Add sounds using [Soundboard](https://www.soundboard.com/sb/onemilliondollars)
- Animate Lights to imitate the gameshow's wrong answer response
- Add a consequence to the timer running out
- Make app loop to allow for mulitiple teams in the same run of play
- Add 50/50 lifeline functionality
- Add limit on lifelines
