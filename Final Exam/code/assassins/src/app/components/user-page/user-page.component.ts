import { Component, OnInit } from '@angular/core';
import { FirebaseService } from 'src/app/core/service/firebase.service';
import { Router } from '@angular/router';
import { UserService } from 'src/app/core/service/user.service';

@Component({
  selector: 'app-user-page',
  templateUrl: './user-page.component.html',
  styleUrls: ['./user-page.component.scss']
})
export class UserPageComponent implements OnInit {

  searchValue: string = '';
  items: Array<any>;
  name_filtered_items: Array<any>;

  currId: string = '';

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
        this.name_filtered_items = result;
      })
  }

  viewDetails(item) {
    this.router.navigate(['user/' + item.payload.doc.id]);
  }

  searchByName() {
    let value = this.searchValue.toLowerCase();
    this.firebaseService.searchUsers(value)
      .subscribe(result => {
        this.name_filtered_items = result;
        this.items = result;
      })
  }

}