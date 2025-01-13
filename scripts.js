const apiUrl = "http://127.0.0.1:8000";

fetch(`${apiUrl}/museum/working-hours`)
    .then(response => response.json())
    .then(data => {
        const workingHoursList = document.getElementById("working-hours");
        data.forEach(item => {
            const li = document.createElement("li");
            li.textContent = `${item.day}: ${item.open_time} - ${item.close_time}`;
            workingHoursList.appendChild(li);
        });
    })
    .catch(error => {
        console.error("Error fetching working hours:", error);
        document.getElementById("working-hours").textContent = "Failed to load working hours.";
    });

const reservationForm = document.getElementById("reservation-form");
reservationForm.addEventListener("submit", (e) => {
    e.preventDefault();

    const name = document.getElementById("name").value;
    const email = document.getElementById("email").value;

    fetch(`${apiUrl}/reservation/reserve`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ name, email })
    })
        .then(response => response.json())
        .then(data => {
            const message = document.getElementById("reservation-message");
            message.textContent = "A confirmation code was sent to your email!";
            message.style.color = "green";
        })
        .catch(error => {
            const message = document.getElementById("reservation-message");
            message.textContent = "We couldn't send you a confirmation code! Please try again.";
            message.style.color = "red";
            console.error("Error making reservation:", error);
        });
});


const tokenForm = document.getElementById("token-form"); 
tokenForm.addEventListener("submit", (e) => {
    e.preventDefault();
    const email = document.getElementById("token-email").value;
    const token = document.getElementById("token").value;

    fetch(`${apiUrl}/confirm`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ email, token })
    })
        .then(response => response.json())
        .then(data => {
               const message = document.getElementById("token-message");
                window.location.href = "confirmation.html";

        })
        .catch(error => {
            const message = document.getElementById("token-message");
            message.textContent = "Failed to confirm your reservation. Please check your token and try again.";
            message.style.color = "red";
            console.error("Error confirming reservation:", error);
        });
});


fetch(`${apiUrl}/museum/virtual-tour`)
    .then(response => response.json())
    .then(data => {
        const virtualTourLink = document.getElementById("virtual-tour-link");
        virtualTourLink.href = data.virtual_tour_link;
    })
    .catch(error => console.error("Error fetching virtual tour link:", error));