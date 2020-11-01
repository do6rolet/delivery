import { Injectable } from '@angular/core';
import {environment} from "./../environments/environment";
import {HttpClient} from "@angular/common/http";

@Injectable({
  providedIn: 'root'
})
export class ApiService {

  constructor(private http: HttpClient) { }

  getCategoryList() {
    return  this.http.get(`${environment.backendUrl}v1/generic/category_list`);
  }

  getProductList(pk) {
    if (pk.hasOwnProperty('cat')) {
      return this.http.get(`${environment.backendUrl}v1/generic/product_list?category=${pk.cat}`);
    }
    if (pk.hasOwnProperty('subcat')) {
      return this.http.get(`${environment.backendUrl}v1/generic/product_list?subcategory=${pk.subcat}`);
    }

    return this.http.get(`${environment.backendUrl}v1/generic/product_list`);
  }
}

