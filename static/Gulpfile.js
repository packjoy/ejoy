var gulp = require('gulp');
var plumber = require('gulp-plumber');
var sass = require('gulp-sass');
var cssnano = require('gulp-cssnano');
var fs = require("fs");
var inject = require('gulp-inject-string');

gulp.task('sass', function () {
    gulp.src('./css/sass/*.scss')
        .pipe(plumber())
        .pipe(sass())
        .pipe(cssnano())
        .pipe(gulp.dest('./css/dist'));
});

// gulp.task('html', function () {
// 	if(!changed) {
// 		return;
// 	}
//     var cssContent = fs.readFileSync("./css/dist/" + changed + ".css", "utf8");
//     gulp.src("../templates/" + changed + "-amp.html")
//         .pipe(inject.after('{% block custom_css %}', cssContent))
//         .pipe(gulp.dest("../templates/"));
// });


gulp.task('watch', function() {
	gulp.watch("./css/sass/*.scss", ['sass']);
});

gulp.task('default', ['watch', 'sass']);