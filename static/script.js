// static/script.js

// Function to display the current date and time in UTC
function displayCurrentDateTime() {
    const now = new Date();
    const utcDate = now.toUTCString();
    const formattedDate = utcDate.replace(/ GMT.*$/, '').replace(/, /g, ' ');
    document.body.innerHTML += `<p>Current Date and Time (UTC): ${formattedDate}</p>`;
}

displayCurrentDateTime();