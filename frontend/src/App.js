import React from "react";
import Navbar from "react-bootstrap/Navbar";
import Container from "react-bootstrap/Container";
import TodoList from "./components/TodoList";
import Todo_Form from "./components/TodoForm";


function App() {
  return (
    <div>
      <Navbar bg="light" style={{marginBottom: "20px"}}>
        <Container>
          <Navbar.Brand herf="#">
            Todo App
          </Navbar.Brand>
        </Container>
      </Navbar>
      <Container>
        <Todo_Form/>
        <TodoList/>
      </Container>
    </div>
  );
}

export default App;
