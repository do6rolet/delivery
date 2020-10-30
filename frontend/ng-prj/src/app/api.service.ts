import { Injectable } from '@angular/core';
import {environment} from "./../environments/environment";
import {HttpClient} from "@angular/common/http";

@Injectable({
  providedIn: 'root'
})
export class ApiService {

  constructor(private http: HttpClient) { }

  getProductList() {
    return  this.http.get(`${environment.backendUrl}v1/generic/product_list`);

  }
}

