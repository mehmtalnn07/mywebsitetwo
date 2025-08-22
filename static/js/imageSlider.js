let currentIndex = 0;
const imageElement = document.getElementById('slider-image');

// Bu fonksiyon resim değiştirme işlemini gerçekleştirir.
function updateImage(images) {
    imageElement.style.opacity = 0;
    setTimeout(() => {
        imageElement.src = images[currentIndex];
        imageElement.style.opacity = 1;
    }, 500);
}

// Sayfa yüklendiğinde çalışacak ana kod bloğu
document.addEventListener('DOMContentLoaded', () => {
    // HTML'deki img etiketinden resim yollarını alıyoruz
    const imagesData = imageElement.getAttribute('data-image-paths');
    
    // Eğer resim yolları varsa, bir diziye dönüştürüyoruz
    if (!imagesData) {
        console.error("Resim yolları bulunamadı! Lütfen data-image-paths niteliğini kontrol edin.");
        return;
    }
    const images = imagesData.split(',');

    // Buton eventlerini ekliyoruz
    const nextButton = document.querySelector('.next');
    const prevButton = document.querySelector('.prev');

    if (nextButton && prevButton) {
        nextButton.addEventListener('click', function() {
            currentIndex = (currentIndex + 1) % images.length;
            updateImage(images);
        });

        prevButton.addEventListener('click', function() {
            currentIndex = (currentIndex - 1 + images.length) % images.length;
            updateImage(images);
        });
    }

    // Klavye eventlerini ekliyoruz
    document.addEventListener('keydown', function(event) {
        if (event.key === 'ArrowRight') {
            if (nextButton) nextButton.click();
        } else if (event.key === 'ArrowLeft') {
            if (prevButton) prevButton.click();
        }
    });

    // Sayfa yüklendiğinde ilk resmi göster
    updateImage(images);
});