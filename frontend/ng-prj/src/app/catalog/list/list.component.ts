import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http'; // используется для запроса на сервер
import {ApiService} from "./../../api.service";
import {ActivatedRoute} from "@angular/router";

@Component({
  selector: 'app-list',
  templateUrl: './list.component.html',
  styleUrls: ['./list.component.scss']
})
export class ListComponent implements OnInit {


  productList = {results: []};

  constructor(
    private http: HttpClient,
    private apiService: ApiService,
    private route: ActivatedRoute
  ) {
    this.getProductList({});

    this.route.params.subscribe(params => {
      if (params.hasOwnProperty('catId')){
        this.getProductList({cat:params.catId});
      }
      else if (params.hasOwnProperty('subCatId')){
        this.getProductList({subcat:params.subCatId});
      }
      else {
        this.getProductList({})
      }
    });
  }
 ngOnInit() :void {
  }

  getProductList(pk) {
    this.apiService.getProductList(pk).subscribe((res: any) => {
      this.productList = res;
    });


  }
}





