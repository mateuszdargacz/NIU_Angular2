/**
 __author__ = 'mateuszdargacz@gmail.com'
 __date__ = '5/14/16 / 4:06 PM'
 __git__ = 'https://github.com/mateuszdargacz'
 */
var core_1 = require('@angular/core');
var http_1 = require('@angular/http');
var ApiService = (function () {
    function ApiService(http) {
        this.http = http;
        this.api_url = 'http://127.0.0.1:8000/';
    }
    ApiService.prototype.token = function () {
        return 'Token ' + localStorage.getItem('auth_token');
    };
    ApiService.prototype.getBaseUrl = function () {
        return this.api_url;
    };
    ApiService.prototype.postFiles = function (url, method, data, files) {
        var _this = this;
        return new Promise(function (resolve, reject) {
            var xhr = new XMLHttpRequest();
            xhr.open(method, _this.getBaseUrl() + url, true);
            xhr.setRequestHeader('Authorization', _this.token());
            xhr.setRequestHeader('X-Requested-With', 'XMLHttpRequest');
            xhr.onreadystatechange = function () {
                if (xhr.readyState === 4) {
                    if (xhr.status < 300) {
                        resolve(JSON.parse(xhr.response));
                    }
                    else {
                        reject(xhr.response);
                    }
                }
            };
            var formData = new FormData();
            for (var file in files)
                formData.append(file, files[file], files[file].name);
            for (var value in data)
                formData.append(value, data[value]);
            xhr.send(formData);
        });
    };
    ApiService.prototype.get = function (url) {
        var headers = new http_1.Headers();
        headers.append('Authorization', this.token());
        headers.append('Content-Type', 'application/json');
        return this.http
            .get(this.getBaseUrl() + url, { headers: headers })
            .map(function (res) { return res.json(); });
    };
    ApiService = __decorate([
        core_1.Injectable(), 
        __metadata('design:paramtypes', [(typeof (_a = typeof http_1.Http !== 'undefined' && http_1.Http) === 'function' && _a) || Object])
    ], ApiService);
    return ApiService;
    var _a;
})();
exports.ApiService = ApiService;
//# sourceMappingURL=api.service.js.map