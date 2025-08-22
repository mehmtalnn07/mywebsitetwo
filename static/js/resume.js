function sendEmail() {
    var subject = "";
    var body = "";
    var email = "mehmtalnn07@gmail.com";
    var mailtoLink = "mailto:" + email + "?subject=" + encodeURIComponent(subject) + "&body=" + encodeURIComponent(body);
    window.location.href = mailtoLink;
}
const images = document.querySelectorAll('.resized-image');
const overlay = document.getElementById('full-screen-overlay');
const fullScreenImage = document.getElementById('full-screen-image');
const prevButton = document.getElementById('prev');
const nextButton = document.getElementById('next');
let currentIndex = 0;
let scale = 1;
const scaleStep = 0.1;
function showImage(index) {
    fullScreenImage.src = images[index].src;
    overlay.classList.add('active');
    overlay.style.display = 'flex';
    setTimeout(() => {
        overlay.style.opacity = '1';
    }, 10);
}
images.forEach((image, index) => {
    image.addEventListener('click', () => {
        currentIndex = index;
        scale = 1;
        fullScreenImage.style.transform = `scale(${scale})`;
        showImage(currentIndex);
    });
});
overlay.addEventListener('click', (e) => {
    if (e.target !== fullScreenImage && e.target !== prevButton && e.target !== nextButton) {
        closeFullScreenOverlay();
    }
});
function debounce(func, wait) {
    let timeout;
    return function() {
        const context = this, args = arguments;
        clearTimeout(timeout);
        timeout = setTimeout(() => func.apply(context, args), wait);
    };
}
function slideLeft() {
    fullScreenImage.style.transition = 'transform 0.5s ease, opacity 0.5s ease';
    fullScreenImage.style.transform = 'translateX(100%) scale(0.5)';
    fullScreenImage.style.opacity = '0';
    setTimeout(() => {
        fullScreenImage.src = images[currentIndex].src;
        fullScreenImage.style.transform = 'translateX(0) scale(1)';
        fullScreenImage.style.opacity = '1';
    }, 500);
}
function slideRight() {
    fullScreenImage.style.transition = 'transform 0.5s ease, opacity 0.5s ease';
    fullScreenImage.style.transform = 'translateX(-100%) scale(0.5)';
    fullScreenImage.style.opacity = '0';
    setTimeout(() => {
        fullScreenImage.src = images[currentIndex].src;
        fullScreenImage.style.transform = 'translateX(0) scale(1)';
        fullScreenImage.style.opacity = '1';
    }, 500);
}
function playNextAnimation() {
    nextButton.classList.add('rotate-animation');
    setTimeout(() => {
        nextButton.classList.remove('rotate-animation');
    }, 1000);
}
const debouncedPrev = debounce((e) => {
    e.stopPropagation();
    currentIndex = (currentIndex > 0) ? currentIndex - 1 : images.length - 1;
    slideRight();
}, 300);
const debouncedNext = debounce((e) => {
    e.stopPropagation();
    currentIndex = (currentIndex < images.length - 1) ? currentIndex + 1 : 0;
    slideLeft();
    playNextAnimation();
}, 300);
prevButton.addEventListener('click', (e) => {
    e.stopPropagation();
    debouncedPrev(e);
});
nextButton.addEventListener('click', (e) => {
    e.stopPropagation();
    debouncedNext(e);
});
document.addEventListener('keydown', (e) => {
    if (overlay.classList.contains('active')) {
        if (e.key === 'ArrowLeft') {
            currentIndex = (currentIndex > 0) ? currentIndex - 1 : images.length - 1;
            slideRight();
        } else if (e.key === 'ArrowRight') {
            currentIndex = (currentIndex < images.length - 1) ? currentIndex + 1 : 0;
            slideLeft();
            playNextAnimation();
        } else if (e.key === 'Escape') {
            closeFullScreenOverlay();
        }
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
document.addEventListener('DOMContentLoaded', function() {
    const loadingScreen = document.getElementById('loadingScreen');
    setTimeout(() => {
        loadingScreen.classList.add('hidden');
    }, 2000);
});
document.addEventListener('DOMContentLoaded', function () {
    const images = document.querySelectorAll('.resized-image');
    images.forEach((image, index) => {
        setTimeout(() => {
            image.classList.add('loaded');
        }, index * 100);
    });
});
document.addEventListener('DOMContentLoaded', function () {
    const contents = document.querySelectorAll('.resume-content, .resume-content2');
    const observer = new IntersectionObserver(entries => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                observer.unobserve(entry.target);
            }
        });
    }, {
        threshold: 0.1
    });
    contents.forEach(content => {
        observer.observe(content);
    });
});