import { Component } from '@angular/core';

import {AuthService} from "app/utility/services/auth.service";
import {Subscription} from "rxjs/Subscription";
import 'rxjs/add/operator/share';
import { ROUTER_DIRECTIVES, Routes, Router } from '@angular/router';

@Component({
  selector: 'ng-registration',
  templateUrl: 'app/utility/components/registration.component.html',
})
export class NgRegistration {
  username: string = '';
  password: string = '';
  password2: string = '';
  errors: [any] = [];
  isLoggedIn: boolean = false;
  constructor(public authService: AuthService, private router: Router) {
    this.isLoggedIn = this.authService.isLoggedIn();
  }

  ngOnInit() {
    this.isLoggedIn = this.authService.isLoggedIn();
  }

  register(): any {
    var that = this;
    this.authService.register(this.username, this.password1, this.password2)
      .subscribe(
        data => {
          if (data.key) {
            that.authService.setToken(data.key);
            that.isLoggedIn = true;
            that.errors = [];
            that.router.navigateByUrl('/');
          }
        },
        err => {
          that.errors = JSON.parse(err._body);
        },
        () => {}
      );
  }
  token(): string{
    return this.authService.token();
  }
}
