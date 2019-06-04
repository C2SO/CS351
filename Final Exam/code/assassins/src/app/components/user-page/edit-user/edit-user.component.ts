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
  items: Array<any>;
  loading = true;

  constructor(
    public firebaseService: FirebaseService,
    private route: ActivatedRoute,
    private fb: FormBuilder,
    private router: Router,
    public dialog: MatDialog,
    private userService: UserService
  ) { }

  ngOnInit() {
    this.loading = true;
    this.route.data.subscribe(routeData => {
      const data = routeData.data;
      this.getData();
      this.currId = this.userService.getCurrentUserId();
      if (this.currId === 'AIbu188nvXhYiTz8QwLBgYo7yWO2') {
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

  getData() {
    this.firebaseService.getUsers()
      .subscribe(result => {
        this.items = result;
        this.loading = false;
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

  getTargetName() {
    const value = this.item.target;
    if (value === '') {
      return 'No Target';
    } else {
      for (let i = 0; i < this.items.length; i++) {
        if (this.items[i].payload.doc.id === value) {
          return this.items[i].payload.doc.data().name;
        }
      }
    }
  }


}
