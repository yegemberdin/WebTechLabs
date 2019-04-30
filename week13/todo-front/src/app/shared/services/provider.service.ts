import { Injectable } from '@angular/core';
import {MainService} from './main.service';
import {HttpClient} from '@angular/common/http';
import {IAuthResponse, ITask, ITaskList} from '../models/models';

@Injectable({
  providedIn: 'root'
})
export class ProviderService extends MainService {

  constructor(http: HttpClient) {
    super(http);
  }

  // view show_tasklists get and post
  getTaskLists(): Promise<ITaskList[]> {
    return this.get('http://127.0.0.1:8000/api/task_lists/',{});
  }

  createTaskList(namee: string): Promise<any> {
    return this.post('http://127.0.0.1:8000/api/task_lists/', {
      name: namee
    });
  }



// view show _currenttasklist get put delete
  removeTaskList(id: number): Promise<any> {
    return this.delet(`http://127.0.0.1:8000/api/task_lists/${id}/`, {});
  }

  updateTaskList(taskList: ITaskList): Promise<any> {
    return this.put(`http://127.0.0.1:8000/api/task_lists/${taskList.id}/`, {
      name: taskList.name
    });
  }

  // view show_current_tasks


  getTasks(taskList: ITaskList): Promise<ITask[]> {
    return this.get(`http://127.0.0.1:8000/api/task_lists/${taskList.id}/tasks`,{});
  }


  auth(login: any, password: any): Promise<IAuthResponse> {
    return this.post('http://127.0.0.1:8000/api/login/', {
      username: login,
      password: password
    });
  }

  logout(): Promise<any> {
    return this.post('http://127.0.0.1:8000/api/logout/', {
    });
  }



}
