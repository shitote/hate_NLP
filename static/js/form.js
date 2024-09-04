// document.addEventListener('DOMContentLoaded', function() {
//     const signupForm = document.getElementById('signup-form');
//     const loginForm = document.getElementById('login-form');
//     const switchToLogin = document.getElementById('switch-to-login');
//     const switchToSignup = document.getElementById('switch-to-signup');

//     switchToLogin.addEventListener('click', function(e) {
//         e.preventDefault();
//         signupForm.classList.add('hidden');
//         loginForm.classList.remove('hidden');
//     });

//     switchToSignup.addEventListener('click', function(e) {
//         e.preventDefault();
//         loginForm.classList.add('hidden');
//         signupForm.classList.remove('hidden');
//     });
// });

// Select the password and confirm password input fields
var passwordInput = document.getElementById('signup-password');
var confirmPasswordInput = document.getElementById('signup-confirmpassword');

// Function to check password validity
function checkPasswordValidity() {
    var password = passwordInput.value;
    var confirmPassword = confirmPasswordInput.value;

    // Regular expression to check password complexity
    var passwordRegex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$/;

    // Remove previous validation classes
    passwordInput.classList.remove('valid', 'invalid');
    confirmPasswordInput.classList.remove('valid', 'invalid');

    // Check if both passwords are the same and meet the regex criteria
    if (password === confirmPassword && passwordRegex.test(password)) {
        passwordInput.classList.add('valid');
        confirmPasswordInput.classList.add('valid');
    } else {
        passwordInput.classList.add('invalid');
        confirmPasswordInput.classList.add('invalid');
    }
}

// Event listeners for real-time validation
passwordInput.addEventListener('input', checkPasswordValidity);
confirmPasswordInput.addEventListener('input', checkPasswordValidity);
