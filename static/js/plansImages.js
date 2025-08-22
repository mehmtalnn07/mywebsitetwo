const images = document.querySelectorAll('.resized-image');
const overlay = document.getElementById('full-screen-overlay');
const fullScreenImage = document.getElementById('full-screen-image');
const fullScreenImageNext = document.getElementById('full-screen-image-next');
const prevButton = document.getElementById('prev');
const nextButton = document.getElementById('next');
let currentIndex = 0;
let isAnimating = false;
const DURATION = 500;
function showImage(index) {
    fullScreenImage.src = images[index].src;
    fullScreenImage.style.transition = 'none';
    fullScreenImage.style.transform = 'translate(-50%, -50%) translateX(0)';
    fullScreenImage.style.opacity = '1';
    fullScreenImageNext.style.transition = 'none';
    fullScreenImageNext.style.opacity = '0';
    fullScreenImageNext.style.transform = 'translate(-50%, -50%) translateX(0)';
    overlay.classList.add('active');
    overlay.style.display = 'flex';
    requestAnimationFrame(() => { overlay.style.opacity = '1'; });
}
images.forEach((image, index) => {
    image.addEventListener('click', () => {
        currentIndex = index;
        showImage(currentIndex);
    });
});
overlay.addEventListener('click', (e) => {
    if (
        e.target !== fullScreenImage &&
        e.target !== fullScreenImageNext &&
        e.target !== prevButton &&
        e.target !== nextButton &&
        !prevButton.contains(e.target) &&
        !nextButton.contains(e.target)
    ) {
        closeFullScreenOverlay();
    }
});
function debounce(func, wait) {
    let timeout;
    return function () {
        const context = this, args = arguments;
        clearTimeout(timeout);
        timeout = setTimeout(() => func.apply(context, args), wait);
    };
}
function animateTransition(direction) {
    if (isAnimating) return;
    isAnimating = true;
    fullScreenImageNext.src = images[currentIndex].src;
    fullScreenImage.style.transition = 'none';
    fullScreenImageNext.style.transition = 'none';
    fullScreenImage.style.transform = 'translate(-50%, -50%) translateX(0)';
    fullScreenImage.style.opacity = '1';
    const incomingStartX = direction === 'next' ? '-100%' : '100%';
    const outgoingEndX  = direction === 'next' ? '100%'  : '-100%';
    fullScreenImageNext.style.opacity = '0';
    fullScreenImageNext.style.transform = `translate(-50%, -50%) translateX(${incomingStartX})`;
    void fullScreenImageNext.offsetWidth;
    fullScreenImage.style.transition = `transform ${DURATION}ms ease, opacity ${DURATION}ms ease`;
    fullScreenImageNext.style.transition = `transform ${DURATION}ms ease, opacity ${DURATION}ms ease`;
    fullScreenImage.style.transform = `translate(-50%, -50%) translateX(${outgoingEndX})`;
    fullScreenImage.style.opacity = '0';
    fullScreenImageNext.style.transform = 'translate(-50%, -50%) translateX(0)';
    fullScreenImageNext.style.opacity = '1';
    setTimeout(() => {
        fullScreenImage.src = fullScreenImageNext.src;
        fullScreenImage.style.transition = 'none';
        fullScreenImage.style.transform = 'translate(-50%, -50%) translateX(0)';
        fullScreenImage.style.opacity = '1';
        fullScreenImageNext.style.transition = 'none';
        fullScreenImageNext.style.opacity = '0';
        fullScreenImageNext.style.transform = 'translate(-50%, -50%) translateX(0)';
        isAnimating = false;
    }, DURATION);
}
const debouncedPrev = debounce((e) => {
    if (isAnimating) return;
    e.stopPropagation();
    currentIndex = (currentIndex > 0) ? currentIndex - 1 : images.length - 1;
    animateTransition('prev');
}, 150);
const debouncedNext = debounce((e) => {
    if (isAnimating) return;
    e.stopPropagation();
    currentIndex = (currentIndex < images.length - 1) ? currentIndex + 1 : 0;
    animateTransition('next');
}, 150);
prevButton.addEventListener('click', debouncedPrev);
nextButton.addEventListener('click', debouncedNext);
document.addEventListener('keydown', (e) => {
    if (!overlay.classList.contains('active') || isAnimating) return;
    if (e.key === 'ArrowLeft') {
        currentIndex = (currentIndex > 0) ? currentIndex - 1 : images.length - 1;
        animateTransition('prev');
    } else if (e.key === 'ArrowRight') {
        currentIndex = (currentIndex < images.length - 1) ? currentIndex + 1 : 0;
        animateTransition('next');
    } else if (e.key === 'Escape') {
        closeFullScreenOverlay();
    }
});
function closeFullScreenOverlay() {
    overlay.style.opacity = '0';
    setTimeout(() => {
        overlay.classList.remove('active');
        overlay.style.display = 'none';
        fullScreenImage.src = '';
    }, 500);
}
document.addEventListener('DOMContentLoaded', function () {
    const thumbs = document.querySelectorAll('.resized-image');
    thumbs.forEach((image, index) => {
        setTimeout(() => { image.classList.add('loaded'); }, index * 100);
    });
});