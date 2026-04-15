const API = "http://127.0.0.1:8000";

async function register() {
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    await fetch(`${API}/register`, {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({username, password})
    });

    alert("Registered!");
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