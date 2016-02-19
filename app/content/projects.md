title: Projects

Here are some things I’ve made on the internet.

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

**Technologies**: Python, Flask, jQuery and Javascript, HTML, CSS and SCSS<br />
**Features**: Responsive design, lightweight<br />
**Deployment**: Ubuntu VPS with Nginx and Gunicorn<br />
<a href="/" class="projects"><i class="fa fa-home"></i></a> <a href="http://github.com/kylerjohnston/another-static-flask-blog" class="projects"><i class="fa fa-github"></i></a>

My goal for this project was to make a blog with a minimalist aesthetic that's really easy to manage. I think I accomplished it. All content is written in Markdown. Using Flask-Frozen, the whole site can be exported into static HTML files, or it can be routed through Flask and served using Gunicorn.

sethbaker.me
------------

**Technologies**: Python, Flask, Bootstrap<br />
**Features**: Responsive design<br />
**Deployment**: Shared hosting<br />
<a href="http://sethbaker.me" class="projects"><i class="fa fa-home"></i></a>

Seth is a good friend of mine running for State Senate in Portland, Maine. I made this website to support his campaign. It has static content about his platform and links to donate on Paypal. I used Flask-Frozen to generate static HTML pages to upload on shared hosting.

![sethbaker.me]({{ url_for('static', filename='img/project-screenshots/sethbaker-me-screenshot.png') }})
