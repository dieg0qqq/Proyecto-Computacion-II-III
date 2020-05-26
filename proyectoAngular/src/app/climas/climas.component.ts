import { Component, OnInit } from '@angular/core';
import { AeroSiglasService } from "../servicios/aero-siglas.service";
import { ClimasService } from "../servicios/climas.service";
import { HttpClient } from "@angular/common/http";


import { aeroSiglas } from '../modelos/aeroSiglas';
import { climas } from '../modelos/climas';

@Component({
  selector: 'app-climas',
  templateUrl: './climas.component.html',
  styleUrls: ['./climas.component.scss']
})
export class ClimasComponent implements OnInit {

  sql = 'http://127.0.0.1:8000';
  climas: climas[];
  siglas: aeroSiglas[];
  arrayClima: climas[];
  lista:boolean;

  selectedLevel;

  constructor(private climasService: ClimasService, private aeroSiglasService: AeroSiglasService,
    private httpClient: HttpClient) {

      httpClient.get(this.sql + '/api/clima/lista').subscribe((data: climas[]) => {
        this.climas = data;
      });

      httpClient.get(this.sql + '/api/siglas/lista').subscribe((data: aeroSiglas[]) => {
        this.siglas = data;
      });

     }

  ngOnInit(): void {
    this.lista = false;
  }

  listaClimas() {

    console.log(this.selectedLevel)
    this.httpClient.get(this.sql + '/api/climaXaeropuerto/' + this.selectedLevel)
    .subscribe((data:climas[]) => {
      this.arrayClima = data;
      console.log(this.arrayClima);
      this.lista = true;
    });
  };

}
