import { ROUTER_DIRECTIVES, Router} from '@angular/router';
import { Component, Input } from '@angular/core';
import { AuthService} from 'app/utility/services/auth.service'
import { ImageService } from 'app/utility/services/image.service'
@Component({
  selector: 'ng-image_create',
  templateUrl: 'app/galleries/images_create.component.html',
  directives: [ROUTER_DIRECTIVES],

})
export class ImagesCreateComponent {

  constructor(private auth_service:AuthService,
              private router: Router,
              private imageService: ImageService) {
  }

  ngOnInit() {
    if(!this.auth_service.isLoggedIn()){
        this.router.navigate(['/']);
      }else{
        this.imageService.getImages().subscribe(
          (images) => {
            this.images  = images;
          }
        )
      }
  }

}
