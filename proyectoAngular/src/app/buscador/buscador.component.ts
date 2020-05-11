import { Component, OnInit } from '@angular/core';
import { AeroSiglasService } from "../servicioAeroSiglas/aero-siglas.service";
import { HttpClient } from "@angular/common/http";

@Component({
  selector: 'app-buscador',
  templateUrl: './buscador.component.html',
  styleUrls: ['./buscador.component.scss']
})
export class BuscadorComponent implements OnInit {

  sql = 'http://127.0.0.1:8000';
  constructor(private aeroSiglasService : AeroSiglasService, private httpClient : HttpClient) { 
    httpClient.get(this.sql + '/api/siglas/lista').subscribe((data) => {
      var array = data as JSON;
      console.log(array);
      for (var i in array){
        console.log(array[i]['id']+":"+array[i]['siglas']);
      }
    });
  }

  ngOnInit(): void {
  }

}
