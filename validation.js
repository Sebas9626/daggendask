// Get form element and submit button
var form = document.querySelector('.form');
var submitBtn = document.querySelector('#submitBtn');

// Add click event listener to submit button
submitBtn.addEventListener('submit', validate(this));

function validate(event) {
  // Prevent form submission
  event.preventDefault();

  // Initialize error message
  var errorMessage = '';

  // Get form field values
  var name = form.name.value;
  var email = form.email.value;
  var age = form.age.value;
  var password = form.password.value;
  var passwordConfirm = form.password_confirm.value;

  // Validate form field values
  if (name === '') {
    errorMessage += 'Please enter your name.\n';
  }
  if (email === '') {
    errorMessage += 'Please enter your email.\n';
  }
  if (age === '') {
    errorMessage += 'Please enter your age.\n';
  }
  if (password === '') {
    errorMessage += 'Please enter a password.\n';
  }
  if (passwordConfirm === '') {
    errorMessage += 'Please confirm your password.\n';
  }
  if (password !== passwordConfirm) {
    errorMessage += 'Passwords do not match.\n';
  }

  // If there is an error message, display it and return false
  if (errorMessage !== '') {
    alert(errorMessage);
    return false;
  }

  // If form is valid, submit it
  form.submit();
}