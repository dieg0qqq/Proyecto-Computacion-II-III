import { TestBed } from '@angular/core/testing';

import { AeroSiglasService } from './aero-siglas.service';

describe('AeroSiglasService', () => {
  let service: AeroSiglasService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(AeroSiglasService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
