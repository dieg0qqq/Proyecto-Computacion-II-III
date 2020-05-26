import { Component, OnInit } from '@angular/core';
import { ChartOptions, ChartType, ChartDataSets } from 'chart.js';
import * as pluginDataLabels from 'chartjs-plugin-datalabels';
import { usuarios } from "../modelos/usuarios";
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { fromEventPattern } from 'rxjs';
import { Router } from '@angular/router';

// import { Component, OnInit } from '@angular/core';
// import { ChartOptions, ChartType, ChartDataSets } from 'chart.js';
import { Label, Color, MultiDataSet, SingleDataSet } from 'ng2-charts';
import { monkeyPatchChartJsLegend, monkeyPatchChartJsTooltip } from 'ng2-charts';
// import { vuelo } from "../modelos/vuelo";
// import { HttpClient } from "@angular/common/http";


@Component({
  selector: 'app-admin',
  templateUrl: './admin.component.html',
  styleUrls: ['./admin.component.scss']
})
export class AdminComponent implements OnInit {

  name: string;
  email: string;
  //variables para el grafico 1
    pieChartLabels: Label[];
    pieChartData: SingleDataSet[];
  // para mostrar los graficos si es que estan listos 
    chartReady: Boolean = false;
  // variables para el grafico 2
    barChartLabels: Label[];

  sql = 'http://127.0.0.1:8000';

  constructor(
    private router: Router,
    public http: HttpClient
   
    ) { 
      monkeyPatchChartJsTooltip();
    monkeyPatchChartJsLegend();
  }

  LogOut() {
    const endpoint = 'http://127.0.0.1:8000/api/logout';
    const headers = new Headers ({
      'Content-Type': 'application/json',
      'Authorization': "Bearer: " + sessionStorage.getItem('token')
    });
   
    this.http.post(endpoint, headers).toPromise().then((token:string) => {
      token = sessionStorage.getItem('token');
      console.log(token);
      this.router.navigate(['/login']);
    })
    .catch(error => {
      console.error(error);
      alert('Error al hacer logout');
    });
  
  }

  ngOnInit() {
    //grafica 1 = vuelos totales por cada aeropuerto
    this.http.get(this.sql+"/api/vuelos/contadorAeropuerto").subscribe((data)=>{
      var aeropuertos = new Array();
      var numero_vuelos = new Array();
      for (var i= 0; i < Object.keys(data).length; i++){
        aeropuertos.push(data[i]['aeropuertos']);
        numero_vuelos.push(data[i]['num_vuelos']);
      }
      this.pieChartLabels = aeropuertos;
      this.pieChartData = numero_vuelos;
      this.chartReady = true;
    });
    this.http.get(this.sql+"/api/vuelos/contadorDia").subscribe(data =>{
      var dia = new Array();
      var numero_vuelos = new Array();
      for (var i= 0; i < Object.keys(data).length; i++){
        dia.push(data[i]['date']);
        numero_vuelos.push(data[i]['views']);
      }
      console.log(numero_vuelos);
      var json_1 = {data : numero_vuelos, label: "vuelos"};
      console.log(json_1);
      var json = new Array();
      json.push(json_1);
      console.log(json);

      this.barChartLabels = dia;
      this.barChartData = json;
    });
  }
  // cosas necesarias para el grafico de pie
  public pieChartOptions: ChartOptions = {
    responsive: true,
  };
  public pieChartType: ChartType = 'pie';
  public pieChartLegend = true;
  public pieChartPlugins = [];

  // necesario para el grafico lineal de vuelos por fecha
  barChartOptions: ChartOptions = {
    responsive: true,
  };
  // barChartLabels: Label[] = ['Apple', 'Banana', 'Kiwifruit', 'Blueberry', 'Orange', 'Grapes'];
  barChartType: ChartType = 'bar';
  barChartLegend = true;
  barChartPlugins = [];

  barChartData: ChartDataSets[] = [
    { data: [45, 37, 60, 70, 46, 33]}
  ];




}
