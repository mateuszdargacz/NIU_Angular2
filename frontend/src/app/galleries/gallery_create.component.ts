import { ROUTER_DIRECTIVES, Router} from '@angular/router';
import { Component, Input } from '@angular/core';
import {GalleryService} from "../utility/services/gallery.service";

@Component({
  selector: 'sd-gallery-create',
  templateUrl: 'app/galleries/gallery_create.component.html',
  directives: [ROUTER_DIRECTIVES],
  providers: [GalleryService],
})
export class GalleryCreateComponent {
  errors:[any] = [];

  constructor(private galleryService:GalleryService, private router:Router) {
  }

  ngOnInit() {
  }

  create() {
    this.galleryService.createGallery({
        name: this.name,
        desc: this.desc,
      },
      null
    ).then(
      (success)=> {
        this.router.navigate(['./home']);
      },
      (errors) => {
        this.errors = JSON.parse(errors);
      }
    )
  }

}
