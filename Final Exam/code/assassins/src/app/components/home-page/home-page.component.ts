import { Component, OnInit } from '@angular/core';
import { AuthService } from 'src/app/core/service/authentication.service';

@Component({
  selector: 'app-home-page',
  templateUrl: './home-page.component.html',
  styleUrls: ['./home-page.component.scss']
})
export class HomePageComponent implements OnInit {

  constructor(private auth: AuthService) { }
  isLoggedIn = false;    

  logout() {
    this.auth.doLogout()
  }

  ngOnInit() {
    this.isLoggedIn  = this.auth.isLoggedIn();
  }

}
