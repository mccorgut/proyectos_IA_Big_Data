// Get references to the form and output div elements
const form = document.getElementById('uploadForm');
const output = document.getElementById('output');

// Add an event listener to the form that triggers when the form is submitted
form.addEventListener('submit', async (event) => {
    event.preventDefault(); // Prevent the default form submission
    const formData = new FormData(form); // Create a FormData object containing the form's data

    try {
        // Send the form data to the server (Flask backend) for analysis using fetch
        const response = await fetch('/analyze', {
            method: 'POST',
            body: formData // Attach the form data in the body of the request
        });

        // Parse the JSON response from the server
        const result = await response.json();

        if (response.ok) {
            // If the response is successful, extract the relevant data from the result
            const animal = result.animal || 'Not detected'; // Default to 'Not detected' if no animal is found
            const funFacts = result.fun_facts || 'No fun facts available.'; // Default to a message if no fun facts are available
            const imageUrl = result.uploaded_image_url || ''; // Default to an empty string if no image URL is returned

            // Dynamically format the fun facts to display them in HTML
            const formattedFunFacts = formatFunFacts(funFacts);

            // Log the image URL (optional debugging)
            console.log(imageUrl);

            // Update the output div with the result
            output.innerHTML = `
                <div class="result">
                    <p><strong>Animal Detected:</strong> ${animal}</p>
                    <p><strong>Fun Facts:</strong></p>
                    <div class="fun-facts">
                        ${formattedFunFacts} <!-- Insert formatted fun facts here -->
                    </div>
                    <!-- Display the uploaded image if available -->
                    ${imageUrl ? `<img src="${imageUrl}" alt="Uploaded Image" style="border-radius: 8px;">` : ''}
                </div>
            `;
        } else {
            // If the response is not successful, display an error message
            output.innerHTML = `<p class="error">${result.error || 'Something went wrong.'}</p>`;
        }
    } catch (err) {
        // If there is an error during the fetch request, display the error message
        output.innerHTML = `<p class="error">Error: ${err.message}</p>`;
    }
});

// Function to format the fun facts text received from the server
function formatFunFacts(funFacts) {
    // Remove any `**` Markdown bold syntax by replacing it with <strong> HTML tags
    funFacts = funFacts.replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>');  // Replaces `**text**` with <strong>text</strong>

    // Split the fun facts into an array, assuming each fact starts with a number like '1.', '2.', '3.', etc.
    const factsArray = funFacts.split(/\d+\./).filter(Boolean);

    // Map each fact into a formatted HTML block, each with a numbered heading and description
    return factsArray.map((fact, index) => {
        // Split each fact into a title and description based on the newline
        const [title, ...description] = fact.trim().split('\n');
        return `
            <p><strong>${index + 1}. ${title.trim()}</strong></p>
            <p>${description.join(' ').trim()}</p>
        `;
    }).join(''); // Join all formatted facts into a single string of HTML
}
