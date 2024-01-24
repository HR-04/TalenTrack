function askQuestion() {
    const inputElement = document.getElementById("input");
    const question = inputElement.value;

    if (question.trim() !== "") {
        // Send question to Flask endpoint
        fetch(`/ask?question=${question}`)
            .then(response => response.json())
            .then(data => {
                const responseContainer = document.getElementById("response");
                responseContainer.innerHTML = data.response;

                // Update chat history
                const chatHistoryContainer = document.getElementById("chat-history");
                chatHistoryContainer.innerHTML += `<p>You: ${question}</p>`;
                chatHistoryContainer.innerHTML += `<p>Bot: ${data.response}</p>`;

                // Clear input
                inputElement.value = "";
            });
    }
}
