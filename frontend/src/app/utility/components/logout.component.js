var core_1 = require('@angular/core');
var user_service_1 = require("../shared/services/user.service");
var router_1 = require('@angular/router');
var LogoutComponent = (function () {
    function LogoutComponent(userService, router) {
        this.userService = userService;
        this.router = router;
        this.isLoggedIn = false;
        this.isLoggedIn = this.userService.isLoggedIn();
    }
    LogoutComponent.prototype.ngOnInit = function () {
        var _this = this;
        this.subscription = this.userService.userChanged.subscribe(function (value) {
            _this.isLoggedIn = value;
        });
    };
    LogoutComponent.prototype.ngOnDestroy = function () {
        this.subscription.unsubscribe();
    };
    LogoutComponent.prototype.logout = function () {
        this.isLoggedIn = false;
        this.userService.logout();
        this.router.navigate(['/']);
    };
    LogoutComponent = __decorate([
        core_1.Component({
            selector: 'sd-logout',
            templateUrl: 'app/components/logout.component.html',
        }), 
        __metadata('design:paramtypes', [(typeof (_a = typeof user_service_1.UserService !== 'undefined' && user_service_1.UserService) === 'function' && _a) || Object, (typeof (_b = typeof router_1.Router !== 'undefined' && router_1.Router) === 'function' && _b) || Object])
    ], LogoutComponent);
    return LogoutComponent;
    var _a, _b;
})();
exports.LogoutComponent = LogoutComponent;
//# sourceMappingURL=logout.component.js.map