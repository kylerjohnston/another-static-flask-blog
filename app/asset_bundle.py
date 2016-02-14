from flask.ext.assets import Bundle

js_all = Bundle('js/dostuff.js',
            filters = 'jsmin',
            output = 'gen/packed.js')
