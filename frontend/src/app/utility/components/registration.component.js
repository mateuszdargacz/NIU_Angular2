var core_1 = require('@angular/core');
var user_service_1 = require("../shared/services/user.service");
var router_1 = require('@angular/router');
var RegisterComponent = (function () {
    function RegisterComponent(userService, router) {
        this.userService = userService;
        this.router = router;
        this.username = '';
        this.password = '';
        this.password2 = '';
        this.errors = [];
        this.isLoggedIn = false;
        this.isLoggedIn = this.userService.isLoggedIn();
    }
    RegisterComponent.prototype.ngOnInit = function () {
        this.isLoggedIn = this.userService.isLoggedIn();
    };
    RegisterComponent.prototype.register = function () {
        var that = this;
        this.userService.register(this.username, this.password1, this.password2)
            .subscribe(function (data) {
            if (data.key) {
                that.userService.setToken(data.key);
                that.isLoggedIn = true;
                that.errors = [];
                that.router.navigate(['/mosaic']);
            }
        }, function (err) {
            that.errors = JSON.parse(err._body);
        }, function () { });
    };
    RegisterComponent.prototype.token = function () {
        return this.userService.token();
    };
    RegisterComponent = __decorate([
        core_1.Component({
            selector: 'ng-registration',
            templateUrl: 'app/utility/components/registration.component.html',
        }), 
        __metadata('design:paramtypes', [(typeof (_a = typeof user_service_1.UserService !== 'undefined' && user_service_1.UserService) === 'function' && _a) || Object, (typeof (_b = typeof router_1.Router !== 'undefined' && router_1.Router) === 'function' && _b) || Object])
    ], RegisterComponent);
    return RegisterComponent;
    var _a, _b;
})();
exports.RegisterComponent = RegisterComponent;
//# sourceMappingURL=registration.component.js.map