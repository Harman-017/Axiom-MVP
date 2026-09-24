const form = document.getElementById("createForm");

form.addEventListener("submit", function (event) {
    event.preventDefault();

    const fullName = document.getElementById("fullName").value.trim();
    const email = document.getElementById("email").value.trim();
    const password = document.getElementById("password").value;
    const confirmPassword = document.getElementById("confirmPassword").value;

    // Check empty fields
    if (fullName === "" || email === "" || password === "" || confirmPassword === "") {
        alert("Please fill in all fields.");
        return;
    }

    // Check valid email
    const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

    if (!emailPattern.test(email)) {
        alert("Please enter a valid email address.");
        return;
    }

    // Check password length
    if (password.length < 8) {
        alert("Password must be at least 8 characters long.");
        return;
    }

    // Check passwords match
    if (password !== confirmPassword) {
        alert("Passwords do not match.");
        return;
    }

    alert("Account created successfully!");

    form.reset();
});