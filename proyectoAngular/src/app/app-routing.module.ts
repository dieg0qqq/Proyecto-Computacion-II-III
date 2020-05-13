import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { InicioComponent } from "./inicio/inicio.component";
import { BuscadorComponent } from "./buscador/buscador.component";
import { InterfazadminComponent } from './interfazadmin/interfazadmin.component';
import { AdminComponent } from './admin/admin.component';

const routes: Routes = [
  { path: '', component: InicioComponent },
  { path: 'buscador', component: BuscadorComponent},
  { path: 'login', component: InterfazadminComponent},
  { path: 'admin', component: AdminComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
