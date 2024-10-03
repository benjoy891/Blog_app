/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './templates/**/*.html',  // Scans all HTML files inside the templates folder and its subdirectories
    './static/**/*.js',       // Adjust for JS files if needed
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}
