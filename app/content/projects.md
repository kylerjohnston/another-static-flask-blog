title: Projects

Here is a running list of some things I’ve made on the internet.

sethbaker.me
------------

**Technologies**: Python, Flask, Bootstrap, SASS<br />
**Features**: Responsive design, secure login and user authentication, custom CRUD blog app<br />
**Deployment**: Ubuntu VPS with Nginx, Gunicorn, and PostgreSQL<br />
<a href="http://sethbaker.me" class="projects"><i class="fa fa-home"></i></a>

Seth is a good friend of mine running for State Senate in Portland, Maine. I developed and deployed this website to support his campaign. It features a lightweight, custom CMS, written in Flask, that can be used to create, edit, and delete blog entries.

![sethbaker.me - mobile screenshot]({{ url_for('static', filename='img/project-screenshots/sethbaker-me-screenshot.png') }})

![sethbaker.me]({{ url_for('static', filename='img/project-screenshots/sethbaker-me-screenshot2.png') }})

Today I Read...
---------------

**Technologies**: Python, Flask, jQuery, D3.js, SASS<br />
**Features**: CRUD, secure user login and authentication, RESTful API<br />
**Deployment**: Ubuntu VPS with Nginx and Gunicorn; PostgreSQL<br />
<a href="http://todayiread.xyz" class="projects"><i class="fa fa-home"></i></a> <a href="http://github.com/kylerjohnston/todayiread" class="projects"><i class="fa fa-github"></i></a>

Developed over two weekends, Today I Read... helps you keep track of your reading progress. Set goals. Track what you've read. Visualize your reading habits with sweet graphs.

I developed Today I Read... so I could keep track of the reading I was doing for school and visualize my reading habits. I used to use Goodreads to keep track of my reading, but I found that it didn't match up with the kinds of reading I did in grad school: I wasn't reading books, I was reading chapters and journal articles, and Goodreads didn't let you record those things. Today I Read... lets you track any kind of reading you want.

![Today I Read... welcome page]({{ url_for('static', filename='img/project-screenshots/todayiread-screenshot-welcome.png') }})

![Today I Read... user home page]({{ url_for('static', filename='img/project-screenshots/todayiread-screenshot-home.png') }})

![Today I Read... settings page]({{ url_for('static', filename='img/project-screenshots/todayiread-screenshot-settings.png') }})

Balladmonger
------------

**Technologies**: Python, Flask, jQuery, and Bootstrap<br />
**Features**: Responsive design, basic RESTful API<br />
**Deployment**: Heroku<br />
<a href="http://balladmonger.kylerjohnston.com" class="projects"><i class="fa fa-home"></i></a> <a href="http://github.com/kylerjohnston/balladmonger" class="projects"><i class="fa fa-github"></i></a>

Balladmonger is a small web app built with Python and Flask which dynamically generates a poem&mdash;or a “ballad”&mdash;based on one or more training texts each time the page is loaded. The instance deployed on Heroku is trained on *King Lear* and about two dozen other texts which are themselves based on *King Lear*, ranging from early modern ballads to *Sense and Sensibility* to twenty-first century fanfiction. I developed it for a seminar exploring Shakespearean remediations and the early modern ballad form. See the post [On Sitting Down to Reflect on Making Some Ballads Again]({{ url_for('main.post', post_name='sitting-down-to-reflect-on-making-some-ballads-again') }}) for more details.

![Balladmonger]({{ url_for('static', filename='img/balladmonger-screenshot.png') }})

This site
---------

**Technologies**: Python, Flask, jQuery and Javascript, HTML, CSS and SASS<br />
**Features**: Responsive design, lightweight<br />
**Deployment**: Ubuntu VPS with Nginx and Gunicorn<br />
<a href="/" class="projects"><i class="fa fa-home"></i></a> <a href="http://github.com/kylerjohnston/another-static-flask-blog" class="projects"><i class="fa fa-github"></i></a>

My goal for this project was to make a blog with a minimalist aesthetic that's really easy to manage. I think I accomplished it. All content is written in Markdown. Using Flask-Frozen, the whole site can be exported into static HTML files, or it can be routed through Flask and served using Gunicorn.


