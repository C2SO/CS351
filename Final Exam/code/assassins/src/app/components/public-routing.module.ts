import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { AuthGuard } from '../core/guard/auth.guard';
import { EditUserResolver } from '../core/resolver/edit-user.resolver';
import { UserResolver } from '../core/resolver/user.resolver';

import { EditUserComponent } from './user-page/edit-user/edit-user.component';
import { HomePageComponent } from './home-page/home-page.component';
import { LoginComponent } from './login/login.component';
import { RegisterComponent } from './register/register.component';
import { UserPageComponent } from './user-page/user-page.component';

const routes: Routes = [
  { path: '', redirectTo: 'home-page', pathMatch: 'full' },
  { path: 'login', component: LoginComponent, canActivate: [AuthGuard] },
  { path: 'register', component: RegisterComponent },
  { path: 'home-page', component: HomePageComponent},
  { path: 'user', component: UserPageComponent, resolve: { data: UserResolver }},
  { path: 'user/details/:id', component: EditUserComponent, resolve: {data : EditUserResolver} }
];
// add 'resolve: { data: UserResolver}' to a route to make that page reguire a user to be logged in

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class PublicRoutingModule { }
