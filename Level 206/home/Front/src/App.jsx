import { useState, useEffect } from "react";

function App() {
  const [users, setUsers] = useState([])
  const [tasks, setTasks] = useState([])

  useEffect(() => {
    async function getUsers() {
      const res = await fetch("./src/python/users.txt");
      const text = await res.text();

      const data = text.trim().split('\n');
      setUsers(data)
    }

    async function getTasks(){
      const res = await fetch("./src/python/todoApp.txt");
      const text = await res.text()

      const data = text.trim().split('\n');
      setTasks(data)
    }

    getUsers();
    getTasks();
  }, []);

  return (
    <>
      <section>
        <h1>Registered Users | Password</h1>
        {
          users.map((el, id) => (
            <p key={id}>{id + 1}) {el}</p>
          ))
        }

        <h1>Already Tasks:</h1>
        {
          tasks.map((el, id) => (
            <p key={id}>{id + 1} | {el}</p>
          ))
        }
      </section>
    </>
  );
}

export default App;
