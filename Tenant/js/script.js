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
document.addEventListener('DOMContentLoaded', function() {
    const username = localStorage.getItem('username');
    if (username) {
        document.getElementById('usernameBtn').textContent = "Hello, " + username;
    }
});


// Write the username
document.addEventListener('DOMContentLoaded', function() {
    const fullName = localStorage.getItem('fullName');
    if (fullName) {
        document.getElementById('usernameBtn').textContent = "Hello, " + fullName;
    }
});

//Write the Unit ID
document.addEventListener('DOMContentLoaded', function() {
    // Display unitID from local storage
    const unitID = localStorage.getItem('unitID'); // Retrieve unitID from local storage
    const unitIDDisplay = document.getElementById('unitIDDisplay');
    
    if (unitID) {
        unitIDDisplay.textContent = `Unit ID: ${unitID}`;
    } else {
        unitIDDisplay.textContent = 'Unit ID: Not Set';
    }

    // Your other existing code
});



