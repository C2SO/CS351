import { Injectable } from '@angular/core';
import { AngularFireAuth } from '@angular/fire/auth';
import * as firebase from 'firebase/app';
import { UserService } from './user.service';
@Injectable()
export class AuthService {

  public loggedIn = false;

  constructor(
    public afAuth: AngularFireAuth,
    private userService: UserService
  ) {
    this.loggedIn = !!sessionStorage.getItem('user');
  }

  // Get currently logged in user from session
  getCurrentUser(): string | any {
    return sessionStorage.getItem('user') || undefined;
  }

  // The method to check whether user is logged in or not
  isLoggedIn() {
    return this.loggedIn;
  }

  doRegister(value) {
    sessionStorage.setItem('user', value.email);
    this.loggedIn = true;
    return new Promise<any>((resolve, reject) => {
      firebase.auth().createUserWithEmailAndPassword(value.email, value.password)
        .then(res => {
          this.userService.setCurrentUserId(res.user.uid);
          resolve(res);
        }, err => reject(err));
    });
  }

  doLogin(value) {
    sessionStorage.setItem('user', value.email);
    this.loggedIn = true;
    return new Promise<any>((resolve, reject) => {
      firebase.auth().signInWithEmailAndPassword(value.email, value.password)
        .then(res => {
          this.userService.setCurrentUserId(res.user.uid);
          resolve(res);
        }, err => reject(err));
    });
  }

  doLogout() {
    sessionStorage.removeItem('user');
    this.loggedIn = false;
    return new Promise((resolve, reject) => {
      if (firebase.auth().currentUser) {
        this.afAuth.auth.signOut();
        this.userService.setCurrentUserId('');
        resolve();
      } else {
        reject();
      }
    });
  }

}
