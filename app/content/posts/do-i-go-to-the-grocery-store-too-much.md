title: A story about shopping for groceries
date: 9 October 2016
tags:
  - hannaford

When I was growing up in the beatific suburbs of Connecticut, my mother would make weekly trips on Sunday to the Big Y and, occasionally, to Costco. Sometimes I would go with her. These were my introductions to grocery shopping. It rarely seemed to work well. My mother's work took her out of town three, sometimes four nights a week. Sundays she would cook dinner; the rest of the week my step-dad and I would eat leftovers, make frozen pizza, or go to Friendly's. When the next weekend came around, my mother would throw out all the rotten produce and moldy bread she'd bought the prior week before heading out for another trip to the Big Y.

It seemed wasteful. I was in high school when Michael Pollan's *Omnivore's Dilemma* and *In Defense of Food* came out. I didn't read them nor was I aware of them, as far as I remember, but I watched *Food Inc.* and Anthony Bourdain and started to really appreciate the importance of food. I wanted to learn cook. I found recipes on the internet and tutorials on YouTube and I would go to the grocery store---Stop N Shop now, because it was closer than Big Y---with lists of all the ingredients I needed to make a single a meal. I'd come home and make much more than I could ever eat. I cooked based on recipes. I didn't know how to plan meals around the ingredients I already had, so the coconut milk or the half can of chopped tomatoes I bought would be spoiled by the time I ever wanted to use it again---*if* I ever wanted to use it again.

My first semester of college I lived in a dorm and ate a lot of fast food and peanut butter sandwiches. After that semester I started commuting to school. I had a kitchen, and I drove by three grocery stores on the way to and from school. I was better at cooking by this point. I had meals I regularly cooked. I knew how to make things based on the ingredients I had on hand. But I was living alone, and I was a skinny kid (I still am). I wanted to cook with fresh produce, but fresh food spoils. If I went grocery shopping once a week, my produce would go bad before I could eat it all. So I started going to the grocery store every other day and buying just the produce and the protein I would need for the next day or two. It was a system that worked for me. The grocery store was on my way home, I was using fresh produce, and nothing was being wasted.

Two and a half years ago my girlfriend moved in with me. My grocery shopping habits perplexed her. Why are you going to the grocery store, she would ask me, when you just went two days ago? She was from a once-a-week-shopper family. I kept shopping, but I wondered if, maybe, it wasn't the most efficient system. Maybe I go to the grocery store too much.

Figuring out how often I really go to the store
-----------------------------------------------

For a little over a year, I've been keeping meticulous records of all of my spending which allows me to see exactly when, where, and how much I'm spending on groceries.

![Figure 1. Grocery purchases, 17 July 2015&ndash;7 October 2016.]({{ url_for('static', filename='img/posts/grocery_purchases.png') }})

I've taken 167 grocery trips between 17 July 2015 and 7 October 2016. 167 trips in 448 days makes for a rough average of one grocery trip every 2.6826347 days, or about every 2 days, 16 hours, and 23 minutes. For a little more accuracy, I wrote a quick Python function to calculate the average number of days between trips.

    :::python
    import datetime
    from functools import reduce

    def avg_day_difference(grocery_trips):
      # Make a list of just the dates of the grocery trips
      dates = list(map(lambda x: datetime.datetime.strptime(x['Date'], 
        '%m/%d/%Y').date(), grocery_trips))

      # Sort it in reverse chronological order, most recent date first
      dates.sort(reverse=True)
      
      # Make a list of the time differences between each transaction
      day_differences = []
      for i in range(len(dates) - 1):
          day_differences.append(dates[i] - dates[i+1])
      
      # Return the mean
      return reduce(lambda x, y: x + y, day_differences) / len(day_differences)

The slightly more accurate calculation shows I make a grocery trip, on average, every 2 days, 16 hours, and 46 minutes.

Not all of these trips are necessarily for produce or food, though. In my budget, I categorize as "grocery" any spending on consumable household stuff. That includes food, but it also includes things like toilet paper and paper towels, cleaning supplies, and bathroom supplies like toothpaste, soap, shampoo, etc. I also include alcohol in my grocery budget. In the plot below, I've included only conventional "grocery stores."

![Figure 2. Purchases from grocery stores,  17 July 2015&ndash;7 October 2016.]({{ url_for('static', filename='img/posts/grocery_store_purchases.png') }})

I've gone on 158 trips to grocery stores, averaging 2 days, 20 hours, and 29 minutes between trips. So I go every two or three days. Which is about what I thought.

Is this too much?
-----------------

According to the Food Marketing Institute, "the trade association that serves as the voice of food retail," the average U.S. consumer made 1.6 trips to the supermarket per week in 2016.[^1] So I'm going to the store more than the average consumer. Is that a bad thing? I'm not sure. It seems like it's working to me.

[^1]: ["U.S. Grocery Shopping Trends, 2016." Food Marketing Institute. Hartman Group. 2016.](http://www.fmi.org/docs/default-source/webinars/fmi-2016-us-grocery-shopper-trends-overview-webinar5ce7030324aa67249237ff0000c12749.pdf?sfvrsn=2) (pdf link)
