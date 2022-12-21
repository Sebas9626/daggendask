
function validate(form) {
  // Prevent form submission
  //event.preventDefault();

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
    else if (/[^a-zA-Z_-]/.test(name)) {
        errorMessage += 'Only letters are allowed in this field.\n';
    }

  if (email === '') {
    errorMessage += 'Please enter your email.\n';
  }
    else if (!((email.indexOf(".") > 0) &&
    (email.indexOf("@") > 0)) ||
    /[^a-zA-Z0-9.@_-]/.test(email)) {
        errorMessage += 'Invalid email. \n';
    }

  if (age === '') {
    errorMessage += 'Please enter your age.\n';
  }

  if (password === '') {
    errorMessage += 'Please enter a password.\n';
  }
    else if (! /[a-z]/.test(password) ||
    ! /[A-Z]/.test(password) ||
    ! /[0-9]/.test(password)) {
        errorMessage += 'Passwords require one each of a-z, A-Z and 0-9.\n';
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