function submitForm() {
    var input = document.getElementById("input").value;
    var imageInput = document.getElementById("image");
    
    var formData = new FormData();
    formData.append("input", input);
    formData.append("image", imageInput.files[0]);

    fetch("/get_gemini_response", {
        method: "POST",
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("response-container").innerHTML = "<h2>The Response is:</h2>" + "<p>" + data.response + "</p>";
    })
    .catch(error => console.error('Error:', error));

    // Display the uploaded image
    var fileReader = new FileReader();
    fileReader.onload = function(e) {
        var imageContainer = document.getElementById("image-container");
        imageContainer.innerHTML = "<img src='" + e.target.result + "' alt='Uploaded Image'>";
    };
    fileReader.readAsDataURL(imageInput.files[0]);
}
