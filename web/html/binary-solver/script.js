// Get the input and output elements
const binaryInput = document.getElementById('binary-input');
const translateButton = document.getElementById('translate-button');
const utf8Output = document.getElementById('utf8-output');

// Add event listener to the translate button
translateButton.addEventListener('click', () => {
    // Get the binary input
    const binary = binaryInput.value;

    // Check if the input is a valid binary number
    if (!/^[01]+$/.test(binary)) {
        utf8Output.textContent = 'Invalid binary code';
        return;
    }

    // Split the binary code into 8-bit chunks
    const chunks = binary.match(/.{1,8}/g);

    // Convert each chunk to a UTF-8 character
    const utf8 = chunks.map(chunk => String.fromCharCode(parseInt(chunk, 2))).join('');

    // Display the UTF-8 output
    utf8Output.textContent = utf8;
});
