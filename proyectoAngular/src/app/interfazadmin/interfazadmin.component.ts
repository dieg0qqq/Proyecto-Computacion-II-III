import { Component, OnInit } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Router } from '@angular/router';
import { NgForm } from '@angular/forms';
import { usuarios } from '../modelos/usuarios';
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
  email: string;
  pass: string;

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
    const endpoint = 'http://127.0.0.1:8000/api/login';
    const data = {
      email: this.email,
      password: this.pass
    };

    this.http.post(endpoint, data)
    .toPromise()
    .then((token:string) => {
      console.log(token);
      sessionStorage.setItem('token', token);
      this.router.navigate(['/login/admin']);
      
    })
    .catch(error => {
      console.error(error);
      alert('Error al iniciar sesion');
    });

   

  }

  // getData() {
  //   const endpoint = 'http://127.0.0.1:8000/api/login';
  //   const headers = new HttpHeaders();

  //   headers.set('Authorization','Bearer' + sessionStorage.getItem('token'));
  //   this.http.get(endpoint, { headers: headers })
  //   .toPromise()
  //   .then(result => {
  //     console.log('Petición exitosa', result);
  //   }) 
  //   .catch(error => {
  //     if (error.status === 401) {
  //       console.log('Token no válido o enviado de forma incorrecta')
  //     } else {
  //       console.log('Otro error')
  //     }
  //   });
  // }

  getData() {
    const endpoint = 'http://127.0.0.1:8000/api/login';

    this.http.get(endpoint)
        .toPromise()
        .then(result => {
            console.log('Petición exitosa', result);
        })
        .catch(error => {
            if (error.status === 401) {
                // Unauthorized, quiere decir que tu token: o no es válido o no fue enviado de forma correcta.
            } else {
                // Otro error ocurrió.
            }
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
