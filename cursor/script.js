document.addEventListener('DOMContentLoaded', function() {
    const input = document.getElementById('todo-input');
    const addBtn = document.getElementById('add-btn');
    const todoList = document.getElementById('todo-list');

    // Function to add a task
    function addTask() {
        const task = input.value.trim();
        if (task === '') return;
        const li = document.createElement('li');
        li.textContent = task;

        // Add remove button
        const removeBtn = document.createElement('button');
        removeBtn.textContent = 'Remove';
        removeBtn.className = 'remove-btn';
        removeBtn.onclick = function() {
            li.remove();
        };

        li.appendChild(removeBtn);
        todoList.appendChild(li);
        input.value = '';
        input.focus();
    }

    // Add task on button click or Enter key
    addBtn.addEventListener('click', addTask);
    input.addEventListener('keydown', function(e) {
        if (e.key === 'Enter') {
            addTask();
        }
    });
});
