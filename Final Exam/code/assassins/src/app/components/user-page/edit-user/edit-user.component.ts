import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { FormBuilder, FormGroup, Validators, FormControl } from '@angular/forms';
import { MatDialog } from '@angular/material';
import { Router } from '@angular/router';
import { FirebaseService } from 'src/app/core/service/firebase.service';
import { AuthService } from 'src/app/core/service/authentication.service';

@Component({
  selector: 'app-edit-user',
  templateUrl: './edit-user.component.html',
  styleUrls: ['./edit-user.component.scss']
})
export class EditUserComponent implements OnInit {

  exampleForm: FormGroup;
  item: any;

  validationMessages = {
    name: [
      { type: 'required', message: 'Name is required.' }
    ],
  };

  constructor(
    public firebaseService: FirebaseService,
    private route: ActivatedRoute,
    private fb: FormBuilder,
    private router: Router,
    private auth: AuthService,
    public dialog: MatDialog
  ) { }

  ngOnInit() {
    this.route.data.subscribe(routeData => {
      const data = routeData.data;
      if (data) {
        this.item = data.payload.data();
        this.item.id = data.payload.id;
        this.createForm();
      }
    });
  }

  createForm() {
    this.exampleForm = this.fb.group({
      name: [this.item.name, Validators.required],
    });
  }

  getUserName() {
    return this.item.name;
  }

  onSubmit(value) {
    this.firebaseService.updateUser(this.item.id, value)
      .then(
        res => {
          this.router.navigate(['/user']);
        }
      );
  }

  cancel() {
    this.router.navigate(['/user']);
  }

}
