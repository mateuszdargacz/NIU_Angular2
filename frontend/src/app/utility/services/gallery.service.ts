import { Injectable } from '@angular/core';

import 'rxjs/Rx';
import {Observable} from "rxjs/Observable";
import {ApiService} from "./api.service";

@Injectable()
export class GalleryService {
  constructor(private apiService:ApiService) {

  }

  getGalleries(): Observable {
    return this.apiService.get('api/galleries/');
  }

  createGallery(data:any, files:any): Promise {
    return this.apiService.postFiles('api/galleries/', 'POST', data, files);
  }

}
