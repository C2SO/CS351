import { Component, OnInit } from '@angular/core';
import { AuthService } from 'src/app/core/service/authentication.service';
import { UserService } from 'src/app/core/service/user.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-home-page',
  templateUrl: './home-page.component.html',
  styleUrls: ['./home-page.component.scss']
})
export class HomePageComponent implements OnInit {

  userId = '';
  isMod = false;

  constructor(
    public auth: AuthService,
    private userService: UserService,
    private router: Router) { }
  isLoggedIn = false;

  logout() {
    this.auth.doLogout();
  }

  ngOnInit() {
    this.isLoggedIn = this.auth.isLoggedIn();
    if (this.userService.getCurrentUserId() === 'AIbu188nvXhYiTz8QwLBgYo7yWO2') {
      this.isMod = true;
    }
  }

  navigateToUser() {
    this.userId = this.userService.getCurrentUserId();
    this.router.navigate(['/user/' + this.userId]);
  }

}
