Another Static Flask Blog
=========================

This is the code I use to generate my blog, [kylerjohnston.com](http://kylerjohnston.com). It uses [Frozen-Flask](http://pythonhosted.org/Frozen-Flask/) to generate static files from a Flask app. Its design was inspired by a couple blog posts ([this one from nicolas.perriault.net](https://nicolas.perriault.net/code/2012/dead-easy-yet-powerful-static-website-generator-with-flask/), [this one by James Harding](http://www.jamesharding.ca/posts/simple-static-markdown-blog-in-flask/), and [this one by Charles Leifer](http://charlesleifer.com/blog/how-to-make-a-flask-blog-in-one-hour-or-less/)) and Miguel Grinberg’s excellent book [*Flask Web Development*](http://flaskbook.com), and my own experience with other static blog generators (Jekyll). 

**This is not intended for use as a template**. This repository reflects the code I use to publish my own website; as such it’s full of my own content and the configurations, Jinja templates, and probably other things I’m forgetting at the moment that are specific to my own needs. I’m publishing this as another example (in addition to the aforementioned blog posts) of how a static blog can be written in Flask. Use it for ideas. Fork it if you want and build off it! But you’ll have to dig around in the configurations and templates a bit to set things up for your particular needs. You’ll probably wanna clean out the `app/content/` directory, at the very least...

How it works
------------

Blog posts are written in markdown with a YAML header and stored in the `app/content/posts/` directory. Supports `title`, `date`, and `tags` YAML variables. Date must be in the format `%d %B %Y`, e.g. `01 January 2016`. A typical post would look like:

    title: A typical blog post
    date: 01 January 2016
    tags:
    - wow
    - what-a-blog
    
    Your post starts here.

I also have a couple non-blog static pages (an about page, a projects page, etc.) under `app/content/`. These are ignored by the blog post aggregator which generates the home page. They have their own routes. I designed this with blueprints to make it more modular in case I want to expand it later. The views file for the main (and currently only) blueprint is in `app/main/views.py`.

If you set the `FLASK_CONFIG` environment variable to `"drafting"`, you can put drafts in the `app/content/drafts/` and they'll be visible at http://127.0.0.1:5000/drafts/ when you run the server. Make sure to set `FLASK_CONFIG` to `"production"` before building and publishing your static pages.

The blog organizes posts in reverse order (e.g. newest first), five posts per page.

Configuration variables can be set in `config.py`.

To run the server:

    $ ./manage.py runserver

To build static pages:

    $ ./manage.py build

To run tests:
    
    $ ./manage.py test

To Do
-----

* Fork into blank template project?

License
-------

The MIT License (MIT)
Copyright (c) 2016 Kyle Johnston <kylerjohnston@gmail.com>

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
