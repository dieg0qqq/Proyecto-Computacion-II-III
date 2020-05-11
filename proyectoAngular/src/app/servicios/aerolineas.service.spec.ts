import { TestBed } from '@angular/core/testing';

import { AerolineasService } from './aerolineas.service';

describe('AerolineasService', () => {
  let service: AerolineasService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(AerolineasService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
