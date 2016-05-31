import { Injectable } from '@angular/core';

import 'rxjs/Rx';
import {Observable} from "rxjs/Observable";
import {ApiService} from "./api.service";

@Injectable()
export class ImageService {
  constructor(private apiService:ApiService) {

  }

  getImages(): Observable {
    return this.apiService.get('api/images/');
  }

  createImage(data:any, files:any): Promise {
    return this.apiService.postFiles('api/images/', 'POST', data, files);
  }

}
