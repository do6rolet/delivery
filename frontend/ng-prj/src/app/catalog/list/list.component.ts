import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http'; // используется для запроса на сервер
import {environment} from "../../../environments/environment";// backendUrl

@Component({
  selector: 'app-list',
  templateUrl: './list.component.html',
  styleUrls: ['./list.component.scss']
})
export class ListComponent implements OnInit {


  productList = {results: []};

  constructor(private http: HttpClient) {
    this.getProductList();
  }
 ngOnInit() :void {
  }

  getProductList() {
    console.log('Server request');
    this.http.get(`${environment.backendUrl}v1/generic/product_list`).subscribe((res: any) => {
      this.productList = res;
      console.log(this.productList)
    });
  }
}





