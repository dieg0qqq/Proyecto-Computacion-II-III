import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { InicioComponent } from "./inicio/inicio.component";
import { BuscadorComponent } from "./buscador/buscador.component";
import { InterfazadminComponent } from './interfazadmin/interfazadmin.component';
import { ClimasComponent} from './climas/climas.component';
import { AdminComponent } from './admin/admin.component';
import { TripadvisorsComponent } from './tripadvisors/tripadvisors.component';
import { Check3Component } from './check3/check3.component';


const routes: Routes = [
  { path: '', component: InicioComponent },
  { path: 'buscador', component: BuscadorComponent},
  { path: 'climas', component: ClimasComponent},
  { path: 'login', component: InterfazadminComponent},
  { path: 'login/admin', component: AdminComponent},
  { path: 'tripadvisor', component: TripadvisorsComponent},
  { path: 'login/examen', component: Check3Component}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
