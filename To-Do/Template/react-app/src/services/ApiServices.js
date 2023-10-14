import axios from 'axios';

function GetToDo() {
  return axios.get('http://127.0.0.1:8000/task/')
    .then(res => {
      return res.data;
    })
    .catch(error => {
      throw error;
    });
}

async function AddNewTask(task) {
  try {
    const res = await axios.post('http://127.0.0.1:8000/task/',{
        task_id : null,
        title : task.title.value,
        description : task.description.value,
        completed : task.status.value,

    });
    return res.data;
  } catch (error) {
    throw error;
  }
}

export { GetToDo, AddNewTask };

