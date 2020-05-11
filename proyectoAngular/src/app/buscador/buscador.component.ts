import { Component, OnInit } from '@angular/core';
import { AeroSiglasService } from "../servicios/aero-siglas.service";
import { AerolineasService } from '../servicios/aerolineas.service';
import { HttpClient } from "@angular/common/http";

@Component({
  selector: 'app-buscador',
  templateUrl: './buscador.component.html',
  styleUrls: ['./buscador.component.scss']
})

export class BuscadorComponent implements OnInit {

  sql = 'http://127.0.0.1:8000';
  constructor(private aeroSiglasService : AeroSiglasService,private aerolinasService : AerolineasService ,private httpClient : HttpClient) { 
    httpClient.get(this.sql + '/api/siglas/lista').subscribe((data) => {
      var array = data as JSON;
      console.log(array);
      for (var i in array){
        console.log(array[i]['id']+":"+array[i]['siglas'] + ":"+array[i]['nombre'] );
      }
    });

    httpClient.get(this.sql + '/api/aerolineas/lista').subscribe((data) => {
      var array = data as JSON;
      console.log(array);
      for (var i in array) {
        console.log(array[i]['id'] + ":" + array[i]['nombreAerolinea']);
      }
    });

  }

  ngOnInit(): void {
    
  }

}
