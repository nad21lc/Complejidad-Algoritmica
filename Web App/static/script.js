document.addEventListener("DOMContentLoaded", function () {
    // Add an event listener to the "Buscar Dataset" button.
    const fileInput = document.getElementById("fileInput");

    // Listen for changes in the file input element
    fileInput.addEventListener("change", function () {
        const selectedFile = fileInput.files[0];
        if (selectedFile) {
            // You can perform actions with the selected file here.
            // For example, you can access the file using selectedFile.
            alert("Selected file: " + selectedFile.name);
        }
    });
    
    const mostrarGrafoButton = document.getElementById("grafo-button");
    const newCard = document.getElementById("new-card");

    mostrarGrafoButton.addEventListener("click", function () {
        newCard.classList.toggle("hidden");
    });
});
