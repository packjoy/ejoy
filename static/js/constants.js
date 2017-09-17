var app = angular.module('app.constants', []);

var mapping = {
	DEV: {
		api: 'http://localhost:5000'
	},
	PROD: {
		api: 'https://SOMETHING-ELSE.COM'
	}
};

app.constant('API', mapping.DEV.api);