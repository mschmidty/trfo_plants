const { src, dest, watch, series, parallel } = require('gulp');
const sass = require('gulp-sass');
const autoprefixer = require('gulp-autoprefixer');
const cssnano = require('gulp-cssnano');

sass.compiler = require('node-sass');

function css() {
  return src('./src/scss/*.scss')
    .pipe(sass().on('error', sass.logError))
    .pipe(autoprefixer({
      overrideBrowserlist: ['last 2 versions'],
      cascade: false
    }))
    .pipe(cssnano())
    .pipe(dest('./css'))
}

exports.default = function(){
  watch('src/scss/*.scss', css)
}