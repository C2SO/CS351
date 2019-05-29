import { Component, OnInit } from '@angular/core';
import { AuthService } from 'src/app/core/service/authentication.service';
import { UserService } from 'src/app/core/service/user.service';

@Component({
  selector: 'app-home-page',
  templateUrl: './home-page.component.html',
  styleUrls: ['./home-page.component.scss']
})
export class HomePageComponent implements OnInit {

  userId = this.userService.getCurrentUserId;

  constructor(
    private auth: AuthService,
    private userService: UserService) { }
  isLoggedIn = false;

  logout() {
    this.auth.doLogout();
  }

  ngOnInit() {
    this.isLoggedIn = this.auth.isLoggedIn();
  }

}
