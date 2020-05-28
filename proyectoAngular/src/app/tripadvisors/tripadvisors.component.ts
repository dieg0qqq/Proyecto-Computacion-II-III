import { Component, OnInit } from '@angular/core';
import { HttpClient } from "@angular/common/http";
import { AerolineasService } from '../servicios/aerolineas.service';
import { TripadvisorsService } from '../servicios/tripadvisors.service';

import { tripadvisors } from '../modelos/tripadvisors';
import { aerolineas } from '../modelos/aerolineas';

@Component({
  selector: 'app-tripadvisors',
  templateUrl: './tripadvisors.component.html',
  styleUrls: ['./tripadvisors.component.scss']
})
export class TripadvisorsComponent implements OnInit {

  sql = 'http://127.0.0.1:8000/api';
  tripadvisors: tripadvisors[];
  aerolineas: aerolineas[];
  arrayTripadvisor: tripadvisors[];

  lista:boolean;
  selectedLevel;

  constructor(private tripadvisorService: TripadvisorsService, private aerolineasService: AerolineasService,
    private httpClient: HttpClient) { 

      httpClient.get(this.sql + '/tripadvisor/lista').subscribe((data: tripadvisors[]) => { 
        this.tripadvisors = data;
      });

      httpClient.get(this.sql + '/aerolinea/lista').subscribe((data: aerolineas[]) => { 
        this.aerolineas = data;
      });
    }

  ngOnInit(): void {
    this.lista = false;

  }

  listaAerolineas() {
    console.log(this.selectedLevel)
    this.httpClient.get(this.sql + '/tripadvisorXaerolinea/' + this.selectedLevel)
    .subscribe((data:tripadvisors[]) => { 
      this.arrayTripadvisor = data;
      console.log(this.arrayTripadvisor);
      this.lista = true;
    })


  }

}
