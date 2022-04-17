## every_enby 🖤💜🤍💛

`every_enby` is a Twitter bot that I built in my spare time, just for funsies. 

Tweets are randomly generated by pulling random words from any of the `[adjective, adverb, noun, verb].txt` files within the project. These files were generated from source files from [Princeton's WordNet](https://wordnet.princeton.edu/) project (which I wrote a [quick and dirty parser](parser.py) for). These words are then combined (using vaguely correct grammar) with either the word "enby" or "non-binary" to create funny little non-binary personas and representations. 

Tweets are sent out every 3 hours between 9AM and 9PM Eastern, using a Heroku scheduler that runs the `tweet.py` file. 

This bot was heavily inspired by [everybisexual](https://twitter.com/everybisexual) and [every_lesbian](https://twitter.com/every_lesbian). 

## Contribution 

I'm not currently looking for contributions to this project, but you're welcome to fork it and use it as inspiration for your own fun bot projects! 