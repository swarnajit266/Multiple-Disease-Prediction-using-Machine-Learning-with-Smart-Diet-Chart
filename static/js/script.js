const sidebar = document.querySelector(".sidebar");
const sidebarClose = document.querySelector("#sidebar-close");

function showForm(formId) {
    // Hide all forms
    const forms = document.querySelectorAll('.form');
    forms.forEach(form => {
        form.style.display = 'none';
        // Disable the form elements if they are hidden
        const inputs = form.querySelectorAll('input');
        inputs.forEach(input => input.disabled = true);
    });

    // Show the target form
    const targetForm = document.getElementById(formId);
    if (targetForm) {
        targetForm.style.display = 'block';
        
        // Enable the inputs of the visible form
        const inputs = targetForm.querySelectorAll('input');
        inputs.forEach(input => input.disabled = false);
    }

    // Set the disease type in hidden input if necessary
    const diseaseTypeInput = document.getElementById('disease_type');
    if (formId === 'form1') {
        diseaseTypeInput.value = 'heart';
    } else if (formId === 'form2') {
        diseaseTypeInput.value = 'diabetes';
    } else if (formId === 'form3') {
        diseaseTypeInput.value = 'dengue';
    }
}

sidebarClose.addEventListener("click", () => sidebar.classList.toggle("close"));