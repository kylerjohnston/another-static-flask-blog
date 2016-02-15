from flask.ext.assets import Bundle

js_all = Bundle('js/dostuff.js',
            filters = 'jsmin',
            output = 'gen/packed.js')

css = Bundle('scss/base.scss',
             'css/font-awesome-4.5.0/css/font-awesome.min.css',
             filters = 'scss,cssutils,cssrewrite',
             output = 'gen/packed.css')
