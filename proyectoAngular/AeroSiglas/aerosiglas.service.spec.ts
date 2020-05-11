import { TestBed } from '@angular/core/testing';

import { AerosiglasService } from './aerosiglas.service';

describe('AerosiglasService', () => {
  let service: AerosiglasService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(AerosiglasService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
