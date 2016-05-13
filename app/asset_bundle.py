from flask.ext.assets import Bundle

js_all = Bundle('js/dostuff.js',
            filters = 'jsmin',
            output = 'gen/packed.js')

css = Bundle('scss/base.scss',
             'scss/layout.scss',
             'scss/global_style.scss',
             'scss/typography.scss',
             'scss/blog.scss',
             'scss/tag_list.scss',
             'css/font-awesome-4.5.0/css/font-awesome.min.css',
             filters = 'scss,cssutils,cssrewrite',
             output = 'gen/packed.css')

portfolio_css = Bundle('scss/portfolio/base.scss',
                       filters = 'scss,cssutils',
                       output = 'gen/portfolio.css')

resume_css = Bundle('scss/resume/base.scss',
                    filters = 'scss,cssutils',
                    depends = 'scss/resume/*.scss',
                    output = 'gen/resume.css')
