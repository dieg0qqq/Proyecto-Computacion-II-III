import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ClimasComponent } from './climas.component';

describe('ClimasComponent', () => {
  let component: ClimasComponent;
  let fixture: ComponentFixture<ClimasComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ClimasComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ClimasComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
