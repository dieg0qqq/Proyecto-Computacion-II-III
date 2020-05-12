import { Component, OnInit } from '@angular/core';
import { AeroSiglasService } from "../servicios/aero-siglas.service";
import { AerolineasService } from '../servicios/aerolineas.service';

import { aeroSiglas } from '../modelos/aeroSiglas';
import { aerolineas } from '../modelos/aerolineas';
import { vuelo } from "../modelos/vuelo";
import { HttpClient } from "@angular/common/http";

@Component({
  selector: 'app-buscador',
  templateUrl: './buscador.component.html',
  styleUrls: ['./buscador.component.scss']
})

export class BuscadorComponent implements OnInit {

  sql = 'http://127.0.0.1:8000';
  siglas: aeroSiglas[];
  arrayVuelo: vuelo[];
  arrayEspecifico: vuelo[];

  inputVuelo: String;
  selectedLevel;
  lista: boolean;
  vuelo: boolean;
  detalles:boolean;

  constructor(private aeroSiglasService: AeroSiglasService, private aerolinasService: AerolineasService, private httpClient: HttpClient) {
    httpClient.get(this.sql + '/api/siglas/lista').subscribe((data: aeroSiglas[]) => {
      this.siglas = data;
    });
    httpClient.get(this.sql + '/api/aerolineas/lista').subscribe((data) => {
      var array = data as JSON;
      // console.log(array);
      for (var i in array) {
        // console.log(array[i]['id'] + ":" + array[i]['nombreAerolinea']);
      }
    });
  }

  ngOnInit(): void {
    this.lista = false;
    this.vuelo = true;
    this.detalles = false;
  }
  buscarVuelo() {
    console.log(this.inputVuelo);
    this.httpClient.get(this.sql + '/api/vueloEspecifico/' + this.inputVuelo).subscribe((data: vuelo[]) => {
      console.log(data[0]['Aerolinea']);
      this.httpClient.get(this.sql + '/api/aerolineas/'+ data[0]['Aerolinea']).subscribe((datum) => {
        console.log(datum);
        data[0]['Aerolinea'] = datum[0]['nombreAerolinea'];
      });
      this.arrayEspecifico = data;
      console.log(this.arrayEspecifico);
    });
    this.detalles = true;
    this.vuelo = false;
  };
  listaAeropuerto() {
    console.log(this.selectedLevel)
    this.httpClient.get(this.sql + '/api/vuelosXaeropuerto/' + this.selectedLevel).subscribe((data: vuelo[]) => {
      this.arrayVuelo = data;
      console.log(this.arrayVuelo);
      this.lista = true;
    });
  };

}
