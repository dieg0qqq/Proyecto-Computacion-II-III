import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class AnaTextoService {

  constructor(private http: HttpClient) { }

  analisis(miTexto) {
    // alert("Has introducido: " + this.miTexto)
    return this.http.post<any>('http://localhost:5000/vader_texto', { "texto": miTexto });
  }
}
