import { HttpClient } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {
  title = 'frontend-app';
  visitas: number = 0;

  constructor(private http: HttpClient) {}

  ngOnInit(): void {
    this.http.get<{ visitas: number }>('http://localhost:8000/visitas').subscribe(data => {
      this.visitas = data.visitas;
    }, error => {
      console.error('Error fetching visitas:', error);
    });
  }
}
