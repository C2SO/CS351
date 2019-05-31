import { Injectable } from '@angular/core';
import { AngularFirestore } from '@angular/fire/firestore';
import * as firebase from 'firebase/app';

@Injectable()
export class UserService {

  constructor(public db: AngularFirestore) { }

  private currId = '';

  getCurrentUser() {
    return new Promise<any>((resolve, reject) => {
      const user = firebase.auth().onAuthStateChanged(x => {
        if (x) {
          this.setCurrentUserId(x.uid);
          resolve(x);
        } else {
          reject('No user logged in');
        }
      });
    });
  }

  getCurrentUserId() {
    return this.currId;
  }

  setCurrentUserId(value) {
    this.currId = value;
  }
}
