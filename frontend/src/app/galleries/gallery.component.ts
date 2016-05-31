import { ROUTER_DIRECTIVES, Router} from '@angular/router';
import { Component, Input } from '@angular/core';
import { AuthService} from 'app/utility/services/auth.service'
@Component({
  selector: 'sd-gallery',
  templateUrl: 'app/galleries/gallery.component.html',
  directives: [ROUTER_DIRECTIVES],

})
export class GalleryComponent {
  @Input() gallery;

  constructor(public authService: AuthService) {
  }

  ngOnInit() {
  }

}
