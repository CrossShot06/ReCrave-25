const carousel = document.getElementById('glimpsesCarousel');
const images = carousel.querySelectorAll('img');
const imageWidth = images[0] ? images[0].offsetWidth + (parseFloat(getComputedStyle(carousel).gap) || 0) : 0; // Get width including gap
let currentIndex = 0;

function scrollCarousel() {
    if (images.length === 0) return;

    // Calculate target scroll position
    let targetScroll = currentIndex * imageWidth;

    // Check if we're at the end (or near the end)
    // If the next image would push us past the total scrollable width, reset to start
    if (targetScroll >= carousel.scrollWidth - carousel.clientWidth - (imageWidth / 2)) { // - imageWidth/2 to handle partial last image
        currentIndex = 0;
        targetScroll = 0;
    } else {
        currentIndex++;
    }
    
    // Animate the scroll
    carousel.scrollTo({
        left: targetScroll,
        behavior: 'smooth'
    });
}

// Adjust imageWidth if window resizes to ensure correct scrolling
window.addEventListener('resize', () => {
    if (images[0]) {
        imageWidth = images[0].offsetWidth + (parseFloat(getComputedStyle(carousel).gap) || 0);
        // Reset to ensure current image is aligned after resize
        carousel.scrollTo({
            left: currentIndex * imageWidth,
            behavior: 'auto'
        });
    }
});

// Start the slideshow (e.g., every 3 seconds)
let slideshowInterval = setInterval(scrollCarousel, 3000); // Change 3000 to adjust speed (milliseconds)

// Optional: Pause slideshow on hover
carousel.addEventListener('mouseenter', () => {
    clearInterval(slideshowInterval);
});

carousel.addEventListener('mouseleave', () => {
    slideshowInterval = setInterval(scrollCarousel, 3000);
});