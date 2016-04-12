title: "How big of a truck will I need to move all my stuff?"
date: 11 April 2016
tags:
  - javascript

In a couple months I'm going to finish my Master's degree, and then I'm going to be moving cross-country. I've accumulated a lot of *stuff* over the years. I've been trying to get rid of a lot of it lately---selling off [my records](https://www.discogs.com/seller/RoddyPowers/profile) and my books and furniture I'm not going to need---but there's still enough stuff that I'm going to have to rent a truck to make the move.

The question is how big of a truck I'm going to need. Penske has a 12 ft.-truck with `450 cu. ft.` of loading space and a 16 ft.-truck with `800 cu. ft.` of loading space for the same price. Before I reserve a truck, I want to get a sense of how much stuff I'm actually moving: though they're both the same price, I'd rather drive the smaller truck cross-country if it's possible.

So I opened up Google Docs, got out a tape measure, and made a spreadsheet of the dimensions of all of the things I might want to move them. You can see the complete spreadsheet as a CSV file [here]({{ url_for('static', filename='data/moving_data.csv') }}). Geometry was never my strongest subject, but this seems like a problem easy enough to get a handle on with some simple code.

I read the CSV file into a Javascript object and wrote some quick functions to calculate the cubic footage of each item and sum a specific property in an array of objects.
    
    :::javascript
    function parseFields(data) {
      return data.map(function(i) {
        return {
          id: i.Thing,
          height: parseInt(i.Height),
          length: parseInt(i.Length),
          width: parseInt(i.Width),
          cubicFeet: cuInToCuFt(i.Height * i.Width * i.Length)
        }
      });
    }

    function cuInToCuFt(cuIn) {
      return Math.ceil(cuIn / 1728); // Round up; be conservative in our estimation
    }

    function sumProperty(prop, arr) {
      return arr.reduce(function(a, b) {
        return a + b[prop];
      }, 0);
    }

It turns out I have `370 cubic feet` of stuff. That's good! Volume-wise, it can all fit in the smaller 12 ft.-truck.

I probably won't be able to (and certainly won't want to) stack everything floor-to-ceiling in the truck, so it's a good idea to see what the total footprint of all of this stuff is too. The 12 ft.-truck has interior dimensions of `12 ft. X 6 ft. 6 in. X 6 ft. 1 in.` That makes for about `78 sq. ft.` of floor space. The 16 ft.-truck, at `16 ft. X 7 ft. 7 in. X 6 ft. 6 in.` has about `121 sq. ft.` of floor space.

I edited my map function above to calculate the square footage of all the things too.

    :::javascript hl_lines="9"
    function parseFields(data) {
      return data.map(function(i) {
        return {
          id: i.Thing,
          height: parseInt(i.Height),
          length: parseInt(i.Length),
          width: parseInt(i.Width),
          cubicFeet: cuInToCuFt(i.Height * i.Width * i.Length),
          squareFeet: sqInToSqFt(i.Width * i.Length)
        }
      });
    }

    function sqInToSqFt(sqIn) {
      return Math.ceil(sqIn / 144);
    }

If we sum that, we find our stuff has a footprint, spread in a single layer, of about `182 sq. ft.`

This is obviously an overestimation of the amount of floor space stuff will take up in the truck. I calculate floor space as `width * length`, but some of the items (mattress and box spring, for example) will be stood on end during transit, taking up a lot less space; my function also rounds up to the next square foot. Still, as a conservative estimate this works---better to end up with a truck that's a little too big than one that's a little too small.

Based on this I think I'm going to reserve the 16 ft.-truck. It is going to be a little more cumbersome to drive and use a bit more fuel, but it will be easier to load and I won't have to stack things as much and risk things falling in transit.
