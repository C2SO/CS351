import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { HomePageComponent } from './home-page/home-page.component';
import { LoginComponent } from './login/login.component';
import { RegisterComponent } from './register/register.component';
import { SucessComponent } from './sucess/sucess.component';
import { AuthGuard } from '../core/guard/auth.guard';
import { UserResolver } from '../core/resolver/user.resolver';

const routes: Routes = [
  { path: '', redirectTo: 'home-page', pathMatch: 'full' },
  { path: 'login', component: LoginComponent, canActivate: [AuthGuard] },
  { path: 'register', component: RegisterComponent },
  { path: 'sucess', component: SucessComponent , resolve: { data: UserResolver}},
  { path: 'home-page', component: HomePageComponent},
  { path: '**', redirectTo: 'home-page', pathMatch: 'full' }
];
// add 'resolve: { data: UserResolver}' to a route to make that page reguire a user to be logged in

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class PublicRoutingModule { }
