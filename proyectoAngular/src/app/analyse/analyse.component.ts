import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { AnaTextoService } from "../servicioAnalisis/ana-texto.service";


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
  resultado: Boolean;
  portada: Boolean;
  en: Boolean;

  ngOnInit(): void {
    this.resultado = false;
    this.portada = true;
    this.en = false;
   }
  
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
      }
    );
    this.resultado = true;
    this.portada = false;
    if (this.idioma != 'en') {
      this.en = true;
    }
  }
}
