import { HttpClientModule } from '@angular/common/http';
import { NgModule } from '@angular/core';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { MatNativeDateModule } from '@angular/material';
import { BrowserModule } from '@angular/platform-browser';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { FlexLayoutModule } from '@angular/flex-layout';

import { AuthGuard } from '../core/guard/auth.guard';
import { AuthService } from '../core/service/authentication.service';
import { EditUserResolver } from '../core/resolver/edit-user.resolver';
import { PublicRoutingModule } from './public-routing.module';
import { MaterialModule } from '../core/material.module';
import { UserResolver } from '../core/resolver/user.resolver';
import { UserService } from '../core/service/user.service';

import { EditUserComponent } from './user-page/edit-user/edit-user.component';
import { HomePageComponent } from './home-page/home-page.component';
import { LoginComponent } from './login/login.component';
import { RegisterComponent } from './register/register.component';
import { SucessComponent } from './sucess/sucess.component';
import { UserPageComponent } from './user-page/user-page.component';

@NgModule({
  declarations: [
    HomePageComponent,
    LoginComponent,
    UserPageComponent,
    EditUserComponent,
    RegisterComponent,
    SucessComponent
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
