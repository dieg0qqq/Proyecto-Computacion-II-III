import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { Check3Component } from './check3.component';

describe('Check3Component', () => {
  let component: Check3Component;
  let fixture: ComponentFixture<Check3Component>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ Check3Component ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(Check3Component);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
