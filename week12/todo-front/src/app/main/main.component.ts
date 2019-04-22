import { Component, OnInit } from '@angular/core';
import {ProviderService} from '../shared/services/provider.service';
import {ITaskList, ITask} from '../shared/models/models';

@Component({
  selector: 'app-main',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.css']
})

export class MainComponent implements OnInit {


  public name: any = '';
  public taskLists: ITaskList[] = [];
  public currentList: ITask[] = [];
  constructor(private provider: ProviderService) { }

  ngOnInit() {
    this.provider.getTaskLists().then(res => {
      this.taskLists = res;
    });
  }
  getTasks(taskList: ITaskList) {
    this.provider.getTasks(taskList).then(res => {
      this.currentList = res;
    });
  }
  removeTaskList(taskList: ITaskList) {
    this.provider.removeTaskList(taskList.id).then(res => {
      console.log(`${taskList.name} deleted`);
      this.provider.getTaskLists().then(r => {
        this.taskLists = r;
      });
    });
  }
  createTaskList() {
    if (this.name !== '') {
      this.provider.createTaskList(this.name).then(res => {
        this.name = '';
        this.taskLists.push(res);
      });
    }
  }
  updateTaskList(taskList: ITaskList) {
      this.provider.updateTaskList(taskList).then(res => {
        console.log(taskList.id + 'updated');
      });
  }

}
