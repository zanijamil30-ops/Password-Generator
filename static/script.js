function copyPassword() {
    const passwordText = document.getElementById("passwordText");
    if (passwordText && passwordText.innerText.trim() !== "") {
        navigator.clipboard.writeText(passwordText.innerText);
        alert("Password copied to clipboard!");
    } else {
        alert("No password to copy!");
    }
}

