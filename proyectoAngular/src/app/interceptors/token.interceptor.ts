import {
    HttpRequest,
    HttpHandler,
    HttpEvent,
    HttpInterceptor
} from '@angular/common/http';

import {
    Observable,
    throwError,
} from 'rxjs';

import { Injectable } from '@angular/core';
import { catchError } from 'rxjs/operators';


@Injectable()
export class TokenInterceptor implements HttpInterceptor {

    constructor() { }

    intercept(
        request: HttpRequest<any>,
        next: HttpHandler,
    ): Observable<HttpEvent<any>> {

        if (sessionStorage.getItem('token')) {
            request = request.clone({
                setHeaders: {
                    Authorization: 'Bearer ' + sessionStorage.getItem('token')
                }
            });
        }

        return next.handle(request)
            .pipe(catchError(err => {
                return throwError(err);
        }))
    }
}