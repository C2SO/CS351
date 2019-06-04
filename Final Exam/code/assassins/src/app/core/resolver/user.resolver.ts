import { Injectable } from '@angular/core';
import { Resolve, Router } from '@angular/router';
import { UserService } from '../service/user.service';
import { UserModel } from '../model/user.model';

@Injectable()
export class UserResolver implements Resolve<UserModel> {

    constructor(public userService: UserService, private router: Router) { }

    resolve(): Promise<UserModel> {

        const user = new UserModel();

        return new Promise((resolve, reject) => {
            this.userService.getCurrentUser()
                .then(res => {
                    if (res.providerData[0].providerId === 'password') {
                        user.name = res.displayName;
                        user.provider = res.providerData[0].providerId;
                        return resolve(user);
                    } else {
                        user.name = res.displayName;
                        user.provider = res.providerData[0].providerId;
                        return resolve(user);
                    }
                }, err => {
                    this.router.navigate(['/login']);
                    return reject(err);
                });
        });
    }
}
