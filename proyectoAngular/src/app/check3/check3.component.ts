import { Component, OnInit } from '@angular/core';
import { AeroSiglasService } from "../servicios/aero-siglas.service";
import { ClimasService } from "../servicios/climas.service";
import { HttpClient } from "@angular/common/http";

import { aeroSiglas } from '../modelos/aeroSiglas';
import { climas } from '../modelos/climas';

@Component({
  selector: 'app-check3',
  templateUrl: './check3.component.html',
  styleUrls: ['./check3.component.scss']
})
export class Check3Component implements OnInit {

  sql = 'http://127.0.0.1:8000';
  climas: climas[];
  siglas: aeroSiglas[];
  arrayClima: climas[];
  datos: climas[];
  parte_sup:boolean;
  lista: boolean;
  
  id;
  button;


  constructor(private climasService: ClimasService, private aeroSiglasService: AeroSiglasService,
    private httpClient: HttpClient) {

      // httpClient.get(this.sql + '/api/clima/lista').subscribe((data: climas[]) => {
      //   this.climas = data;
      // });

      httpClient.get(this.sql + '/api/siglas/lista').subscribe((data: aeroSiglas[]) => {
        this.siglas = data;
      });

     }

  ngOnInit(): void {
    this.parte_sup = false;
    this.lista = true;
  }

  listaClimas() {
  
    this.httpClient.get(this.sql + '/api/clima/lista')
    .subscribe((data:climas[]) => {
      this.arrayClima = data;
      console.log(this.arrayClima);
    });
  };

  sup() {
    this.parte_sup = true;
    this.lista = false;
    console.log(this.id);
    this.httpClient.get(this.sql + '/api/array/' + this.id)
    .subscribe((data:climas[]) => {
      this.datos = data;
      console.log(this.datos);
    });
  };
}
