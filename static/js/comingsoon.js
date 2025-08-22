document.addEventListener('DOMContentLoaded', () => {
    const targetDate = new Date('2025-12-31T00:00:00').getTime();
    const updateCountdown = () => {
        const now = new Date().getTime();
        const distance = targetDate - now;
        const days = Math.floor(distance / (1000 * 60 * 60 * 24));
        const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
        const seconds = Math.floor((distance % (1000 * 60)) / 1000);
        document.getElementById('days').innerText = days < 10 ? `0${days}` : days;
        document.getElementById('hours').innerText = hours < 10 ? `0${hours}` : hours;
        document.getElementById('minutes').innerText = minutes < 10 ? `0${minutes}` : minutes;
        document.getElementById('seconds').innerText = seconds < 10 ? `0${seconds}` : seconds;
        if (distance < 0) {
            clearInterval(interval);
            document.querySelector('.countdown-container').innerHTML = '<p class="expired">The time has come!</p>';
        }
    };
    updateCountdown();
    const interval = setInterval(updateCountdown, 1000);
});