from fanstatic import Library, Resource

library = Library('underscore.js', 'resources')
underscore = Resource(library, 'underscore.js', minified='underscore-min.js')
