import { Injectable } from '@angular/core';
import { Resolve, ActivatedRouteSnapshot, ActivatedRoute } from '@angular/router';
import { FirebaseService } from '../service/firebase.service';

@Injectable()
export class EditUserResolver implements Resolve<any> {

  constructor(public firebaseService: FirebaseService) { }

  resolve(route: ActivatedRouteSnapshot) {

    return new Promise((resolve, reject) => {
      const userId = route.paramMap.get('id');
      this.firebaseService.getUserResolver(userId)
      .subscribe(
        data => {
          resolve(data);
        }
      );
    });
  }
}
