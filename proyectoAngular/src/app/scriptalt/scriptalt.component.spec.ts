import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ScriptaltComponent } from './scriptalt.component';

describe('ScriptaltComponent', () => {
  let component: ScriptaltComponent;
  let fixture: ComponentFixture<ScriptaltComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ScriptaltComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ScriptaltComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
