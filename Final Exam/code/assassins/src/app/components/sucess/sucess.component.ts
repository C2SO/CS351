import { Component, OnInit } from '@angular/core';
import { AuthService } from 'src/app/core/service/authentication.service';

@Component({
  selector: 'app-sucess',
  templateUrl: './sucess.component.html',
  styleUrls: ['./sucess.component.scss']
})
export class SucessComponent implements OnInit {

  constructor(private auth: AuthService) { }
  isLoggedIn = false;    

  logout() {
    this.auth.doLogout()
  }

  ngOnInit() {
    this.isLoggedIn  = this.auth.isLoggedIn();
  }

}
