import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http'; // используется для запроса на сервер
import {ApiService} from "./../../api.service";

@Component({
  selector: 'app-list',
  templateUrl: './list.component.html',
  styleUrls: ['./list.component.scss']
})
export class ListComponent implements OnInit {


  productList = {results: []};

  constructor(private http: HttpClient, private apiService: ApiService ) {
    this.getProductList();
  }
 ngOnInit() :void {
  }

  getProductList() {
    this.apiService.getProductList().subscribe((res: any) => {
      this.productList = res;
    });


  }
}





