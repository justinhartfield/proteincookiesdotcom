/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./*.html", "./js/*.js"],
  theme: {
    extend: {
      fontFamily: {
        'anton': ['Anton', 'sans-serif'],
        'sans': ['Inter', 'sans-serif'],
      },
      colors: {
        brand: {
          50: '#fffbeb',
          100: '#fef3c7',
          500: '#f59e0b',
          600: '#d97706',
          900: '#451a03',
        },
        accent: {
          500: '#10b981',
        }
      }
    }
  },
  plugins: [],
}
