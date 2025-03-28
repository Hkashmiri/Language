document.addEventListener("DOMContentLoaded", function () {
    // Add click event to language cards
    const languageCards = document.querySelectorAll(".language-card");
    
    languageCards.forEach(card => {
        card.addEventListener("click", function () {
            const selectedLanguage = this.querySelector("h3").textContent.toLowerCase();
            window.location.href = `${selectedLanguage}.html`;
        });
    });

});

// audio lessons
function toggleSound(audioId) {
    const audioElement = document.getElementById(audioId);
    if (audioElement.paused) {
        audioElement.play();
    } else {
        audioElement.pause();
    }
}

