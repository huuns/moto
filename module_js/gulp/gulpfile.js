// =============================================================================
// write      : moto
// update     : 2016.10.30.
// dependency : brew / npm
//
// installation :
//
// 1. brew 설치 (http://brew.sh/linuxbrew/)
//
// apt-get install -y build-essential curl git m4 ruby texinfo libbz2-dev libcurl4-openssl-dev libexpat-dev libncurses-dev zlib1g-dev
//
// # ---> root 이외의 사용자에서 실행해야 합니다.
// ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/linuxbrew/go/install)"
//
//
// 2. nodejs 설치 (https://nodejs.org/)
//
// brew 명령어를 통해 쉽게 설치가 가능합니다.
// brew update 먼저하고
// brew install node.js
//
//
// 3. gulp 설치
// npm install gulp --save-dev
// npm install gulp-uglify --save-dev
// ...
//
//
// =============================================================================




var gulp        = require('gulp');
var uglify      = require('gulp-uglify');
var concat      = require('gulp-concat');
var jshint      = require('gulp-jshint');
var minify      = require('gulp-minify-css');
var jsminify    = require('gulp-minify');
var shell       = require('gulp-shell');
var rename      = require('gulp-rename');
var stripdebug  = require('gulp-strip-debug');
var ignore      = require('gulp-ignore');
var gutil       = require('gulp-util');

var browserSync = require('browser-sync').create();


// dependencies
//==============================================================================
var depend_js = [ 'depend/src/js/jquery/dist/*.min.js' ];
var depend_uglify_js = [
  'depend/src/js/bootstrap/dist/js/*.min*',
  'depend/src/js/jquery-cookie/*.js',
  'depend/src/js/twitter-bootstrap-wizard/*.min.js',  //modal-step
  'depend/src/js/bootstrap-select/dist/js/*.min.js',  //select
  'depend/src/js/spin.js/*.min.js',                   //progress
  'depend/src/js/blockUI/*.js',                       //progress
  'depend/src/js/*.js*'
]

var dependencies_lib_path_css = [
    'depend/src/js/bootstrap/dist/css/*.css',
    'depend/src/js/bootstrap-select/dist/css/*.css'
];

gulp.task('depend_js', function() {
    return gulp.src(depend_js)
              .pipe(gulp.dest('depend/dist/djs'));
});

gulp.task('depend_uglify_js', function() {
    return gulp.src(depend_uglify_js)
              .pipe(concat('dependencies_concat.js'))
              .pipe(gulp.dest('depend/dist/djs/'))
              .pipe(ignore.exclude([ "**/*.map" ]))
              .pipe(rename('dependencies_concat.min.js'))
              .pipe(uglify().on('error', gutil.log))
              .pipe(gulp.dest('depend/dist/djs'));
});

gulp.task('depend_css', function() {
    return gulp.src(dependencies_lib_path_css)
              .pipe(minify())
              .pipe(gulp.dest('depend/dist/dcss'));
});
//==============================================================================



// publish
//==============================================================================
var pub_lib_path_js  = [ 'DJANGO_PROJECT/static/*.js' ];
var pub_lib_path_css = [ 'DJANGO_PROJECT/static/*.css' ];

gulp.task('pub_js', function() {
    return gulp.src(pub_lib_path_js)
              .pipe(jshint())
              .pipe(jshint.reporter())
              .pipe(stripdebug())
              .pipe(concat('concat.js'))
              .pipe(gulp.dest('publish/'))
              .pipe(rename('publish_1030_v1.min.js'))
              .pipe(uglify().on('error', gutil.log))
              .pipe(gulp.dest('publish/'));
});

gulp.task('pub_css', function() {
    return gulp.src(pub_lib_path_css)
              .pipe(concat('publish_1030_v1.min.css'))
              .pipe(minify())
              .pipe(gulp.dest('publish/'));
});
//==============================================================================


gulp.task('with_django_collect', shell.task([
    'python DJANGO_PROJECT/manage.py collectstatic --noinput'
]));

gulp.task('with_django_runserver', shell.task([
    'python DJANGO_PROJECT/manage.py runserver 0.0.0.0:8000'
]));

gulp.task('browser-sync', function() {

    browserSync.init({
      notify: false,
      proxy: "localhost:8000/"
    });

    gulp.watch('./depend/**/*.*').on('change', browserSync.reload);
    gulp.watch('./DJANGO_PROJECT/**/*.js').on('change', browserSync.reload);
    gulp.watch('./DJANGO_PROJECT/**/*.py').on('change', browserSync.reload);
    gulp.watch('./DJANGO_PROJECT/**/*.css').on('change', browserSync.reload);
    gulp.watch('./DJANGO_PROJECT/**/*.html').on('change', browserSync.reload);
});

gulp.task('depend', ['depend_js', 'depend_uglify_js', 'depend_css']);
gulp.task('default', ['with_django_collect', 'with_django_runserver', 'browser-sync']);
gulp.task('publish', ['pub_js', 'pub_css']);
