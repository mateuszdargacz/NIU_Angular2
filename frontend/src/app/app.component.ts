/*
 * Angular 2 decorators and services
 */
import { Component, ViewEncapsulation } from '@angular/core';
import { RouteConfig, Router } from '@angular/router-deprecated';

import { AppState } from './app.service';
import { Home } from './home';
import { RouterActive } from './router-active';
import {AuthService} from "./utility/services/auth.service";
import {ApiService} from "./utility/services/api.service";
import { ROUTER_DIRECTIVES, Routes, ROUTER_PROVIDERS } from '@angular/router';
import {GalleryCreateComponent} from "./galleries/gallery_create.component";

/*
 * App Component
 * Top Level Component
 */
@Component({
  selector: 'app',
  pipes: [ ],
  providers: [AuthService, ApiService, ROUTER_PROVIDERS],
  directives: [ RouterActive ],
  encapsulation: ViewEncapsulation.None,
  styles: [
    require('./app.css'),
    require('../../node_modules/bootstrap/dist/css/bootstrap.min.css')
  ],
  templateUrl: 'app/app.component.html',

})
@RouteConfig([
  { path: '/',      name: 'Index', component: Home, useAsDefault: true },
  { path: '/create',name: 'Create', component: GalleryCreateComponent },
  { path: '/about', name: 'About', loader: () => require('es6-promise!./about')('About') }
])
export class App {
  angularclassLogo = 'assets/img/angularclass-avatar.png';
  loading = false;
  name = 'Ascii Art Generator';

  constructor(
    public appState: AppState) {

  }

  ngOnInit() {
    console.log('Initial App State', this.appState.state);
  }

}
