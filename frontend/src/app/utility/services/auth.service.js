var Observable_1 = require("rxjs/Observable");
var core_1 = require('@angular/core');
var http_1 = require('@angular/http');
var api_service_1 = require("./api.service");
var AuthService = (function () {
    function AuthService(http, restService) {
        var _this = this;
        this.http = http;
        this.restService = restService;
        this.loggedIn = false;
        this.userChanged = new core_1.EventEmitter();
        this.loggedIn = !!localStorage.getItem('auth_token');
        this.userChanged = new Observable_1.Observable(function (observer) { return _this._observer = observer; }).share();
    }
    AuthService.prototype.login = function (username, password) {
        var headers = new http_1.Headers();
        headers.append('Content-Type', 'application/json');
        return this.http
            .post(this.restService.getBaseUrl() + 'rest-auth/login/', JSON.stringify({ username: username, password: password }), { headers: headers })
            .map(function (res) { return res.json(); });
    };
    AuthService.prototype.register = function (username, password1, password2) {
        var headers = new http_1.Headers();
        headers.append('Content-Type', 'application/json');
        return this.http
            .post(this.restService.getBaseUrl() + 'rest-auth/registration/', JSON.stringify({ username: username, password1: password1, password2: password2 }), { headers: headers })
            .map(function (res) { return res.json(); });
    };
    AuthService.prototype.setToken = function (token) {
        localStorage.setItem('auth_token', token);
        this._observer.next(true);
        this.loggedIn = true;
    };
    AuthService.prototype.token = function () {
        return 'Token ' + localStorage.getItem('auth_token');
    };
    AuthService.prototype.logout = function () {
        localStorage.removeItem('auth_token');
        this._observer.next(false);
        this.loggedIn = false;
    };
    AuthService.prototype.isLoggedIn = function () {
        return localStorage.getItem('auth_token');
    };
    AuthService = __decorate([
        core_1.Injectable(), 
        __metadata('design:paramtypes', [(typeof (_a = typeof http_1.Http !== 'undefined' && http_1.Http) === 'function' && _a) || Object, api_service_1.ApiService])
    ], AuthService);
    return AuthService;
    var _a;
})();
exports.AuthService = AuthService;
//# sourceMappingURL=auth.service.js.map