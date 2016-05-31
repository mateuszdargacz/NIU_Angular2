var core_1 = require('@angular/core');
var auth_service_1 = require("../services/auth.service");
var router_1 = require('@angular/router');
var NgLogin = (function () {
    function NgLogin(userService, router) {
        this.userService = userService;
        this.router = router;
        this.username = '';
        this.password = '';
        this.errors = [];
        this.isLoggedIn = false;
        this.isLoggedIn = this.userService.isLoggedIn();
    }
    NgLogin.prototype.ngOnInit = function () {
        this.isLoggedIn = this.userService.isLoggedIn();
    };
    NgLogin.prototype.login = function () {
        var that = this;
        this.userService.login(this.username, this.password)
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
    NgLogin.prototype.token = function () {
        return this.userService.token();
    };
    NgLogin = __decorate([
        core_1.Component({
            selector: 'ng-login',
            templateUrl: 'app/utility/components/login.component.html',
        }), 
        __metadata('design:paramtypes', [(typeof (_a = typeof auth_service_1.UserService !== 'undefined' && auth_service_1.UserService) === 'function' && _a) || Object, (typeof (_b = typeof router_1.Router !== 'undefined' && router_1.Router) === 'function' && _b) || Object])
    ], NgLogin);
    return NgLogin;
    var _a, _b;
})();
exports.NgLogin = NgLogin;
//# sourceMappingURL=login.component.js.map