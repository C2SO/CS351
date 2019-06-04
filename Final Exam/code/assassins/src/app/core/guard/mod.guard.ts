import { Injectable } from '@angular/core';
import { CanActivate, ActivatedRouteSnapshot, Router } from '@angular/router';
import { AngularFireAuth } from '@angular/fire/auth';
import { UserService } from '../service/user.service';
import { AuthService } from '../service/authentication.service';


@Injectable()
export class ModGuard implements CanActivate {

  constructor(
    public afAuth: AngularFireAuth,
    public userService: UserService,
    private router: Router,
    private authService: AuthService
  ) {}

  canActivate(): Promise<boolean> {
    return new Promise((resolve, reject) => {
      this.userService.getCurrentUser()
      .then(user => {
        if (this.userService.getCurrentUserId() === this.userService.getModId()) {
          return resolve(true);
        }
        return resolve(false);
      }, err => {
        return resolve(false);
      });
    });
  }
}
