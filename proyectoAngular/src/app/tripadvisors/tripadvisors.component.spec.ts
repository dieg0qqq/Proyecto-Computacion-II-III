import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { TripadvisorsComponent } from './tripadvisors.component';

describe('TripadvisorsComponent', () => {
  let component: TripadvisorsComponent;
  let fixture: ComponentFixture<TripadvisorsComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ TripadvisorsComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(TripadvisorsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
