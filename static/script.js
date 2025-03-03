function analyzeSentiment() {
    let text = document.getElementById("text-input").value;
    if (!text) {
        alert("Please enter some text.");
        return;
    }

    fetch("/analyze", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text: text })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("result").innerText = "Sentiment: " + data.sentiment + " (Score: " + data.score.toFixed(2) + ")";
    })
    .catch(error => {
        console.error("Error:", error);
        document.getElementById("result").innerText = "Error: Unable to fetch API response.";
        document.getElementById("result").style.opacity = "1";
        document.getElementById("result").style.transform = "translateY(0)";

    });
}
