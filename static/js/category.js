
function Save() {
    var categoryName = document.getElementById('categoryName').value
    var csrfToken = '{{ csrf_token }}'
  
    fetch('{% url "category" %}', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': csrfToken
      },
      body: JSON.stringify({
        name: categoryName
      })
    }).then((response) => {
      if (response.ok) {
        localStorage.setItem('categoryAdded', 'true')
        location.reload() // Reload the page
      } else {
        alert('Error adding category.')
      }
    })
  }
  
  window.onload = function () {
    var create_success = document.getElementById('message')
    // Check if the categoryAdded flag is set
    if (localStorage.getItem('categoryAdded') === 'true') {
      create_success.innerHTML = '<h5 class="bg-success ps-5 text-white">Category added successfully!</h5>'
  
      // Remove the success message after 5 seconds
      setTimeout(() => {
        create_success.innerHTML = '' // Clear the message
        localStorage.removeItem('categoryAdded') // Clear the flag
      }, 5000) // Delay of 5000 milliseconds (5 seconds)
    }
  }
  
  
  let deleteID = ''
  
  function setDeleteID(id) {
    console.log('Setting delete ID:', id) // Debugging: Log the ID being set
    deleteID = id // Store the ID of the category to delete
  }
  
  function itemDelete() {
    if (!deleteID) {
      console.error('Delete ID is not set!') // Log if ID is not set
      alert('No category ID set for deletion.') // Alert user
      return // Prevent further action if ID is not set
    }
  
    const baseDeleteUrl = "{% url 'delete_category' '0' %}".slice(0, -1)
    const url = `${baseDeleteUrl}${deleteID}/` // Base URL for delete category
    console.log('Constructed URL:', url) // Log the constructed URL
    // Redirect to the delete URL
    window.location.href = url 
}