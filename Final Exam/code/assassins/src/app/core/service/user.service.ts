import { Injectable } from '@angular/core';
import { AngularFirestore } from '@angular/fire/firestore';
import * as firebase from 'firebase/app';

@Injectable()
export class UserService {

  constructor(public db: AngularFirestore) { }

  private currId = '';
  private modId  ='AIbu188nvXhYiTz8QwLBgYo7yWO2';

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

  getModId() {
    return this.modId;
  }

  setCurrentUserId(value) {
    this.currId = value;
  }

  initCurrentUserId() {
    this.currId = firebase.auth().currentUser.uid;
  }
}
