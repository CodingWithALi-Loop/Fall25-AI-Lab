// Example: highlight input when focused
document.querySelectorAll('input, select').forEach(el => {
    el.addEventListener('focus', () => {
        el.style.borderColor = "#2575fc";
        el.style.boxShadow = "0 0 5px #6a11cb";
    });
    el.addEventListener('blur', () => {
        el.style.borderColor = "#ccc";
        el.style.boxShadow = "none";
    });
});
