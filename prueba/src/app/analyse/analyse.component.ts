import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { AnaTextoService } from "../ana-texto.service";


@Component({
  selector: 'app-analyse',
  templateUrl: './analyse.component.html',
  styleUrls: ['./analyse.component.scss']
})
export class AnalyseComponent implements OnInit {

  constructor(private http: HttpClient, private AnaTextoService: AnaTextoService) { }
  miTexto: Text;
  texto: String;
  pos_por: String;
  neg_por: String;
  neu_por: String;
  compound: String;
  conclusion: String;
  idioma: String;

  ngOnInit(): void { }
  
  analizar() {
    var anali;
    this.AnaTextoService.analisis(this.miTexto).subscribe(
      data => {
        console.log(this.miTexto);
        anali = data as JSON;
        this.texto = anali['texto'];
        this.pos_por = anali['%pos'];
        this.neg_por = anali['%neg'];
        this.neu_por = anali['%neu'];
        this.compound = anali['compound'];
        this.conclusion = anali['conclusion'];
        this.idioma = anali['idioma'];

        if (this.idioma == 'en') {
          document.getElementById("cambio").innerHTML =
            "<div id=\"DivCambiado\">" +
            "<h4>Texto introducido: </h4><label>" + this.texto + "</label >" +
            "<h4>Análisis del texto: </h4><label>" + this.conclusion + "</label >" +
            "<div id=\"accordion\">" +
            "<div id=\"headingOne\">" +
            "<h5 class=\"mb-0\" >" +
            "<button class=\"btn btn-link\" data-toggle=\"collapse\" data-target=\"#collapseOne\" aria-controls=\"collapseOne\" >" +
            "Informacion adicional <i class=\"fas fa-plus-circle\"></i> " +
            "</button>" +
            "</h5>" +
            "</div>" +
            "<div id = \"collapseOne\" class=\"collapse\" aria-labelledby=\"headingOne\" data-parent=\"#accordion\" >" +
            "<div>" +
            "<ul>" +
            "<li>" +
            "Compound: <label>" + this.compound + "</label>" +
            "</li>" +
            "<li>" +
            "Porcentajes:" +
            "<ul>" +
            "<li>" +
            "Positivo(%): <label>" + this.pos_por + "</label>" +
            "</li>" +
            "<li>" +
            "Negativo(%): <label>" + this.neg_por + "</label>" +
            "</li>" +
            "<li>" +
            "Neutro(%): <label>" + this.neu_por + "</label>" +
            "</li>" +
            "</ul>" +
            "</li>" +
            "</ul>" +
            "</div>" +
            "</div>" +
            "<a href=\"/analyse\">" +
            "<button id=\"buttonVolverAnalizer\" type=\"button\" class=\"btn btn-primary px-3\">" +
            "Volver <i class=\"fas fa-chevron-left\"></i>" +
            "</button>" +
            "</a>";
        }
        else {
          document.getElementById("cambio").innerHTML =
            "<div id=\"DivCambiado\">" +
            "<h4>Texto introducido: </h4><label>"+this.miTexto+"</label>"+
            "<h4> Traducción del texto introducido: </h4><label>" + this.texto + "</label >" +
            "<h4>Análisis del texto: </h4><label>" + this.conclusion + "</label >" +
            "<div id=\"accordion\">" +
            "<div id=\"headingOne\">" +
            "<h5 class=\"mb-0\" >"+
            "<button class=\"btn btn-link\" data-toggle=\"collapse\" data-target=\"#collapseOne\" aria-controls=\"collapseOne\" >"+
            "Informacion adicional <i class=\"fas fa-plus-circle\"></i> " +
            "</button>"+
            "</h5>"+
            "</div>"+
            "<div id = \"collapseOne\" class=\"collapse\" aria-labelledby=\"headingOne\" data-parent=\"#accordion\" >"+
            "<div>"+
            "<ul>" +
            "<li>" +
            "Compound: <label>" + this.compound + "</label>" +
            "</li>" +
            "<li>" +
            "Porcentajes:" +
            "<ul>" +
            "<li>" +
            "Positivo(%): <label>" + this.pos_por + "</label>" +
            "</li>" +
            "<li>" +
            "Negativo(%): <label>" + this.neg_por + "</label>" +
            "</li>" +
            "<li>" +
            "Neutro(%): <label>" + this.neu_por + "</label>" +
            "</li>" +
            "</ul>" +
            "</li>" +
            "</ul>" +
            "</div>"+
            "</div>" +
            "<a href=\"/analyse\">" +
            "<button id=\"buttonVolverAnalizer\" type=\"button\" class=\"btn btn-primary px-3\">" +
            "Volver <i class=\"fas fa-chevron-left\"></i>" +
            "</button>" +
            "</a>";
        }        
      }
    );
  }

  mostrar() {
    
  }
}
