document.addEventListener("DOMContentLoaded", () => {

  //''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
  // Define the 'request' function to handle interactions with the server
  function server_request(url, data={}, verb, callback) {
    return fetch(url, {
      credentials: 'same-origin',
      method: verb,
      body: JSON.stringify(data),
      headers: {'Content-Type': 'application/json'}
    })
    .then(response => response.json())
    .then(response => {
      if(callback)
        callback(response);
    })
    .catch(error => console.error('Error:', error));
  }

  //''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
  // References to frequently accessed elements
  let main = document.querySelector('main');
  let table = document.querySelector('.table');
  let template = document.querySelector('#new_row');
  let add_form = document.querySelector('form[name=add_user]');
  let edit_form = document.querySelector('form[name=edit_user]');

  //''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
  // Handle POST Requests
  add_form.addEventListener('submit', (event) => {
    // Stop the default form behavior
    event.preventDefault();

    alert('Feature is incomplete!');

  /*
    1. Grab the data from the input fields
    2. Grab the action and method attributes from the form
    3. Submit a server POST request and when the server responds...
      4. Insert a template row into the table
      5. Update the content of the newly added row with the ID, first_name, and last_name of the user
  */
  });

  //''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
  // Handle PUT and DELETE Requests
  main.addEventListener('click', (event) => {

    // Open edit form
    if(event.target.classList.contains('edit_button')) {
      main.dataset.mode = 'editing';

      let row = event.target.closest('.row');
      edit_form.querySelector('input[name=first_name]').value = row.children[1].innerText.trim();
      edit_form.querySelector('input[name=last_name]').value = row.children[2].innerText.trim();
      edit_form.dataset.id = row.dataset.id;
    }

    // Close edit form
    if(event.target.classList.contains('cancel_button')) {
      main.dataset.mode = 'viewing';
    }

    // Submit PUT request from the edit form
    /*
      1. Check if the 'save_button' was the clicked element
      2. Retrieve the ID, first_name, and last_name from the edit form
      3. Submit a server PUT request and when the server responds...
        4. Update the row corresponding to this user with the new data if successful
        5. Switch back the main container's mode to 'viewing'
    */

    // Submit DELETE request and delete the row if successful
    /*
      1. Check if the 'delete_button' was the clicked element
      2. Retrieve the ID from the closest row
      3. Submit a server DELETE request and when the server responds...
        4. Remove the row if successful
    */
  });

});