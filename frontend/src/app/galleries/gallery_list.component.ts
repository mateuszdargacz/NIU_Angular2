import { ROUTER_DIRECTIVES, Router} from '@angular/router';
;
import { Component } from '@angular/core';
import { GalleryService } from "../utility/services/gallery.service";
import {AuthService} from "../utility/services/auth.service";
import {GalleryComponent} from "./gallery.component";

@Component({
  selector: 'sd-gallery-list',
  templateUrl: 'app/galleries/gallery_list.component.html',
  directives: [ROUTER_DIRECTIVES, GalleryComponent],
  providers: [GalleryService],

})
export class GalleryListComponent {
  galleries:[any] = [];
  isLoggedIn: boolean = false;

  constructor(private auth_service:AuthService,
              private router: Router,
              private galleryService: GalleryService) {

  }

  ngOnInit() {
      this.isLoggedIn = this.auth_service.isLoggedIn();
      if(!this.isLoggedIn){
        this.router.navigateByUrl('/');
      }else{
        this.galleryService.getGalleries().subscribe(
          (galleries) => {
            this.galleries  = galleries;
          }
        )
      }
  }

}
