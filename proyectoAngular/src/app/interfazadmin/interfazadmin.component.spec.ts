import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { InterfazadminComponent } from './interfazadmin.component';

describe('InterfazadminComponent', () => {
  let component: InterfazadminComponent;
  let fixture: ComponentFixture<InterfazadminComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ InterfazadminComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(InterfazadminComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
