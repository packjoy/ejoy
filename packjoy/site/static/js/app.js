angular.module('app', [
	'ngAnimate',
	'ngTouch',
	'ui.router',
	'ui.bootstrap',
	'ngResource',
	'app.controllers',
	'app.services',
	'app.constants'
])

// .run(function($state) {
// 	// Doesn't seems like working
// 	$state.go('home');
// })

.config(['$qProvider', '$stateProvider', '$locationProvider', '$urlRouterProvider', function($qProvider, $stateProvider, $locationProvider, $urlRouterProvider) {
	// This is a bug fix for the new 1.6
	// angular js. Url encoding issue
	$locationProvider.hashPrefix('');

	$stateProvider
		.state('home', {
			url: "/",
			templateUrl: '../static/partials/index.html',
			controller: 'HomeCtrl'
		})
		.state('products', {
			url: "/products",
			templateUrl: '../static/partials/products.html',
			controller: 'ProductsCtrl'
		})
		.state('contactUs', {
			url: "/contact-us",
			templateUrl: '../static/partials/contact-us.html',
			controller: 'ContactUsCtrl'
		})
		.state('productDetails', {
			url: "/:prodSlug",
			templateUrl: '../static/partials/product-details.html',
			controller: 'ProductDetailsCtrl',
			resolve: {
				product: function($stateParams, Products) {
					console.log($stateParams.prodSlug);
					return Products.get({ slug: $stateParams.prodSlug });
				}
			}
		});

	$urlRouterProvider.otherwise('/');

}]);