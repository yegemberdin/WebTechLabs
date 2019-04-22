import { Injectable } from '@angular/core';
import {MainService} from './main.service';
import {HttpClient} from '@angular/common/http';
import {ITask, ITaskList} from '../models/models';

@Injectable({
  providedIn: 'root'
})
export class ProviderService extends MainService {

  constructor(http: HttpClient) {
    super(http);
  }
  getTaskLists(): Promise<ITaskList[]> {
    return this.get('http://localhost:8000/api/task_lists/',{});
  }
  getTasks(taskList: ITaskList): Promise<ITask[]> {
    return this.get(`http://localhost:8000/api/task_lists/${taskList.id}/tasks`,{});
  }
  removeTaskList(id: number): Promise<any> {
    return this.delet(`http://localhost:8000/api/task_lists/${id}/`, {});
  }
  createTaskList(namee: string): Promise<any> {
    return this.post('http://localhost:8000/api/task_lists/', {
      name: namee
    });
  }
  updateTaskList(taskList: ITaskList): Promise<any> {
    return this.put(`http://localhost:8000/api/task_lists/${taskList.id}/`, {
      name: taskList.name
    });
  }
}
