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

portfolio_css = Bundle('scss/portfolio/imports.scss',
                       'scss/portfolio/base.scss',
                       'scss/portfolio/layout.scss',
                       'scss/portfolio/typography.scss',
                       'scss/portfolio/window.scss',
                       filters = 'scss,cssutils',
                       output = 'gen/portfolio.css')
