/*
 * Angular 2 decorators and services
 */
var core_1 = require('@angular/core');
var router_deprecated_1 = require('@angular/router-deprecated');
var app_service_1 = require('./app.service');
var home_1 = require('./home');
var router_active_1 = require('./router-active');
/*
 * App Component
 * Top Level Component
 */
var App = (function () {
    function App(appState) {
        this.appState = appState;
        this.angularclassLogo = 'assets/img/angularclass-avatar.png';
        this.loading = false;
        this.name = 'Ascii Art Generator';
    }
    App.prototype.ngOnInit = function () {
        console.log('Initial App State', this.appState.state);
    };
    App = __decorate([
        core_1.Component({
            selector: 'app',
            pipes: [],
            providers: [],
            directives: [router_active_1.RouterActive],
            encapsulation: core_1.ViewEncapsulation.None,
            styles: [
                require('./app.css'),
                require('../../node_modules/bootstrap/dist/css/bootstrap.min.css')
            ],
            templateUrl: 'app/app.component.html',
        }),
        router_deprecated_1.RouteConfig([
            { path: '/', name: 'Index', component: home_1.Home, useAsDefault: true },
            { path: '/home', name: 'Home', component: home_1.Home },
            { path: '/about', name: 'About', loader: function () { return require('es6-promise!./about')('About'); } }
        ]), 
        __metadata('design:paramtypes', [app_service_1.AppState])
    ], App);
    return App;
})();
exports.App = App;
//# sourceMappingURL=app.component.js.map