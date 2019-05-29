import { HttpClientModule } from '@angular/common/http';
import { NgModule } from '@angular/core';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { MatNativeDateModule } from '@angular/material';
import { BrowserModule } from '@angular/platform-browser';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { FlexLayoutModule } from '@angular/flex-layout';

import { PublicRoutingModule } from './public-routing.module';
import { MaterialModule } from '../core/material.module';
import { HomePageComponent } from './home-page/home-page.component';
import { LoginComponent } from './login/login.component';
import { SucessComponent } from './sucess/sucess.component';
import { RegisterComponent } from './register/register.component';
import { AuthGuard } from '../core/guard/auth.guard';
import { UserService } from '../core/service/user.service';
import { AuthService } from '../core/service/authentication.service';
import { UserResolver } from '../core/resolver/user.resolver';
import { UserPageComponent } from './user-page/user-page.component';
import { EditUserComponent } from './user-page/edit-user/edit-user.component';
import { EditUserResolver } from '../core/resolver/edit-user.resolver';

@NgModule({
  declarations: [
    HomePageComponent,
    LoginComponent,
    UserPageComponent,
    EditUserComponent
  ],
  imports: [
    BrowserModule,
    BrowserAnimationsModule,
    FlexLayoutModule,
    FormsModule,
    HttpClientModule,
    MaterialModule,
    MatNativeDateModule,
    ReactiveFormsModule,
    PublicRoutingModule
  ],
  providers: [
    AuthGuard,
    UserService,
    AuthService,
    UserResolver,
    EditUserResolver
  ]
})
export class PublicModule { }
