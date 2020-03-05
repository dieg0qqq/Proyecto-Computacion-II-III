import { TestBed } from '@angular/core/testing';

import { AnaTextoService } from './ana-texto.service';

describe('AnaTextoService', () => {
  let service: AnaTextoService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(AnaTextoService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
