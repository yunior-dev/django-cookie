const defaultTheme = require('tailwindcss/defaultTheme')
/*
 |--------------------------------------------------------------------------
 | Tailwind CSS config file.
 | https://tailwindcss.com/docs
 |--------------------------------------------------------------------------
 */

module.exports = {
  purge: [
    './templates/**/*.html',
    {%- if cookiecutter.use_vuejs == "y" %}
    './resources/vue/**/*.vue'
    {%- endif %}
  ],
  darkMode: false, // or 'media' or 'class'
  theme: {
    extend: {
      fontFamily: {
        sans: ['Inter var', ...defaultTheme.fontFamily.sans],
      },
    },
  },
  variants: {
    extend: {},
  },
  plugins: [],
}
