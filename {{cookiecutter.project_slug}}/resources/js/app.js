window._ = require('lodash')
{%+ if cookiecutter.use_vuejs == "y" %}
/**
 * We'll load the axios HTTP library which allows us to easily issue requests
 * to our Django back-end.
 */

window.axios = require('axios')

window.axios.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest'

/**
 * Next, we will load the fresh Vue application instance to the index html page.
 */
require('../vue/main')
{%- endif %}
