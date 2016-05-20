/**
 __author__ = 'mateuszdargacz@gmail.com'
 __date__ = '5/14/16 / 4:06 PM'
 __git__ = 'https://github.com/mateuszdargacz'
 */

import {Injectable} from '@angular/core';
import {Http, Headers} from '@angular/http';
import {Observable} from "rxjs/Observable";


@Injectable()
export class ApiService {
  public api_url:string;

  constructor(private http:Http) {
    this.api_url = 'http://127.0.0.1:8000/';
  }

  token():string {
    return 'Token ' + localStorage.getItem('auth_token');
  }

  getBaseUrl():string {
    return this.api_url;
  }

  postFiles(url:string, method:string, data:any, files:any):Promise {
    return new Promise((resolve, reject) => {

      let xhr:XMLHttpRequest = new XMLHttpRequest();
      xhr.open(method, this.getBaseUrl() + url, true);
      xhr.setRequestHeader('Authorization', this.token());
      xhr.setRequestHeader('X-Requested-With', 'XMLHttpRequest');
      xhr.onreadystatechange = () => {
        if (xhr.readyState === 4) {
          if (xhr.status < 300) {
            resolve(JSON.parse(xhr.response));
          } else {
            reject(xhr.response);
          }
        }
      };

      let formData = new FormData();
      for (var file in files)
        formData.append(file, files[file], files[file].name);
      for (var value in data)
        formData.append(value, data[value]);

      xhr.send(formData);
    });
  }

  get(url):Observable {
    let headers = new Headers();
    headers.append('Authorization', this.token());
    headers.append('Content-Type', 'application/json');
    return this.http
      .get(
        this.getBaseUrl() + url,
        {headers: headers}
      )
      .map(res => res.json())
  }

}
