import { Injectable } from '@angular/core';
import { AngularFirestore } from '@angular/fire/firestore';
import * as firebase from 'firebase/app';
import { NONE_TYPE } from '@angular/compiler/src/output/output_ast';

@Injectable()
export class UserService {

  constructor(
    public db: AngularFirestore
  ) {
  }


  getCurrentUser() {
    return new Promise<any>((resolve, reject) => {
      const user = firebase.auth().onAuthStateChanged(x => {
        if (x) {
          resolve(x);
        } else {
          reject('No user logged in');
        }
      });
    });
  }


  getCurrentUserId() {
    if (firebase.auth().currentUser) {
      return firebase.auth().currentUser.uid;
    }
    return '';
  }
}
