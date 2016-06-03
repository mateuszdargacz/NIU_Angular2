import { Component } from '@angular/core';

import {AuthService} from "../services/auth.service";
import {Router} from '@angular/router-deprecated';
@Component({
  selector: 'ng-login',
  templateUrl: 'app/utility/components/login.component.html',
})

export class NgLogin {
  username: string = '';
  password: string = '';
  errors: [any] = [];
  isLoggedIn: boolean = false;
  constructor(public authService: AuthService, private router: Router) {
    this.isLoggedIn = this.authService.isLoggedIn();
  }

  ngOnInit() {
    this.isLoggedIn = this.authService.isLoggedIn();
  }

  login(): any {
    var that = this;
    this.authService.login(this.username, this.password)
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
