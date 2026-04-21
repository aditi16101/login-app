// const API = "http://127.0.0.1:8000";
const API = "http://127.0.0.1:8001";

async function register() {
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;
    const confirmPassword = document.getElementById("confirm_password").value;

    if (password !== confirmPassword) {
        alert("Passwords do not match!");
        return;
    }

    const res = await fetch(`${API}/register`, {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({ username, password, confirm_password: confirmPassword })
    });

    const data = await res.json();

    console.log(data);

    if (res.ok) {
        alert(data.message || "Registered!");
    } else {
        alert(data.detail || JSON.stringify(data));
    }
}

async function login() {
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    const res = await fetch(`${API}/login`, {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({username, password})
    });

    if (res.ok) {
        window.location.href = "dashboard.html";
    } else {
        alert("Login failed");
    }
}

async function resetPassword() {
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    const res = await fetch(`${API}/reset-password`, {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({username, new_password: password})
    });

    if (res.ok) {
        alert("Password updated!");
    } else {
        alert("Error updating password");
    }
}