import { Injectable } from '@angular/core';
import { AngularFirestore } from '@angular/fire/firestore';
import { UserService } from './user.service';
import * as firebase from 'firebase';

@Injectable({
  providedIn: 'root'
})
export class FirebaseService {

  db2 = firebase.firestore().collection('users');

  dbCol = this.db.collection('users');

  constructor(
    public db: AngularFirestore,
    private userService: UserService) {
  }

  getUser(userKey) {
    return this.dbCol.doc(userKey).snapshotChanges();
  }

  updateUser(userKey, value) {
    value.nameToSearch = value.name.toLowerCase();
    return this.dbCol.doc(userKey).update({
      nameToSearch: value.nameToSearch,
      name: value.name
    });
  }

  getUsers() {
    return this.dbCol.snapshotChanges();
  }

  searchUsers(searchValue) {
    return this.db.collection('users', ref => ref.where('nameToSearch', '>=', searchValue)
      .where('nameToSearch', '<=', searchValue + '\uf8ff'))
      .snapshotChanges();
  }

  createUser(value) {
    const userId = this.userService.getCurrentUserId();
    return this.dbCol.doc(userId).set({
      name: value.name,
      nameToSearch: value.name.toLowerCase(),
      email: value.email,
      target: ''
    });
  }

  startRound(value: string[]) {
    for (let i = 0; i < value.length; i++) {
      if (!(i + 1 >= value.length)) {
        this.setTarget(value[i], value[i + 1]);
      } else {
        this.setTarget(value[i], value[0]);
      }
    }
  }

  setTarget(assassin, target) {
    this.dbCol.doc(assassin).update({
      target
    });
  }

  getUserObject(value) {
    return this.db2.doc(value).get();
  }

  targetEliminated(value) {
    this.getUserObject(value).then(assassin => {
      const assassinObject = assassin.data();
      this.getUserObject(assassinObject.target).then(target => {
        const targetObject = target.data();
        if (value === targetObject.target) {
          this.setTarget(value, '');
        } else {
          this.setTarget(value, targetObject.target);
        }
        this.setTarget(assassinObject.target, '');
      });
    });
  }
}
