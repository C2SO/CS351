import { Component, OnInit } from '@angular/core';
import { FirebaseService } from 'src/app/core/service/firebase.service';
import { Router } from '@angular/router';
import { UserService } from 'src/app/core/service/user.service';
import { shuffle } from 'lodash';

@Component({
  selector: 'app-manage-rounds',
  templateUrl: './manage-rounds.component.html',
  styleUrls: ['./manage-rounds.component.scss']
})
export class ManageRoundsComponent implements OnInit {

  searchValue = '';
  items: Array<any>;
  selectedOptions: string[] = [];
  nameFilteredItems: Array<any>;

  currId = '';

  constructor(
    public firebaseService: FirebaseService,
    private router: Router,
    private userService: UserService
  ) { }

  ngOnInit() {
    this.getData();
    this.currId = this.userService.getCurrentUserId();
    if (this.currId !== 'AIbu188nvXhYiTz8QwLBgYo7yWO2') {
      this.router.navigate(['user/' + this.currId]);
    }
  }

  getData() {
    this.firebaseService.getUsers()
      .subscribe(result => {
        this.items = result;
        this.nameFilteredItems = result;
      });
  }

  viewDetails(item) {
    this.router.navigate(['user/' + item.payload.doc.id]);
  }

  searchByName() {
    const value = this.searchValue.toLowerCase();
    this.firebaseService.searchUsers(value)
      .subscribe(result => {
        this.nameFilteredItems = result;
        this.items = result;
      });
  }

  startRound() {
    this.firebaseService.startRound(shuffle(this.selectedOptions));
    this.selectedOptions = [''];
  }

}
