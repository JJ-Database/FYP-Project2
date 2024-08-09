// Dropdown Clicked
document.addEventListener('DOMContentLoaded', function() {
    var usernameBtn = document.getElementById('usernameBtn');
    var dropdownMenu = document.getElementById('dropdownMenu');

    usernameBtn.addEventListener('click', function() {
        // Toggle the display of the dropdown menu
        if (dropdownMenu.style.display === 'block') {
            dropdownMenu.style.display = 'none';
        } else {
            dropdownMenu.style.display = 'block';
        }
    });
});

// Write the username
// document.addEventListener('DOMContentLoaded', function() {
//     const username = localStorage.getItem('username');
//     if (username) {
//         document.getElementById('usernameBtn').textContent = "Hello, " + username;
//     }
// });


// Write the username
document.addEventListener('DOMContentLoaded', function() {
    const fullName = localStorage.getItem('fullName');
    if (fullName) {
        document.getElementById('usernameBtn').textContent = "Hello, " + fullName;
    }
});

// Function to check if the user is logged in
function isUserLoggedIn() {
    // Replace this with your actual login check logic
    // For example, check if a cookie or local storage item exists
    return sessionStorage.getItem("loggedIn") === "true";
}

// Redirect to login page if not logged in
function checkLogin() {
    if (!isUserLoggedIn()) {
        window.location.href = "loginForm.html";
    }
}

// Call the checkLogin function when the page loads
window.onload = checkLogin;
