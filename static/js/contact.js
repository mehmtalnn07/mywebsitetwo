function submitForm(event) {
    event.preventDefault();
    const form = document.getElementById('contactForm');
    const button = form.querySelector('button');
    button.disabled = true;
    button.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Sending...';
    setTimeout(() => {
        form.reset();
        const successMessage = document.createElement('div');
        successMessage.className = 'success-message';
        successMessage.innerHTML = '<i class="fas fa-check-circle"></i> Message Sent Successfully!';
        document.body.appendChild(successMessage);
        setTimeout(() => {
            successMessage.classList.add('show');
        }, 100);
        setTimeout(() => {
            successMessage.classList.remove('show');
            setTimeout(() => {
                successMessage.remove();
            }, 500);
        }, 4000);
        button.disabled = false;
        button.innerHTML = '<i class="fas fa-paper-plane"></i> Send Message';
    }, 2000);
}