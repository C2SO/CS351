import { Component, OnInit } from '@angular/core';
import { FirebaseService } from 'src/app/core/service/firebase.service';
import { Router } from '@angular/router';
import { UserService } from 'src/app/core/service/user.service';
import { AuthService } from 'src/app/core/service/authentication.service';

@Component({
  selector: 'app-user-page',
  templateUrl: './user-page.component.html',
  styleUrls: ['./user-page.component.scss']
})
export class UserPageComponent implements OnInit {

  searchValue = '';
  items: Array<any>;
  nameFilteredItems: Array<any>;

  currId = '';

  constructor(
    public firebaseService: FirebaseService,
    private router: Router,
    public auth: AuthService,
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

  searchByName() {
    const value = this.searchValue.toLowerCase();
    this.firebaseService.searchUsers(value)
      .subscribe(result => {
        this.nameFilteredItems = result;
        this.items = result;
      });
  }

  viewDetails(item) {
    this.router.navigate(['user/' + item.payload.doc.id]);
  }

  targetEliminated(item) {
    this.firebaseService.targetEliminated(item.payload.doc.id);
  }

}
