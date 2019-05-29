import { Component } from '@angular/core';
import { AuthService } from '../../core/service/authentication.service';
import { Router } from '@angular/router';
import { FormBuilder, FormGroup, Validators, FormControl } from '@angular/forms';
import { FirebaseService } from 'src/app/core/service/firebase.service';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.scss']
})
export class RegisterComponent {

  registerForm: FormGroup;
  errorMessage = '';
  successMessage = '';

  constructor(
    public authService: AuthService,
    private fb: FormBuilder,
    private firebaseService: FirebaseService
  ) {
    this.createForm();
  }

  createForm() {
    this.registerForm = this.fb.group({
      email: ['', Validators.required],
      password: ['', Validators.required],
      name: ['', Validators.required]
    });
  }

  tryRegister(value) {
    this.authService.doRegister(value)
      .then(res => {
        console.log(res);
        this.firebaseService.createUser(value).then(x => {
          this.errorMessage = '';
          this.successMessage = 'Your account has been created';
          this.resetFields();
        }, err => {
          console.log(err);
          this.errorMessage = err.message;
          this.successMessage = '';
        });
      }, err => {
        console.log(err);
        this.errorMessage = err.message;
        this.successMessage = '';
      });


  }

  resetFields() {
    this.registerForm = this.fb.group({
      name: new FormControl('', Validators.required),
      email: new FormControl('', Validators.required),
      password: new FormControl('', Validators.required),
    });
  }

}
