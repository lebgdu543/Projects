document.addEventListener("DOMContentLoaded", function() {
    const loginForm = document.getElementById("login-form");
    const loginMessage = document.getElementById("login-message");
    const card = document.querySelector(".card");
  
    loginForm.addEventListener("submit", (event) => {
      event.preventDefault();
      const username = document.getElementById("username").value;
      const password = document.getElementById("password").value;
  
      // Simulate a login process
      if (username === "admin" && password === "password") {
        loginMessage.textContent = "Login successful!";
        loginMessage.style.color = "green";
        card.style.display = "block";
      } else {
        loginMessage.textContent = "Invalid username or password.";
        loginMessage.style.color = "red";
      }
    });

  });
  