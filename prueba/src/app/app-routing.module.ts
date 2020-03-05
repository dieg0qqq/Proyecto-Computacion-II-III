import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { IndexComponent } from './index/index.component'
import { AnalyseComponent} from "./analyse/analyse.component";

const routes: Routes = [
  { path: '', component: IndexComponent },
  { path: 'analyse' , component: AnalyseComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
