const { src, dest, watch, series, parallel } = require('gulp');
const sass = require('gulp-sass');
const autoprefixer = require('gulp-autoprefixer');
const cssnano = require('gulp-cssnano');
const babel = require('gulp-babel');
const concat = require('gulp-concat');
const rename = require('gulp-rename');

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

function js() {
  return src('./src/js/*.js')
      .pipe(concat('main.min.js'))
      .pipe(dest('./js'));
}

exports.default = function(){
  watch('src/scss/*.scss', css)
  watch('src/js/*.js', js)
}