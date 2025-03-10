document.addEventListener("DOMContentLoaded", () => {
    const fields = [
        { selector: "#id_name", style: "#e9ecef" },
        { selector: "#id_email", style: "#e9ecef" }
    ];

    fields.forEach(({ selector, style }) => {
        const field = document.querySelector(selector);
        if (field && field.value.trim() !== "") {
            field.setAttribute("readonly", "readonly"); // Prevent user edits
            field.style.backgroundColor = style; // Apply a styled background
        }
    });
});