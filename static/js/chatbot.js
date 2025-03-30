document.addEventListener("DOMContentLoaded", function () {
    const sendBtn = document.getElementById("send-btn");
    const userInput = document.getElementById("user-input");
    const chatbox = document.getElementById("chatbox");

    function appendMessage(role, text) {
        const messageDiv = document.createElement("div");
        messageDiv.classList.add(role === "user" ? "user-message" : "bot-message");
        messageDiv.innerHTML = text;
        chatbox.appendChild(messageDiv);
        chatbox.scrollTop = chatbox.scrollHeight;
    }

    sendBtn.addEventListener("click", function () {
        const message = userInput.value.trim();
        if (message) {
            appendMessage("user", message);
            userInput.value = "";

            fetch("/chatbot/get_response/", {
                method: "POST",
                headers: {
                    "Content-Type": "application/x-www-form-urlencoded",
                    "X-CSRFToken": getCookie("csrftoken")
                },
                body: new URLSearchParams({ message })
            })
            .then(response => response.json())
            .then(data => appendMessage("bot", data.response))
            .catch(error => console.error("Error:", error));
        }
    });

    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.startsWith(name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
});
