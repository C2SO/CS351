import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { MatDialog } from '@angular/material';
import { Router } from '@angular/router';
import { FirebaseService } from 'src/app/core/service/firebase.service';
import { UserService } from 'src/app/core/service/user.service';

@Component({
  selector: 'app-edit-user',
  templateUrl: './edit-user.component.html',
  styleUrls: ['./edit-user.component.scss']
})
export class EditUserComponent implements OnInit {

  exampleForm: FormGroup;
  item: any;
  editMode = false;

  validationMessages = {
    name: [
      { type: 'required', message: 'Name is required.' }
    ],
  };

  currId = '';
  isMod = false;

  constructor(
    public firebaseService: FirebaseService,
    private route: ActivatedRoute,
    private fb: FormBuilder,
    private router: Router,
    public dialog: MatDialog,
    private userService: UserService
  ) { }

  ngOnInit() {
    if (this.userService.getCurrentUserId() === this.userService.getModId()) {
      this.isMod = true;
    }
    this.route.data.subscribe(routeData => {
      const data = routeData.data;
      this.currId = this.userService.getCurrentUserId();
      if (this.currId === this.userService.getModId()) {
        this.router.navigate(['user/' + this.route.snapshot.data.data.payload.id]);
      } else if (this.currId !== this.route.snapshot.data.data.payload.id) {
        this.router.navigate(['user/' + this.currId]);
      }
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

  toggleEdit() {
    this.editMode = !this.editMode;
  }

  getUserEmailByUID() {
    return this.item.email;
  }


}
