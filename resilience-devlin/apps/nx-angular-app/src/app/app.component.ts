import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup } from '@angular/forms';
import { HttpClient } from '@angular/common/http';
import { finalize } from 'rxjs';
import { Todo } from './Todo';

@Component({
  selector: 'resilience-devlin-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
})
export class AppComponent implements OnInit {
  todoForm: FormGroup;
  isLoading = false;
  todo: Todo = {
    id: 0,
    activity: '',
  };

  constructor(private fb: FormBuilder, private _httpClient: HttpClient) {
    this.todoForm = this.fb.group({
      todoId: [0],
    });
  }

  ngOnInit(): void {}

  onSubmit() {
    const id: number = this.todoForm.value.todoId;
    this.todo = {
      id: 0,
      activity: '',
    };
    this.isLoading = true;
    this._httpClient
      .get<Todo>(`http://localhost:8000/todos/${id}`)
      .pipe(finalize(() => (this.isLoading = false)))
      .subscribe((data) => {
        console.log('DATA: ', data);
        this.isLoading = false;
        this.todo = data;
      });
  }
}
