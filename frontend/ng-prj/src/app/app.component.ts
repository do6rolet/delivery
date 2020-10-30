import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http'; // используется для запроса на сервер
import { environment } from "../environments/environment"; // backendUrl

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  title = 'ng-prj';
  name = 'Do6ro';
  productList = { results: []};
  constructor(private http: HttpClient) {
    this.getProductList();
  }

  getProductList(){
    console.log('Server request');
    this.http.get(`${environment.backendUrl}v1/generic/product_list`).subscribe((res: any) => {
        this.productList = res;
        console.log(this.productList)
    });
  }

}




