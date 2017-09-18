angular.module('app.controllers', [])

.controller('HomeCtrl', ['$scope', 'Products', 'Email', '$uibModal', HomeCtrl])
.controller('ShoppingCartCtrl', [ShoppingCartCtrl])
.controller('ProductsCtrl', function($scope) {
	$scope.products = [1, 2, 3, 4]
})

.controller('ContactUsCtrl', function($scope) {
	$scope.products = [1, 2, 3, 4]
})

.controller('ProductDetailsCtrl', ['$scope', 'Products', 'product', ProductDetailsCtrl]);





// CTRL functions
function HomeCtrl($scope, Products, Email, $uibModal) {
	$scope.products = Products.query();
	this.items = ['item1', 'item2', 'item3'];
	$scope.alerts = [];							// here comes the alerts
	$scope.myInterval = '10000'; 				// miliseconds for shufeling
	$scope.customer = {};						// holding customer info (email) 
	$scope.slides = [{ 
			image: null,
			text: null,
			id: 0
		}, { 
			image: '//unsplash.it/940/406',
			text: 'image 2',
			id: 1
		}, { 
			image: '//unsplash.it/940/406',
			text: 'image 3',
			id: 2
	}];



	// removing alerts by click
	$scope.closeAlert = function(index) {
		$scope.alerts.splice(index, 1);
	};


	// Joining Emal List
	$scope.joinEmailList = function(email) {
		if(email === undefined) {
			$scope.alerts.push({ type: 'danger', msg: 'The email seems to be invalid.' });
			return;
		}
		var resp = Email.save({ 'email': email });
		resp.$promise.then(function(data) {
			$scope.alerts.push({ type: 'success', msg: data.message });
		}, function(error) {
			// This is where error happens
			var error_message = error.status + ' ' + error.data.message;
			$scope.alerts.push({ type: 'danger', msg: error_message });
		});
		$scope.customer.email = '';
	};


	// Buying Product
	$scope.buyProd = function(id) {
		var modalInstance = $uibModal.open({
			animation: true,
			ariaLabelledBy: 'modal-title',
			ariaDescribedBy: 'modal-body',
			templateUrl: 'myModalContent.html',
			controller: 'ShoppingCartCtrl',
			size: 'lg',
			resolve: {
				items: function () {
					return this.items;
				}
			}
		});
		modalInstance.result.then(function (selectedItem) {
			$ctrl.selected = selectedItem;
		}, function () {
			$log.info('Modal dismissed at: ' + new Date());
		});
	};
};


function ProductDetailsCtrl($scope, Products, product) {
	console.log(product);
	$scope.product = product;
};

function ShoppingCartCtrl() {};