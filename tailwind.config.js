/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './templates/home.html',
    "./node_modules/flowbite/**/*.js"
  ],
  theme: {
    extend: {},
  },
  plugins: [
    require('flowbite/plugin')
  ],
}

