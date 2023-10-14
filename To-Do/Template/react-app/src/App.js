import './App.css';
import TaskList from './components/TaskList';
import Header from './components/Header/Header';

function App() {
  return (
    <>
      <div className="App-Main">
        <Header />
        <TaskList />
      </div>
    </>


  );
}
export default App;
