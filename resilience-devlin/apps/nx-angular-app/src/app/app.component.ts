import { Component, OnInit, ViewChild } from '@angular/core';
import { FormBuilder, FormGroup } from '@angular/forms';
import { HttpClient } from '@angular/common/http';
import { catchError, finalize, of } from 'rxjs';

@Component({
  selector: 'resilience-devlin-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
})
export class AppComponent implements OnInit {
  todoForm: FormGroup;

  constructor(private fb: FormBuilder, private _httpClient: HttpClient) {
    this.todoForm = this.fb.group({
      todoId: [0],
    });
  }

  ngOnInit(): void {}

  onSubmit() {
    console.log(this.todoForm.value);
    const id: number = this.todoForm.value.todoId;
    this._httpClient
      .get(`http://localhost:8000/todos/${id}`)
      .pipe(
        catchError((error) => {
          console.log('ERROR: ', error);
          return of(null);
        })
      )
      .subscribe((data) => {
        console.log('DATA: ', data);
      });
  }
}
