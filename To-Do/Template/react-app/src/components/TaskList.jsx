import React, { useState, useEffect } from 'react';
import Form from 'react-bootstrap/Form';
import InputGroup from 'react-bootstrap/InputGroup';
import Button from 'react-bootstrap/Button';
import './TaskList.css';
import { GetToDo, AddNewTask } from '../services/ApiServices'; // Assuming you have imported AddNewTask from ApiServices
import AddTask from './AddTask';

const TaskList = () => {
  const [tasks, setTasks] = useState([]);
  const [showAddTask, setShowAddTask] = useState(false);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const res = await GetToDo();
        console.log('Api Response', res);
        setTasks(res);
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };

    fetchData();
  }, []);

  const handleAddSubmit = (e) => {
    // Assuming you have a target variable that holds the new task data
    AddNewTask(e.target) // Pass your task data to AddNewTask
      .then(res => {
        setTasks(res);
        setShowAddTask(false); // Close the AddTask component after adding a new task
      })
      .catch(error => {
        console.error('Error adding task:', error);
      });
  }

  return (
    <div className="TaskListContainer">
      <Button variant="dark" className="addTask-button" onClick={() => setShowAddTask(true)}>
        Add New Task
      </Button>
      {showAddTask && <AddTask handleAddSubmit={handleAddSubmit} />} {/* Pass onSubmit callback */}
      {tasks.map((task) => {
        return (
          <div className="TaskInputCont" key={task.id}>
            <InputGroup className="mb-3">
              <InputGroup.Text id="basic-addon1">@</InputGroup.Text>
              <Form.Control
                value={task.title}
                placeholder="Title"
                aria-label="Title"
                aria-describedby="basic-addon1"
              />
            </InputGroup>
            <InputGroup>
              <InputGroup.Text>Note here</InputGroup.Text>
              <Form.Control
                value={task.description}
                as="textarea"
                aria-label="Note"
                placeholder="Text"
              />
            </InputGroup>
            <div className="buttons-cont">
              <Button variant="dark" className="button-i">
                Edit
              </Button>
              <Button variant="dark" className="button-i">
                Delete
              </Button>
              <label className="material-checkbox" htmlFor="checkboxId">
                <input type="checkbox" id="checkboxId" />
                <span className="checkmark"></span>
                {task.completed ? 'Completed' : 'Not Completed'}
              </label>
            </div>
          </div>
        );
      })}
    </div>
  );
};

export default TaskList;