import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Router } from '@angular/router';
import { NgForm } from '@angular/forms';
import { ResourceLoader } from '@angular/compiler';

@Component({
  selector: 'app-interfazadmin',
  templateUrl: './interfazadmin.component.html',
  styleUrls: ['./interfazadmin.component.scss']
})
export class InterfazadminComponent implements OnInit {

  loading = false;
  submitted = false;
  returnUrl: string;
  messageError: string;
  blurredUser = false;
  blurredPass = false;

  constructor(
    private router: Router,
    public http: HttpClient
    /*private authenticationService: AuthenticationService*/
  ) {
    // redirect to home if already logged in
   /* if (this.authenticationService.currentUserValue) {
      this.router.navigate(['/']);
    }*/
  }

  doLogin() {
    const endpoint = 'http://localhost:4200/login';
    const data = {
      username: 'Diego',
      password: '12345'
    };

    this.http.post(endpoint, data)
    .toPromise()
    .then(token => {
      // console.log(result);
      sessionStorage.setItem('token', token);
    })
    .catch(error => {
      console.error(error);
      alert('Error al iniciar sesion');
    });
  }

  ngOnInit() {
    this.blurredUser = false;
    this.blurredPass = false;
    this.messageError = '';
  }

  async onSubmit(f: NgForm) {
    this.submitted = true;
    console.log(f.value);
    console.log(f.valid);

    if (f.valid) {
      this.loading = true;
      await this.delay(2000);
      /*this.authenticationService.login(f.value.username, f.value.password)
        .subscribe(
          (user: User) => {
            user.password = f.value.password;
            sessionStorage.setItem('currentUser', JSON.stringify(user));
            this.router.navigate(['/home']);
          },
          error => {
            this.router.navigate(['/login']);
            this.messageError = 'Error: usuario y/o password incorrectos.';
            this.loading = false;
          });*/
    }
  }

  delay(ms: number) { // esperamos 1 segundo para que se vea el spinner de carga
    return new Promise(resolve => setTimeout(() => resolve(), ms));
  }

  blur(campo: string) {
    this.messageError = '';
    switch (campo) {
      case 'username':
        this.blurredUser = true;
        break;
      case 'password':
        this.blurredPass = true;
        break;
      default:
        break;
    }
  }

}
