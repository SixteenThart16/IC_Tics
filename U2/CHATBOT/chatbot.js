function sendMessage() {
    var userMessage = document.getElementById("user-message").value;
    var chatWindow = document.getElementById("chat-window");
    var chatBubble = document.createElement("div");
    chatBubble.classList.add("chat-bubble");
    chatBubble.textContent = userMessage;
    chatWindow.appendChild(chatBubble);
    document.getElementById("user-message").value = ""; 
}