# TwitStream
Using twitter API to generate meaningful data and present it in a digestible format.

## Dependencies
1. [Tweepy](https://github.com/tweepy/tweepy)

2. [Geopy](https://github.com/geopy/geopy)

3. [matplotlib](https://github.com/matplotlib/matplotlib)

4. [numpy](http://www.numpy.org/)

5. [Basemap](https://matplotlib.org/basemap/)

You can install 1 through 4 with

```
pip install -r requirements.txt
```
but Basemap is too big to fit in the python package index currently and requires manual installation.

You shouldn't have too much trouble finding it in any package manager.

## Instructions
1. Clone this repository wherever required.

2. Add ckey, csecret, akey, asecret in config.py. (If you don't have them yet then register your app in the [twitter developer console](https://apps.twitter.com) to receive them. You will need a twitter account with a valid mobile attached to it to use the keys.)

3. In twitstream.py you'll find a filter call with a track list in it. Change it to look for tweets with the specific filters you want.

4. Generate the locations in locations.txt by running twitstream.py.

5. These locations are used in location.py to generate your latitude and longitude in location.py.

6. Map these locations in Basemap by running visualize.py.

## Warning
Twitter allows for custom location setting which means a lot of the tweets you parse might not have a location at all or have an invalid location, these are filtered out when generating the coordinates to map, which means a lot of the tweets you parse are of no use.

I've gotten an efficiency of about ~60% (Minor edit: Over a sample of 10k tweets its close to 56%), so if you have a better way of filtering out these tweets please raise an issue to let me know. Any help to better the project would be appreciated.

## Examples
Here's a plot of news about rain being tweeted out on 27/9/17. (Sample size of about 500 tweets)
![World plot](https://github.com/gopal131072/TwitStream/blob/master/images/rain-damp.png)

Here's the part where most of the tweets were concentrated. In the southern part of the UK.
![UK plot](https://github.com/gopal131072/TwitStream/blob/master/images/rain-damp-uk.png)

And here's the weather report from the same day for the same time, courtesy of bing.
![Weather report](https://github.com/gopal131072/TwitStream/blob/master/images/rain-uk.PNG)

As you can see the plot of rain in uk coincides for the most part with the plot of the weather report. There are a few anomolies which don't affect the overall similarity of the plots.

## So what's the point of all this again?
I think social media allows for a great deal of information gathering which could prove very beneficial.
For example you could track people tweeting about fever/flu like symptoms to track the growth of a disease through a population.
This is a pretty small project right now because I'm playing around with the idea on a whim for now, but the idea has a lot of potential.

Feel free to submit issues or PR's if you'd like to help out.


