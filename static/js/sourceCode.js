document.addEventListener('DOMContentLoaded', () => {
    const countdownElement = document.getElementById('countdown');
    const statusLine = document.getElementById('status-line');
    const targetDate = new Date('2024-12-31T00:00:00').getTime();
    const updateCountdown = () => {
        const now = new Date().getTime();
        const distance = targetDate - now;
        if (distance < 0) {
            countdownElement.innerText = '>> PERMISSION DENIED — CODE ACCESS RESTRICTED';
            statusLine.innerText = '>> Intrusion detected. Access terminated.';
            clearInterval(interval);
            return;
        }
        const days = Math.floor(distance / (1000 * 60 * 60 * 24));
        const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
        const seconds = Math.floor((distance % (1000 * 60)) / 1000);
        countdownElement.innerText = `Time remaining: ${days}d ${hours}h ${minutes}m ${seconds}s`;
    };
    const interval = setInterval(updateCountdown, 1000);
    updateCountdown();
    lottie.loadAnimation({
        container: document.getElementById('matrix-animation'),
        renderer: 'svg',
        loop: true,
        autoplay: true,
        path: '/static/animations/matrix.json'
    });
});
