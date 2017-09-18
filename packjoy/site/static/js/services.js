angular.module('app.services', [])

.factory('Products', ['API', '$resource', ProductsFactory])
.factory('Email', ['API', '$resource', EmailFactory])
.factory('LocalStorage', ['$window', LocalStorageFactory]);

// Products Factory Constructor
function ProductsFactory(API, $resource) {
	return $resource(API + '/api/products/:slug');
};


// Email Factory Constructor
function EmailFactory(API, $resource) {
	return $resource(API + '/api/email');
};

function LocalStorageFactory($window) {
	return {}
};