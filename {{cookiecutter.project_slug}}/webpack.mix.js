const mix = require('laravel-mix')

/*
 |--------------------------------------------------------------------------
 | Mix Asset Management
 |--------------------------------------------------------------------------
 |
 | Mix provides a clean, fluent API for defining some Webpack build steps
 | for your application. By default, we are compiling the CSS file
 | for the application as well as bundling up all the JS files.
 |
 */

let staticPath = 'static'
let resourcesPath = 'resources'

// setResroucesRoots add prefix to url() in scss on example:
// from /images/close.svg to /static/images/close.svg
mix.setResourceRoot('/static')

// Path where mix-manifest.json is created.
mix.setPublicPath('static')

// if you don't need browser-sync feature you can remove this lines.
if (process.argv.includes('--browser-sync')) {
  mix.browserSync('localhost:8000')
}

// Now you can use full mix api.
mix.js(`${resourcesPath}/js/app.js`, `${staticPath}/js/`){%- if cookiecutter.use_vuejs == "y" -%}.vue(){%- endif %}
mix.postCss(`${resourcesPath}/css/app.css`, `${staticPath}/css/`, [
  require('postcss-import'),
  require('tailwindcss'),
])
