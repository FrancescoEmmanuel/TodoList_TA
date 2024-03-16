import React from 'react';
import TodoItem from './TodoItem';

function TodoList({ todos, toggleTodo, deleteTodo, title, handleUpdate }) {
  return (
    <div className="bg-zinc-800 p-4 rounded text-white font-semibold">
      <ul>
        {todos.length === 0 && `NOTHING ${title.toUpperCase()}`}
        {todos.map((todo) => (
          <TodoItem
            {...todo}
            key={todo.id}
            toggleTodo={toggleTodo}
            deleteTodo={deleteTodo}
            handleUpdate={() => handleUpdate(todo.id)}
          />
        ))}
      </ul>
    </div>
  );
}

export default TodoList;
