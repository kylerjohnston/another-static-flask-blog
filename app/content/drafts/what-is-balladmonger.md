title: What Balladmonger is, and how it works
date: 24 November 2015
tags:
- shakespeare
- king-lear
- markov-chains
- python
- flask

## About Balladmonger

I wrote [Balladmonger](http://github.com/kylerjohnston/balladmonger) as a project for a graduate seminar on the interactions between Shakespearian texts and early modern ballads. Its purpose was to "remediate" *King Lear* into a ballad (well, multiple ballads) and a digital media object, interrogating in the process our ideas of what a work of literature is (can we call what Balladmonger produces remediations of *King Lear*?) and destabilizing (I hope) ideas of "authority" and "authorship." You can see the implementation of Balladmonger trained on *King Lear* at [balladmonger.kylerjohnston.com](http://balladmonger.kylerjohnston.com).

![Balladmonger]({{ url_for('static', filename='img/balladmonger-screenshot.png') }})

Of course, outside the context of my seminar Balladmonger is just a program that generates poems based on some texts you feed it. It could be trained on any text file.

## How it works

Balladmonger consists of two Python packages: `printingpress`, which cleans up the source texts and then trains a Markov chain model on them, and `balladmongerer`, which generates a poem based on the model trained by `printingpress` and formats it in HTML and CSS. The initial design of Balladmonger was heavily influenced by [this post on StatsBlog](http://www.statsblogs.com/2014/02/20/how-to-fake-a-sophisticated-knowledge-of-wine-with-markov-chains/) by Tony Fischetti. 

`printingpress` makes its model by extracting all possible three-word combinations&mdash;trigrams&mdash;from the training texts and sticking them into a Python dictionary where the first two words act as a key and the third word as a value. Each key can have multiple values: every instance of a word following a particular two-word key in the training corpus is recorded as a value. So if we were training it on Taylor Swift:

> 'Cause the players gonna play, play, play, play, play
>
> And the haters gonna hate, hate, hate, hate, hate

we'd get a dictionary that would look something like:

    :::python
    ngram_dict = {
        ('cause', 'the'): ['players'],
        ('the', 'players'): ['gonna'],
        ('players', 'gonna'): ['play'],
        ('gonna', 'play'): ['play'],
        ('play', 'play'): ['play', 'play', 'play', 'and'],
        ('play', 'and'): ['the'],
        ('and', 'the'): ['haters'],
        ('the', 'haters'): ['gonna'],
        ('haters', 'gonna'): ['hate'],
        ('gonna', 'hate'): ['hate'],
        ('hate', 'hate'): ['hate', 'hate', 'hate']
    }

There's no need to calculate probabilities of, e.g., the frequency of "and" occuring after the bigram "play play" since every instance of a word following "play play" is recorded in the list. So to generate a poem, all we have to do is randomly select a key and then randomly select one item from its list of values. If we randomly select "gonna play", "play" is our only possible next value. Balladmonger then uses the last two words as a new key to select a new value. So "play play" would be our new key, and now we have a list of four possible values to randomly select from, three of which are "play" and one of which is "and".

`printingpress` does a little preprocessing on the texts, removing chapter headings and the like, and uses the [Natural Language Toolkit](http://www.nltk.org) library to try to infer where sentences end and begin before the model is generated, but essentially this is the way Balladmonger works. It's pretty simple! Of course, the poems it generates *are* pretty simple: more reminiscent of @horse_ebooks than Shakespeare. But that's what I'm going for here: any meaning you take from one of Balladmonger's poems you're going to have to make yourself. And that's not a bad thing. 

You can [check out the project on Github](http://github.com/kylerjohnston/balladmonger) to train it on your own texts and try it out for yourself.

I will have more on the literary implications of Balladmonger later.

