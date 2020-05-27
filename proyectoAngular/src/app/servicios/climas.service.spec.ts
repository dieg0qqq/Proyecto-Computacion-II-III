import { TestBed } from '@angular/core/testing';

import { ClimasService } from './climas.service';

describe('ClimasService', () => {
  let service: ClimasService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(ClimasService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
